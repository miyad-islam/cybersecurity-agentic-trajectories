"""
Standalone Dataset Validator CLI
Validates any cybersecurity trajectory dataset against Draft-7 JSON Schemas and IP hygiene.
"""

import argparse
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from pipeline.validators.syntax_checker import SecurityTrajectoryValidator

def main():
    parser = argparse.ArgumentParser(description="Validate cybersecurity trajectory dataset JSONL.")
    parser.add_argument("input_file", type=str, help="Path to input JSONL dataset")
    parser.add_argument("--schemas", type=str, default="pipeline/schemas/tools.json", help="Path to tools.json")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"[-] Error: File not found: {args.input_file}")
        sys.exit(1)

    schemas_path = os.path.join(os.path.dirname(__file__), args.schemas)
    if not os.path.exists(schemas_path):
        print(f"[-] Error: Schemas file not found: {schemas_path}")
        sys.exit(1)

    validator = SecurityTrajectoryValidator(schemas_path)
    total = 0
    passed = 0
    failed = 0

    print(f"[*] Validating {args.input_file} against {schemas_path}...")
    with open(args.input_file, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            total += 1
            try:
                record = json.loads(line)
            except Exception as e:
                print(f"[-] Line {idx}: JSON parse error: {e}")
                failed += 1
                continue

            valid, errors = validator.validate_trajectory(record)
            if valid:
                passed += 1
            else:
                failed += 1
                if failed <= 5:
                    print(f"[-] Record {record.get('id', idx)} failed validation: {errors}")

    pass_rate = (passed / total * 100) if total > 0 else 0
    print("\n================ Validation Summary ================")
    print(f"Total Trajectories: {total}")
    print(f"Passed:             {passed} ({pass_rate:.1f}%)")
    print(f"Failed:             {failed}")
    print("====================================================")

    if failed > 0:
        sys.exit(1)
    else:
        print("[+] All trajectories passed validation successfully!")

if __name__ == "__main__":
    main()
