# 🛡️ Autonomous Cybersecurity & SOC Incident Response Trajectories

[![Validation](https://img.shields.io/badge/JSON_Schema-Draft--07_Valid-brightgreen.svg)](pipeline/schemas/tools.json)
[![Sanitization](https://img.shields.io/badge/IP_Sanitization-RFC--5737_Compliant-blue.svg)](pipeline/validators/syntax_checker.py)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-2%2C000_Sample-yellow)](https://huggingface.co/datasets)
[![Gumroad](https://img.shields.io/badge/Gumroad-Commercial_10k_Package-red)](https://gumroad.com)

A production-grade dataset and verification pipeline for training autonomous Cybersecurity & SOC (Security Operations Center) agents in multi-turn tool calling, telemetry investigation, and incident containment.

![Cyber Defense Command](docs/cover.jpg)

---

## 🎯 Architecture & Trajectory Lifecycle

```
[ Security Incident Alert ]
          │
          ▼
┌───────────────────────────────────────┐
│ Turn 1: Initial Triage & Investigation│  <── Calls Splunk, Auth0, WAF, or CloudTrail
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│ Turn 2: Deep Forensics / Containment  │  <── Calls CrowdStrike, Zeek, or Shodan
│   (25% Injected Error & Recovery)     │  <── HTTP 429 / 504 Self-Correction
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│ Turn 3: Post-Incident Remediation     │  <── Final IOC verification & containment report
└───────────────────────────────────────┘
```

---

## 🚀 Commercial Release (10,000 Trajectories)

The full 10,000-trajectory commercial dataset is available for purchase on **[Gumroad](https://gumroad.com)** ($9.99 Launch Special) with a perpetual, royalty-free commercial training license.

### Package Includes:
1. `cybersecurity_trajectories_openai.jsonl` (10,000 production trajectories in native OpenAI format)
2. `cybersecurity_trajectories_sharegpt.json` (LLaMA-Factory / Axolotl / Unsloth ready)
3. `pipeline/schemas/tools.json` (12 Enterprise Draft-7 tool schemas)
4. `dataset_info.json` (1-click integration for fine-tuning frameworks)

---

## 🧪 Local Schema Validator CLI

You can validate any sample trajectory against our strict Draft-7 JSON schemas and RFC-5737 IP sanitization rules:

```bash
# Clone the repository
git clone https://github.com/miyad-islam/cybersecurity-agentic-trajectories.git
cd cybersecurity-agentic-trajectories

# Install dependencies
pip install -r requirements.txt

# Run the validation CLI
python validate_dataset.py --file test_cyber_sample.jsonl
```

### Validator Checks:
* ✅ Strict Draft-7 JSON Schema compliance across all 12 tool functions.
* ✅ Multi-turn conversation structural integrity (`system` $\rightarrow$ `user` $\rightarrow$ `assistant` $\rightarrow$ `tool` $\rightarrow$ `assistant`).
* ✅ Zero routable production IP leaks (strictly conforms to RFC-5737 test prefixes `198.51.100.0/24`, `203.0.113.0/24`, `192.0.2.0/24` and RFC-1918 private subnets).

---

## 📊 MITRE ATT&CK Matrix Coverage

| MITRE ATT&CK Tactic | Technique ID | Enterprise SOC Tool |
| :--- | :--- | :--- |
| **Initial Access** | T1190 Exploit Public-Facing Application | `waf_rule_audit`, `shodan_query` |
| **Execution** | T1059 Command and Scripting Interpreter | `crowdstrike_endpoint_telemetry` |
| **Persistence** | T1053 Scheduled Task / Cron Job | `osquery_fleet_query` |
| **Privilege Escalation** | T1078.004 Cloud IAM Role Hijacking | `aws_cloudtrail_lookup` |
| **Defense Evasion** | T1562 Impair Defenses | `suricata_alert_stream` |
| **Credential Access** | T1110.003 Password Spraying | `auth0_audit_logs` |
| **Discovery** | T1087 Account Discovery | `active_directory_ldap_search` |
| **Lateral Movement** | T1021 Remote Services (SSH/RDP) | `splunk_search` |
| **Collection** | T1560 Archive Collected Data | `virustotal_lookup` |
| **Exfiltration** | T1048 Exfiltration Over Alternative Protocol | `zeek_network_flows` |

---

## 📄 License
* Repository code and validation tools: **MIT License**.
* Free 2,000 Sample Dataset: **CC-BY-NC 4.0** (Research Only).
* Complete 10,000 Dataset: **Perpetual Commercial License** via Gumroad.
