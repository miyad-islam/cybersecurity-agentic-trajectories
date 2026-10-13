"""
Mock Cybersecurity Trajectory Generator CLI
Generates test trajectories locally using procedural simulation.
"""

import argparse
import json
import os
import sys

# Ensure local imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pipeline.generators.scenarios import generate_incident
from pipeline.generators.simulator import generate_full_trajectory
from pipeline.validators.syntax_checker import SecurityTrajectoryValidator

def main():
    parser = argparse.ArgumentParser(description="Generate synthetic cybersecurity trajectories.")
    parser.add_argument("--count", type=int, default=10, help="Number of trajectories to generate")
    parser.add_argument("--out", type=str, default="sample_trajectories.jsonl", help="Output JSONL path")
    parser.add_argument("--validate", action="store_true", help="Validate while generating")
    args = parser.parse_args()

    validator = None
    if args.validate:
        schemas_path = os.path.join(os.path.dirname(__file__), "pipeline", "schemas", "tools.json")
        validator = SecurityTrajectoryValidator(schemas_path)

    generated = 0
    with open(args.out, "w", encoding="utf-8") as f:
        for i in range(args.count):
            incident = generate_incident(i)
            traj = generate_full_trajectory(incident)
            
            if validator:
                is_valid, errors = validator.validate_trajectory(traj)
                if not is_valid:
                    print(f"[-] Validation error on sample {i}: {errors}")
                    continue
                    
            f.write(json.dumps(traj) + "\n")
            generated += 1

    print(f"[+] Successfully generated and wrote {generated} trajectories to {args.out}")

if __name__ == "__main__":
    main()
