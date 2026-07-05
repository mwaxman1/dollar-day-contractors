#!/usr/bin/env python3
"""
Gumroad product creation script for WA HVAC Newly Licensed Feed
Requires: GUMROAD_ACCESS_TOKEN environment variable
"""
import os
import requests
import json

# Product details
PRODUCTS = [
    {
        "name": "WA HVAC Newly Licensed Contractor Feed — Monthly",
        "description": """Get a weekly CSV every Monday with every HVAC contractor who got licensed in Washington state in the last 7 days.

**What you get:**
- Business name, owner name, phone, address
- License number, effective date, expiration date
- Specialty codes (HVAC, Refrigeration, etc.)
- UBI number for verification
- Delivered via email + web dashboard access

**Data source:** WA Dept of Labor & Industries (L&I) — public record, updated daily, fully legal to reuse for recruitment.

**Sample this week:** 2 new HVAC licenses (MINI SPLIT PROS in Seattle, PRINGLES POWER VAC in Pasco). 38 total in last 90 days.

**Why this works:** You're on job sites 10 hrs/day. You can't monitor license boards. This feed puts newly licensed techs in your inbox before competitors find them.

Cancel anytime. No contract.""",
        "price": 4900,  # $49.00 in cents
        "currency": "USD",
        "recurring": "monthly",
        "tags": ["hvac", "recruiting", "contractors", "washington", "leads"]
    },
    {
        "name": "WA HVAC Newly Licensed Contractor Feed — Pro Monthly",
        "description": """Everything in Starter, plus:

- Phone-verified contact enrichment (we call to confirm numbers)
- Outreach email templates that get replies
- Priority support
- Early access to Texas (TDLR) and California (CSLB) feeds when they launch

**Best for:** HVAC companies actively hiring 2+ techs/quarter who want to move fast.

$99/month. Cancel anytime.""",
        "price": 9900,
        "currency": "USD",
        "recurring": "monthly",
        "tags": ["hvac", "recruiting", "contractors", "washington", "leads", "pro"]
    },
    {
        "name": "WA HVAC Newly Licensed Contractors — 90-Day Backlog",
        "description": """One-time purchase. Instant download of ALL HVAC contractors licensed in Washington state in the last 90 days.

**Includes:** 38+ contractors with full details (business name, owner, phone, address, license #, effective date, specialty, UBI).

**Use case:** You're hiring NOW and need a candidate pool immediately. Or you want to see the data quality before subscribing.

**Data is current as of this week.** One-time $199. No subscription.""",
        "price": 19900,
        "currency": "USD",
        "recurring": None,
        "tags": ["hvac", "recruiting", "contractors", "washington", "leads", "backlog"]
    }
]

def create_product(product):
    token = os.environ.get("GUMROAD_ACCESS_TOKEN")
    if not token:
        print("ERROR: GUMROAD_ACCESS_TOKEN not set")
        return None
    
    url = "https://api.gumroad.com/v2/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    data = {
        "name": product["name"],
        "description": product["description"],
        "price": product["price"],
        "currency": product["currency"],
        "tags": ",".join(product["tags"]),
    }
    
    if product["recurring"]:
        data["subscription_duration"] = "monthly"
    
    resp = requests.post(url, headers=headers, data=data)
    
    if resp.status_code == 201:
        result = resp.json()
        print(f"✅ Created: {product['name']}")
        print(f"   Permalink: {result['product']['permalink']}")
        print(f"   Short URL: {result['product']['short_url']}")
        return result['product']
    else:
        print(f"❌ Failed: {product['name']}")
        print(f"   Status: {resp.status_code}")
        print(f"   Response: {resp.text}")
        return None

if __name__ == "__main__":
    print("Creating Gumroad products...")
    print("=" * 50)
    
    for product in PRODUCTS:
        result = create_product(product)
        if result:
            print(f"   🔗 https://gumroad.com/l/{result['permalink']}")
        print()
    
    print("Done! Set GUMROAD_ACCESS_TOKEN to run.")