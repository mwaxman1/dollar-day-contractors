#!/usr/bin/env python3
"""
Weekly refresh script for WA HVAC newly-licensed contractor feed.
Downloads latest WA L&I contractor data, filters for HVAC, finds licenses issued in last 7 days,
outputs CSV for subscribers.
"""
import csv
import requests
from datetime import datetime, timedelta
import os
import sys

DATA_URL = "https://data.wa.gov/api/views/m8qx-ubtq/rows.csv?accessType=DOWNLOAD&api_foundry=true"
OUTPUT_DIR = "/home/mike/projects/dollar-day-contractors/data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HVAC_KEYWORDS = ['HVAC', 'HEATING', 'VENTILAT', 'AIR CONDIT', 'REFRIGERAT', 'COOLING', 'FURNACE', 'BOILER', 'DUCT']

def download_latest():
    """Download the latest WA contractor CSV."""
    print(f"[{datetime.now()}] Downloading latest WA contractor data...")
    resp = requests.get(DATA_URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=180, stream=True)
    resp.raise_for_status()
    
    raw_path = os.path.join(OUTPUT_DIR, "wa_contractors_latest.csv")
    with open(raw_path, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"  Downloaded {os.path.getsize(raw_path)/1024/1024:.1f} MB")
    return raw_path

def filter_newly_licensed_hvac(raw_path, days_back=7):
    """Extract HVAC contractors licensed in the last N days."""
    cutoff = datetime.now() - timedelta(days=days_back)
    newly_licensed = []
    
    print(f"[{datetime.now()}] Filtering for HVAC contractors licensed since {cutoff.date()}...")
    with open(raw_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Filter active HVAC
            spec1 = row.get('SpecialtyCode1Desc', '').upper()
            spec2 = row.get('SpecialtyCode2Desc', '').upper()
            is_hvac = any(kw in spec1 or kw in spec2 for kw in HVAC_KEYWORDS)
            
            if not is_hvac or row.get('StatusCode') != 'A':
                continue
            
            # Check license effective date
            effective_str = row.get('LicenseEffectiveDate', '')
            try:
                effective = datetime.strptime(effective_str, '%m/%d/%Y')
                if effective >= cutoff:
                    newly_licensed.append({
                        'BusinessName': row.get('BusinessName', '').strip(),
                        'LicenseNumber': row.get('ContractorLicenseNumber', '').strip(),
                        'LicenseType': row.get('ContractorLicenseTypeCodeDesc', '').strip(),
                        'Address': row.get('Address1', '').strip(),
                        'City': row.get('City', '').strip(),
                        'State': row.get('State', '').strip(),
                        'Zip': row.get('Zip', '').strip(),
                        'Phone': row.get('PhoneNumber', '').strip(),
                        'LicenseEffectiveDate': effective_str,
                        'LicenseExpirationDate': row.get('LicenseExpirationDate', '').strip(),
                        'BusinessType': row.get('BusinessTypeCodeDesc', '').strip(),
                        'Specialty1': row.get('SpecialtyCode1Desc', '').strip(),
                        'Specialty2': row.get('SpecialtyCode2Desc', '').strip(),
                        'PrincipalName': row.get('PrimaryPrincipalName', '').strip(),
                        'UBI': row.get('UBI', '').strip(),
                        'DaysSinceLicensed': (datetime.now() - effective).days,
                    })
            except ValueError:
                continue
    
    # Sort by most recently licensed
    newly_licensed.sort(key=lambda x: x['DaysSinceLicensed'])
    return newly_licensed

def save_weekly_csv(contractors, output_path):
    """Save the weekly CSV for subscribers."""
    if not contractors:
        print("  No newly licensed HVAC contractors this week.")
        # Create empty file with headers
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['BusinessName', 'LicenseNumber', 'LicenseType', 'Address', 'City', 'State', 'Zip', 
                           'Phone', 'LicenseEffectiveDate', 'LicenseExpirationDate', 'BusinessType',
                           'Specialty1', 'Specialty2', 'PrincipalName', 'UBI', 'DaysSinceLicensed'])
        return 0
    
    fieldnames = list(contractors[0].keys())
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contractors)
    
    print(f"  Saved {len(contractors)} contractors to {output_path}")
    return len(contractors)

def main():
    try:
        raw_path = download_latest()
        contractors = filter_newly_licensed_hvac(raw_path, days_back=7)
        weekly_path = os.path.join(OUTPUT_DIR, f"wa_hvac_newly_licensed_{datetime.now().strftime('%Y-%m-%d')}.csv")
        count = save_weekly_csv(contractors, weekly_path)
        
        # Also save as "latest.csv" for easy access
        latest_path = os.path.join(OUTPUT_DIR, "wa_hvac_newly_licensed_latest.csv")
        save_weekly_csv(contractors, latest_path)
        
        print(f"[{datetime.now()}] Done. Found {count} newly licensed HVAC contractors this week.")
        return 0
    except Exception as e:
        print(f"[{datetime.now()}] ERROR: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())