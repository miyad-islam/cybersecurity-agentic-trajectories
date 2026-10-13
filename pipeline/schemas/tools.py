"""
12 Production Cybersecurity & SOC Incident Response Tool Schemas
Draft-7 JSON Schema Compliant for Function-Calling & Agentic Multi-Turn Fine-Tuning.
"""

from dataclasses import dataclass, asdict
from typing import List, Dict, Any
import json

TOOLS: List[Dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "splunk_search",
            "description": "Execute a search query against the enterprise SIEM (Splunk/Elastic) across security indexes (endpoint, auth, network).",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query string (SPL or Lucene syntax), e.g. 'index=security sourcetype=auth failed_login | stats count by src_ip'"
                    },
                    "earliest_time": {
                        "type": "string",
                        "description": "Start time boundary, e.g. '-4h', '-24h', or ISO-8601 timestamp"
                    },
                    "latest_time": {
                        "type": "string",
                        "description": "End time boundary, e.g. 'now', or ISO-8601 timestamp"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of events to return (1-500)",
                        "minimum": 1,
                        "maximum": 500
                    }
                },
                "required": ["query", "earliest_time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "aws_cloudtrail_lookup",
            "description": "Look up AWS CloudTrail management events to inspect IAM privilege escalation, STS assume role calls, or unauthorized resource mutations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_name": {
                        "type": "string",
                        "description": "Specific API event name, e.g. 'AssumeRole', 'CreateAccessKey', 'AttachUserPolicy', 'StopLogging'"
                    },
                    "username": {
                        "type": "string",
                        "description": "IAM username or assumed role ARN to filter by"
                    },
                    "start_time": {
                        "type": "string",
                        "description": "Start lookup window, e.g. '-6h' or ISO timestamp"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Max events to return",
                        "minimum": 1,
                        "maximum": 100
                    }
                },
                "required": ["event_name", "start_time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "suricata_alerts",
            "description": "Fetch Network Intrusion Detection System (IDS/IPS) alerts for suspicious network traffic, signatures, and anomaly triggers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "src_ip": {
                        "type": "string",
                        "description": "Source IP address to filter alerts"
                    },
                    "dest_ip": {
                        "type": "string",
                        "description": "Destination IP address to filter alerts"
                    },
                    "severity": {
                        "type": "integer",
                        "description": "Alert severity level (1=High, 2=Medium, 3=Low)",
                        "enum": [1, 2, 3]
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Max alerts to retrieve",
                        "minimum": 1,
                        "maximum": 100
                    }
                },
                "required": ["severity"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "nmap_scan",
            "description": "Perform an internal port scan and service banner enumeration against a designated target host or subnet.",
            "parameters": {
                "type": "object",
                "properties": {
                    "target": {
                        "type": "string",
                        "description": "Target hostname or IP address"
                    },
                    "ports": {
                        "type": "string",
                        "description": "Port range to scan, e.g. '22,80,443,3389' or '1-1024'"
                    },
                    "scan_type": {
                        "type": "string",
                        "description": "Scan mode",
                        "enum": ["syn", "service_version", "aggressive", "ping"]
                    }
                },
                "required": ["target", "scan_type"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "shodan_query",
            "description": "Query Shodan threat intelligence database to check public exposure, banner grabs, and open ports for an external IP or domain.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ip": {
                        "type": "string",
                        "description": "Target IPv4 address to inspect"
                    },
                    "history": {
                        "type": "boolean",
                        "description": "Whether to return historical scanning records"
                    }
                },
                "required": ["ip"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "virustotal_lookup",
            "description": "Query VirusTotal threat intelligence for SHA256/MD5 file hashes, malicious domains, or suspicious URLs.",
            "parameters": {
                "type": "object",
                "properties": {
                    "resource": {
                        "type": "string",
                        "description": "SHA256 hash, MD5 hash, domain, or IP address to check"
                    },
                    "resource_type": {
                        "type": "string",
                        "description": "Type of resource",
                        "enum": ["file", "domain", "ip_address", "url"]
                    }
                },
                "required": ["resource", "resource_type"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "cve_search",
            "description": "Search the National Vulnerability Database (NVD) and MITRE for known Common Vulnerabilities and Exposures (CVE).",
            "parameters": {
                "type": "object",
                "properties": {
                    "cve_id": {
                        "type": "string",
                        "description": "CVE identifier, e.g. 'CVE-2024-3094' or 'CVE-2023-44487'"
                    },
                    "software_name": {
                        "type": "string",
                        "description": "Optional software product name to filter vulnerabilities"
                    }
                },
                "required": ["cve_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "osquery_run",
            "description": "Execute read-only SQL queries via Osquery agent on an enterprise workstation or server to inspect running processes, open sockets, or persistence keys.",
            "parameters": {
                "type": "object",
                "properties": {
                    "host_id": {
                        "type": "string",
                        "description": "Target endpoint identifier or hostname"
                    },
                    "query": {
                        "type": "string",
                        "description": "SQL query against Osquery virtual tables, e.g. 'SELECT name, path, pid FROM processes WHERE on_disk = 0'"
                    }
                },
                "required": ["host_id", "query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "tcpdump_pcap_analyze",
            "description": "Analyze network packet captures (PCAP) for DNS tunneling, C2 beaconing intervals, or unauthorized TLS sessions.",
            "parameters": {
                "type": "object",
                "properties": {
                    "pcap_file": {
                        "type": "string",
                        "description": "Filename or path of the captured PCAP trace"
                    },
                    "filter_expression": {
                        "type": "string",
                        "description": "BPF filter expression, e.g. 'tcp port 443 and ip host 198.51.100.25'"
                    },
                    "detect_beaconing": {
                        "type": "boolean",
                        "description": "Run statistical jitter analysis to detect C2 heartbeats"
                    }
                },
                "required": ["pcap_file"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "velociraptor_artifact_collect",
            "description": "Trigger digital forensics artifact collection on an endpoint using Velociraptor (collect MFT records, Autoruns, Prefetch, or Shellbags).",
            "parameters": {
                "type": "object",
                "properties": {
                    "client_id": {
                        "type": "string",
                        "description": "Velociraptor endpoint client identifier"
                    },
                    "artifact_name": {
                        "type": "string",
                        "description": "Name of artifact to collect",
                        "enum": ["Windows.Forensics.Prefetch", "Windows.System.Autoruns", "Linux.Forensics.BashHistory", "Generic.System.MemoryDmp"]
                    }
                },
                "required": ["client_id", "artifact_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "auth0_audit_logs",
            "description": "Retrieve identity provider authentication audit events to detect password spraying, credential stuffing, or anomalous MFA bypass attempts.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_email": {
                        "type": "string",
                        "description": "User email address to investigate"
                    },
                    "event_code": {
                        "type": "string",
                        "description": "Event filter code, e.g. 'f' (failed login), 'pwd_leak', 'mfa_failure', 's' (success)"
                    },
                    "time_window": {
                        "type": "string",
                        "description": "Time window to query, e.g. '-12h'"
                    }
                },
                "required": ["time_window"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "iptables_block",
            "description": "Execute network firewall containment rule to drop incoming/outgoing packets from a confirmed malicious Command and Control (C2) or attacker IP.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ip_address": {
                        "type": "string",
                        "description": "IPv4 address or CIDR block to drop"
                    },
                    "chain": {
                        "type": "string",
                        "description": "Firewall chain",
                        "enum": ["INPUT", "FORWARD", "OUTPUT"]
                    },
                    "duration_seconds": {
                        "type": "integer",
                        "description": "Temporary ban duration in seconds (0 for permanent rule)",
                        "minimum": 0
                    },
                    "reason": {
                        "type": "string",
                        "description": "Mandatory audit justification for the block rule"
                    }
                },
                "required": ["ip_address", "chain", "reason"]
            }
        }
    }
]

def export_schemas_json(filepath: str) -> None:
    """Exports tools to Draft-7 JSON schema file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(TOOLS, f, indent=2)

if __name__ == "__main__":
    export_schemas_json("tools.json")
    print(f"Exported {len(TOOLS)} tool schemas successfully.")
