"""
Strict Draft-7 JSON Schema and RFC-5737 IP Validator
Ensures 100% adherence to declared tool definitions and zero PII/leaked IPs.
"""

import json
import re
import ipaddress
from typing import Dict, Any, List, Tuple
from jsonschema import Draft7Validator

class SecurityTrajectoryValidator:
    def __init__(self, schemas_path: str):
        with open(schemas_path, "r", encoding="utf-8") as f:
            tools_list = json.load(f)
        
        self.tool_validators = {}
        for tool in tools_list:
            func = tool.get("function", {})
            name = func.get("name")
            params = func.get("parameters", {})
            if name and params:
                self.tool_validators[name] = Draft7Validator(params)
                
        # Regex to find IPv4 addresses
        self.ipv4_regex = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

    def validate_trajectory(self, trajectory: Dict[str, Any]) -> Tuple[bool, List[str]]:
        errors = []
        messages = trajectory.get("messages", [])
        
        if not messages or len(messages) < 4:
            errors.append("Trajectory must have at least 4 messages (system, user, assistant, tool).")
            return False, errors
            
        tool_call_ids = set()
        
        for idx, msg in enumerate(messages):
            role = msg.get("role")
            content = msg.get("content") or ""
            
            # Check IP sanitization across all content
            for ip_match in self.ipv4_regex.findall(content):
                try:
                    ip_obj = ipaddress.ip_address(ip_match)
                    if not (ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_reserved or 
                            ip_obj in ipaddress.ip_network("198.51.100.0/24") or 
                            ip_obj in ipaddress.ip_network("203.0.113.0/24") or 
                            ip_obj in ipaddress.ip_network("192.0.2.0/24")):
                        errors.append(f"Message {idx} contains non-sanitized routable IP: {ip_match}")
                except ValueError:
                    continue
            
            if role == "assistant" and "tool_calls" in msg:
                for tc in msg["tool_calls"]:
                    tc_id = tc.get("id")
                    tool_call_ids.add(tc_id)
                    func = tc.get("function", {})
                    name = func.get("name")
                    raw_args = func.get("arguments", "{}")
                    
                    if name not in self.tool_validators:
                        errors.append(f"Undeclared tool called: {name}")
                        continue
                        
                    try:
                        args = json.loads(raw_args) if isinstance(raw_args, str) else raw_args
                    except Exception as e:
                        errors.append(f"Tool {name} arguments invalid JSON: {e}")
                        continue
                        
                    validator = self.tool_validators[name]
                    for err in validator.iter_errors(args):
                        errors.append(f"Tool {name} schema violation: {err.message}")

            elif role == "tool":
                tc_id = msg.get("tool_call_id")
                if tc_id not in tool_call_ids:
                    errors.append(f"Orphan tool response with ID: {tc_id}")

        return (len(errors) == 0), errors
