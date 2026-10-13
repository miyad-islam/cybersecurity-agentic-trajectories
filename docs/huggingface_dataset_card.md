---
license: cc-by-nc-4.0
task_categories:
- text-generation
language:
- en
tags:
- cybersecurity
- soc
- agentic
- tool-calling
- mitre-attack
- incident-response
- function-calling
- synthetic
size_categories:
- 1K<n<10K
---

# 🛡️ Autonomous Cybersecurity & SOC Agentic Incident Response Trajectories (Preview)

A curated dataset of high-fidelity, multi-turn tool-calling trajectories for training and evaluating autonomous Cybersecurity & Security Operations Center (SOC) agents. Generated with **Qwen 2.5 72B Instruct (Native BF16)** and validated against strict Draft-7 JSON Schemas and RFC-5737 IP sanitization rules.

## 🚀 Commercial Full Release (10,000 Trajectories)
* **Full 10,000-Row Dataset Available**: Perpetual commercial training license available on [Gumroad](https://gumroad.com) ($9.99 Launch Special).
* Includes both **OpenAI JSONL** and **LLaMA-Factory ShareGPT** formats, full tool definitions, and unredacted training benchmarks.

---

## 📊 Dataset Overview

* **Dataset Size (This Free Preview)**: 2,000 production trajectories
* **Full Commercial Size**: 10,000 production trajectories
* **Format**: OpenAI JSONL Multi-turn Tool-calling (`messages` with role `tool`, `tool_calls`, and structured JSON observation arguments)
* **Average Turns Per Incident**: 3.2 turns (Triage $\rightarrow$ Deep Forensics $\rightarrow$ Containment / Remediation)
* **Synthetic Sanitization**: 100% RFC-5737 compliant (No real-world private infrastructure IPs exposed)

---

## 🎯 MITRE ATT&CK Matrix Coverage

This dataset spans 10 critical MITRE ATT&CK enterprise tactics:

| MITRE ATT&CK Tactic | Technique Example | Primary Tool Invoked |
| :--- | :--- | :--- |
| **Initial Access** | T1190 Exploit Public-Facing App | `waf_rule_audit`, `shodan_query` |
| **Execution** | T1059 Command and Scripting | `crowdstrike_endpoint_telemetry` |
| **Persistence** | T1053 Scheduled Task / Cron Job | `osquery_fleet_query` |
| **Privilege Escalation** | T1078.004 Cloud IAM Role Hijacking | `aws_cloudtrail_lookup` |
| **Defense Evasion** | T1562 Impair Defenses | `suricata_alert_stream` |
| **Credential Access** | T1110.003 Password Spraying | `auth0_audit_logs` |
| **Discovery** | T1087 Account Discovery | `active_directory_ldap_search` |
| **Lateral Movement** | T1021 Remote Services (SSH/RDP) | `splunk_search` |
| **Collection** | T1560 Archive Collected Data | `virustotal_lookup` |
| **Exfiltration** | T1048 Exfiltration Over Alt Protocol | `zeek_network_flows` |

---

## 🛠️ Tool Ecosystem (12 Enterprise SOC Tools)

All agent trajectories interact with Draft-7 JSON schemas across 12 realistic enterprise tools:
1. `splunk_search` — Query security SIEM indexes with SPL.
2. `crowdstrike_endpoint_telemetry` — Triage host-level process trees, DLL injections, and memory dumps.
3. `virustotal_lookup` — Check hashes and file reputation against multi-engine AV scanners.
4. `aws_cloudtrail_lookup` — Audit AWS IAM role assumptions and STS tokens.
5. `shodan_query` — Query open ports and CVE vulnerability intelligence on external IPs.
6. `osquery_fleet_query` — SQL queries across distributed endpoint fleets.
7. `auth0_audit_logs` — Single Sign-On and enterprise authentication audit telemetry.
8. `suricata_alert_stream` — IDS/IPS deep packet inspection alert triage.
9. `zeek_network_flows` — Network metadata, DNS tunneling, and Bro/Zeek connection logs.
10. `active_directory_ldap_search` — Query domain controllers for privileged group memberships.
11. `waf_rule_audit` — Inspect Cloudflare/AWS WAF block/drop rule activations.
12. `pagerduty_trigger` — Escalate critical incidents to Tier-3 incident commanders.

---

## ⚡ Agentic Self-Correction & Error Recovery (25% Injected)

Unlike naive single-turn question-answering datasets, **25% of all trajectories feature realistic SOC environment failures**:
* **HTTP 429 Rate Limits**: Agent parses the rate limit, backs off, and switches to cached telemetry.
* **HTTP 504 SIEM Timeouts**: Agent narrows its SPL time window or filters on specific index partitions to recover.
* **Tool Schema Validation Failures**: Agent inspects schema error messages and resubmits correctly typed parameters.

---

## 📄 License & Terms

* **Free Hugging Face Sample (2,000 rows)**: Licensed under **CC-BY-NC 4.0** (Non-Commercial Research Use).
* **Commercial 10,000-Row Release**: Available on [Gumroad](https://gumroad.com) with a perpetual, royalty-free commercial training license for fine-tuning private and proprietary models.
