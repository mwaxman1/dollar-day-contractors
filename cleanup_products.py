
import requests
TOKEN = "nxCGKjK9zGCijg14aVHkSZmT9NSo71b5SDg-x_9gHio"
headers = {"Authorization": "Bearer " + TOKEN}

# Delete the duplicate (ID: q2stTvIjQhhcH1vcqJ0_3Q==)
r = requests.delete("https://api.gumroad.com/v2/products/q2stTvIjQhhcH1vcqJ0_3Q==", headers=headers)
print(f"Delete duplicate starter: {r.status_code} {r.text[:100]}")
