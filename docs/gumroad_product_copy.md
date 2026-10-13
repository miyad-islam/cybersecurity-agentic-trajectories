# 🛡️ Gumroad Product Listing Details

## Product Title
**Autonomous Cybersecurity & SOC Agentic Incident Response Trajectories (10,000 Dataset)**

## Subtitle / Tagline
10,000 production-grade multi-turn tool-calling trajectories across 10 MITRE ATT&CK tactics for training autonomous Tier-2/Tier-3 SOC AI agents.

## Price
* **Launch Special Price**: `$9.99` (Regular $49.00)

## Product Category
Software Development / Artificial Intelligence & Machine Learning Datasets

---

## Product Description (Copy & Paste to Gumroad)

```markdown
### Train Autonomous SOC & Cybersecurity Agents with Enterprise-Grade Tool Calling

Fine-tuning general LLMs on simple Q&A datasets is not enough for cybersecurity operations. Real SOC incident response requires multi-turn investigation, telemetry log querying, indicator of compromise (IOC) verification, containment actions, and resilient self-correction when queries fail.

This dataset provides **10,000 production-grade, multi-turn tool-calling trajectories** generated with **Qwen 2.5 72B Instruct (Native BF16)** and rigorously validated against Draft-7 JSON Schemas and RFC-5737 IP sanitization rules.

---

### 📦 What You Get in the Commercial Download:
1. **`cybersecurity_trajectories_openai.jsonl`**: Complete 10,000 multi-turn trajectories in native OpenAI function-calling format (`role: "tool"`, `tool_calls`, structured arguments).
2. **`cybersecurity_trajectories_sharegpt.json`**: Formatted for instant 1-click fine-tuning with **LLaMA-Factory**, Axolotl, Unsloth, and Hugging Face SFTTrainer.
3. **`tools.json`**: Full Draft-7 JSON Schemas for 12 enterprise security tools (Splunk, CrowdStrike, VirusTotal, AWS CloudTrail, Shodan, OSquery, Auth0, Suricata, Zeek, Active Directory, WAF, PagerDuty).
4. **`dataset_info.json`**: Pre-configured registry file for LLaMA-Factory integration.
5. **Perpetual Commercial Training License**: Train, fine-tune, and deploy internal or customer-facing AI agents with zero royalty restrictions.

---

### 🎯 MITRE ATT&CK Tactical Coverage:
Every trajectory is mapped to enterprise cyber defense scenarios spanning 10 MITRE ATT&CK tactics:
- **Initial Access** (T1190 Public App Exploitation, WAF Bypass)
- **Execution** (T1059 Powershell/Bash C2, EDR Telemetry)
- **Persistence** (T1053 Cron/Scheduled Tasks, Persistence Hooks)
- **Privilege Escalation** (T1078.004 Cloud IAM Hijacking, Privilege Abuse)
- **Defense Evasion** (T1562 Defense Impairment, Log Clearing)
- **Credential Access** (T1110.003 Password Spraying, Kerberoasting)
- **Discovery** (T1087 Account Discovery, Active Directory LDAP Enumeration)
- **Lateral Movement** (T1021 RDP/SSH Pivoting, Pass-the-Hash)
- **Collection** (T1560 Sensitive File Staging, Archive Collection)
- **Exfiltration** (T1048 DNS Tunneling & Alternate Protocol Exfiltration)

---

### ⚡ 25% Injected Error-Recovery Scenarios:
Unlike naive synthetic datasets where every tool call succeeds unrealistically:
- **Rate Limit Resilience (HTTP 429)**: Agent parses rate limit headers, backs off, and queries fallback caches.
- **SIEM Timeout Adaptation (HTTP 504)**: Agent narrows SPL time windows and indexes to overcome query limits.
- **Schema Self-Correction**: Agent inspects validation errors and re-issues properly typed arguments.

---

### 🛡️ Commercial License Terms:
Perpetual, non-exclusive, worldwide commercial license to use this dataset for fine-tuning, training, evaluating, and deploying commercial AI models, internal security tools, and SaaS applications.
```

---

## Media Files for Gumroad Upload:
* **Cover Image (16:9)**: `cybersecurity-agentic-trajectories/docs/cover.jpg`
* **Thumbnail (1:1)**: `cybersecurity-agentic-trajectories/docs/thumb.jpg`
* **File to Deliver**: `Cybersecurity_SOC_Agentic_Trajectories_Full_Package.zip` (generated automatically in `dist/commercial/`)
