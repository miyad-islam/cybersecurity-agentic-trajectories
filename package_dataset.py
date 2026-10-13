"""
Packaging and Format Conversion CLI
Converts cybersecurity trajectories into OpenAI JSONL and LLaMA-Factory formats.
Splits into 2,000-row preview sample and 10,000-row commercial package.
"""

import argparse
import json
import os
import zipfile

def convert_to_sharegpt(trajectory: dict) -> dict:
    """Converts OpenAI format to ShareGPT format compatible with LLaMA-Factory."""
    conversations = []
    tools = []
    
    for msg in trajectory.get("messages", []):
        role = msg.get("role")
        content = msg.get("content", "")
        
        if role == "system":
            conversations.append({"from": "system", "value": content})
        elif role == "user":
            conversations.append({"from": "human", "value": content})
        elif role == "assistant":
            if "tool_calls" in msg:
                tool_calls_str = json.dumps(msg["tool_calls"])
                val = f"{content}\nAction: {tool_calls_str}" if content else f"Action: {tool_calls_str}"
                conversations.append({"from": "gpt", "value": val})
            else:
                conversations.append({"from": "gpt", "value": content})
        elif role == "tool":
            conversations.append({
                "from": "observation",
                "value": content
            })
            
    return {
        "id": trajectory.get("id"),
        "conversations": conversations
    }

def main():
    parser = argparse.ArgumentParser(description="Package cybersecurity trajectories for release.")
    parser.add_argument("input_file", type=str, help="Validated trajectories JSONL")
    parser.add_argument("--outdir", type=str, default="dist", help="Output distribution directory")
    parser.add_argument("--sample_size", type=int, default=2000, help="Free sample size")
    args = parser.parse_args()

    os.makedirs(os.path.join(args.outdir, "huggingface_sample"), exist_ok=True)
    os.makedirs(os.path.join(args.outdir, "llama_factory"), exist_ok=True)
    os.makedirs(os.path.join(args.outdir, "commercial"), exist_ok=True)

    records = []
    with open(args.input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    total = len(records)
    print(f"[*] Processing {total} trajectories...")

    # 1. Write Hugging Face Sample
    sample_records = records[:args.sample_size]
    sample_path = os.path.join(args.outdir, "huggingface_sample", f"sample_{len(sample_records)}.jsonl")
    with open(sample_path, "w", encoding="utf-8") as f:
        for r in sample_records:
            f.write(json.dumps(r) + "\n")
    print(f"[+] Wrote {len(sample_records)} sample records to {sample_path}")

    # 2. Write LLaMA-Factory ShareGPT format
    sharegpt_records = [convert_to_sharegpt(r) for r in records]
    sharegpt_path = os.path.join(args.outdir, "llama_factory", "cybersecurity_trajectories_sharegpt.json")
    with open(sharegpt_path, "w", encoding="utf-8") as f:
        json.dump(sharegpt_records, f, indent=2)

    # dataset_info.json
    dataset_info = {
        "cybersecurity_agentic_trajectories": {
            "file_name": "cybersecurity_trajectories_sharegpt.json",
            "formatting": "sharegpt",
            "columns": {
                "messages": "conversations"
            }
        }
    }
    info_path = os.path.join(args.outdir, "llama_factory", "dataset_info.json")
    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(dataset_info, f, indent=2)
    print(f"[+] Exported LLaMA-Factory configuration to {info_path}")

    # 3. Create Commercial Package ZIP
    commercial_zip_path = os.path.join(args.outdir, "commercial", "Cybersecurity_SOC_Agentic_Trajectories_Full_Package.zip")
    with zipfile.ZipFile(commercial_zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(args.input_file, arcname="cybersecurity_trajectories_openai.jsonl")
        z.write(sharegpt_path, arcname="cybersecurity_trajectories_sharegpt.json")
        z.write(info_path, arcname="dataset_info.json")
        
        # Schemas
        schemas_file = os.path.join(os.path.dirname(__file__), "pipeline", "schemas", "tools.json")
        if os.path.exists(schemas_file):
            z.write(schemas_file, arcname="tools_schema.json")

    print(f"[+] Generated full commercial zip package: {commercial_zip_path} ({os.path.getsize(commercial_zip_path)} bytes)")

if __name__ == "__main__":
    main()
