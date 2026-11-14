"""Print the issue body for the outage findings in a summary file.

Prints nothing when the Worker reports no finding with severity "outage".
"""
import json
import sys

summary = json.load(open(sys.argv[1]))
outage = [a for a in summary.get("alerts", []) if a.get("severity") == "outage"]
if outage:
    print(f"The Worker reported these findings in the snapshot of {summary.get('generated_at')}:\n")
    for finding in outage:
        print(f"- **{finding['rule']}**: {finding['message']}")
    print("\nThis issue closes by itself when a later snapshot reports no outage finding.")
