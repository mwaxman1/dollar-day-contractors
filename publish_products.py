
import requests
import json

TOKEN = "nxCGKjK9zGCijg14aVHkSZmT9NSo71b5SDg-x_9gHio"
headers = {"Authorization": "Bearer " + TOKEN}

# List all products
r = requests.get("https://api.gumroad.com/v2/products", headers=headers)
data = r.json()
print("Products found:", len(data.get("products", [])))
for p in data.get("products", []):
    pid = p["id"]
    name = p["name"]
    published = p["published"]
    permalink = p.get("custom_permalink", p.get("permalink", "N/A"))
    print(f"  ID: {pid} | {name} | published={published} | permalink={permalink}")
    
    if not published:
        # Publish it
        pr = requests.put(f"https://api.gumroad.com/v2/products/{pid}", headers=headers, json={"published": True})
        print(f"    Publishing... status={pr.status_code} response={pr.text[:200]}")
