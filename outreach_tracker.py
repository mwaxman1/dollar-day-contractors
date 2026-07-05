#!/usr/bin/env python3
"""
Outreach tracker for WA HVAC feed launch.
Logs daily outreach activities and responses.
"""
import json
import os
from datetime import datetime
from pathlib import Path

TRACKER_FILE = Path("/home/mike/projects/dollar-day-contractors/outreach_log.json")

def load_log():
    if TRACKER_FILE.exists():
        with open(TRACKER_FILE) as f:
            return json.load(f)
    return {"entries": [], "metrics": {"samples_requested": 0, "paying_signals": 0, "subscribers": 0}}

def save_log(log):
    with open(TRACKER_FILE, "w") as f:
        json.dump(log, f, indent=2)

def add_entry(day, channel, action, target, response=None, notes=""):
    log = load_log()
    entry = {
        "timestamp": datetime.now().isoformat(),
        "day": day,
        "channel": channel,
        "action": action,
        "target": target,
        "response": response,
        "notes": notes
    }
    log["entries"].append(entry)
    save_log(log)
    print(f"Logged: Day {day} | {channel} | {action} -> {target}")

def update_metric(metric, delta=1):
    log = load_log()
    if metric in log["metrics"]:
        log["metrics"][metric] += delta
        save_log(log)
        print(f"Metric updated: {metric} = {log['metrics'][metric]}")

def show_summary():
    log = load_log()
    print("\n" + "="*60)
    print("OUTREACH SUMMARY")
    print("="*60)
    print(f"Total entries: {len(log['entries'])}")
    for k, v in log["metrics"].items():
        print(f"  {k}: {v}")
    print("\nRecent entries:")
    for e in log["entries"][-10:]:
        print(f"  Day {e['day']} | {e['channel']:20s} | {e['action']:30s} | {e['target'][:50]}")
    print("="*60)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        show_summary()
    elif sys.argv[1] == "log":
        # python outreach_tracker.py log "Day 1" "reddit" "posted" "r/HVAC" "3 upvotes, 2 comments asking for link"
        _, day, channel, action, target, *rest = sys.argv
        response = rest[0] if rest else None
        add_entry(day, channel, action, target, response)
    elif sys.argv[1] == "metric":
        _, metric, *rest = sys.argv
        delta = int(rest[0]) if rest else 1
        update_metric(metric, delta)
    elif sys.argv[1] == "summary":
        show_summary()
    else:
        print("Usage: python outreach_tracker.py [log|metric|summary] ...")