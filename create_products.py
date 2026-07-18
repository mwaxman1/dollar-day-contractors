
import requests
import json

TOKEN = 'nxCGKjK9zGCijg14aVHkSZmT9NSo71b5SDg-x_9gHio'
products = [{"name": "WA HVAC New License Alerts - Starter", "price": 4900, "description": "Weekly CSV of newly licensed HVAC contractors in Washington state. Perfect for hiring managers at 3-10 person HVAC shops looking for new talent.", "subscription_interval": "monthly", "custom_permalink": "wa-hvac-starter-weekly"}]

for p in products:
    url = 'https://api.gumroad.com/v2/products'
    headers = {'Authorization': 'Bearer ' + TOKEN}
    r = requests.post(url, headers=headers, json=p)
    print(f"Product {p['name']} Result: {r.status_code}")
    print(r.text)
    print("-" * 20)
