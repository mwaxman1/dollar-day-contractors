#!/usr/bin/env python3
"""Weekly refresh of TX TDLR contractor license data."""
import requests
import csv
import os
import sys
from datetime import datetime

BASE = "https://data.texas.gov/resource/7358-krk7.json"
LICENSE_TYPES = ["A/C Contractor", "Electrical Contractor"]

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_all():
    all_records = []
    for lt in LICENSE_TYPES:
        offset = 0
        limit = 50000
        while True:
            params = {
                "$limit": limit,
                "$offset": offset,
                "$where": f"license_type = '{lt}'"
            }
            r = requests.get(BASE, params=params, timeout=30)
            if r.status_code != 200:
                print(f"ERROR fetching {lt}: {r.status_code}", file=sys.stderr)
                break
            batch = r.json()
            if not batch:
                break
            all_records.extend(batch)
            print(f"  {lt}: fetched {len(batch)} (total {len(all_records)})")
            if len(batch) < limit:
                break
            offset += limit
    return all_records

def write_csv(records, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["business_name", "owner", "state", "city", "phone", "license_number", "license_type", "trade", "expiration_date"])
        for r in records:
            trade = "HVAC" if "A/C" in r.get("license_type", "") else "Electrical" if "Electric" in r.get("license_type", "") else "Plumbing"
            writer.writerow([
                r.get("business_name", ""),
                r.get("owner_name", ""),
                "TX",
                r.get("business_county", ""),
                "",
                r.get("license_number", ""),
                r.get("license_type", ""),
                trade,
                r.get("license_expiration_date_mmddccyy", "")
            ])
    print(f"Saved: {path} ({len(records)} records)")

if __name__ == "__main__":
    print(f"TX TDLR refresh started: {datetime.now().isoformat()}")
    records = fetch_all()
    write_csv(records, "tx_all_contractors.csv")
    print(f"Done. Total: {len(records)} records")
