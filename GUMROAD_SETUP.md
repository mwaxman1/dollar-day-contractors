# Gumroad Setup - Manual Steps Required

## Why Manual?
Gumroad's signup/login flow has reCAPTCHA and session cookies that don't persist for API automation. The browser session works for page loads but not for API calls.

## Quick Manual Setup (2 minutes)

1. **Go to https://gumroad.com/signup**
2. **Sign up with email: darren@turn2threads.com**
3. **Set password: DarrenTurn2024!** (or your choice)
4. **Verify email if needed**

5. **Get Access Token:**
   - Go to: https://gumroad.com/settings/advanced
   - Click "Generate access token"
   - Copy the token (starts with `gz_` or similar)

6. **Create 3 Products via API** (I'll run this once you give me the token):

```bash
# Starter - $49/mo
curl -X POST https://api.gumroad.com/v2/products \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d "name=WA HVAC New License Alerts - Starter" \
  -d "description=Weekly CSV of newly licensed HVAC contractors in Washington state. Perfect for hiring managers at 3-10 person shops." \
  -d "price=4900" \
  -d "subscription_interval=monthly" \
  -d "custom_permalink=wa-hvac-starter"

# Pro - $99/mo  
curl -X POST https://api.gumroad.com/v2/products \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d "name=WA HVAC New License Alerts - Pro" \
  -d "description=Weekly CSV + monthly backlog (all licenses last 90 days) + hiring email templates + phone/email enrichment on 50%+ records." \
  -d "price=9900" \
  -d "subscription_interval=monthly" \
  -d "custom_permalink=wa-hvac-pro"

# Backlog - $199 one-time
curl -X POST https://api.gumroad.com/v2/products \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d "name=WA HVAC License Backlog - All 90 Days" \
  -d "description=One-time download: every HVAC contractor licensed in WA in the last 90 days (~38 records). Includes business name, license number, issue date, city, county, classification." \
  -d "price=19900" \
  -d "custom_permalink=wa-hvac-backlog"
```

7. **Give me the 3 product URLs/permalinks** - I'll wire them into the landing page buy buttons.

## Landing Page
Live at: https://mwaxman1.github.io/dollar-day-contractors/

Current buy buttons point to `#pricing` anchor - need real Gumroad checkout URLs.

## Data Pipeline Status
✅ Weekly WA L&I scraper (cron: Mondays 6 AM)
✅ Latest CSV: 2 newly licensed HVAC contractors this week
✅ GitHub Pages deployment working
✅ Outreach tracker initialized (Day 1 logged)
