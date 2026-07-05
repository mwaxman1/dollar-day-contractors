#!/usr/bin/env python3
"""
Deploy landing page to Vercel
"""
import subprocess
import os

os.chdir("/home/mike/projects/dollar-day-contractors")

# Create vercel.json for static deployment
vercel_config = {
    "version": 2,
    "builds": [
        {"src": "landing.html", "use": "@vercel/static"}
    ],
    "routes": [
        {"src": "/(.*)", "dest": "/landing.html"}
    ]
}

with open("vercel.json", "w") as f:
    import json
    json.dump(vercel_config, f, indent=2)

# Deploy
result = subprocess.run(["npx", "vercel", "--prod", "--yes"], capture_output=True, text=True, timeout=120)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
print("Exit code:", result.returncode)