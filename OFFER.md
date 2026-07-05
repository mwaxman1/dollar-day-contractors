# WA HVAC Newly Licensed Contractor Feed - Offer

## One-Sentence Value Prop
**Get weekly CSV alerts of newly licensed HVAC contractors in Washington state — so you can recruit them before your competitors do.**

---

## The Problem (Human-Scale Pain)
You're an HVAC owner with 3 techs trying to grow to 20. You're on job sites 10 hours/day. You can't monitor state licensing boards. You can't cold-call every applicant to verify licensure. You lose good techs to competitors who found them first.

---

## The Product
**Weekly CSV delivered every Monday** with every HVAC contractor who got their WA state license in the last 7 days:
- Business name, owner name, phone, address
- License number, effective date, expiration date
- Specialty codes (HVAC, Refrigeration, etc.)
- UBI number for verification

**Sample:** 2 new HVAC licenses this week in WA — MINI SPLIT PROS (Seattle) and PRINGLES POWER VAC (Pasco).

---

## Pricing
- **$49/month** — Weekly CSV via email + web dashboard access
- **$99/month** — Above + phone-verified contact enrichment + outreach email templates
- **$199 one-time** — 90-day historical backlog (all HVAC licenses issued in last 90 days)

---

## Why This Creates Real Value for Humans with 2 Hands
1. **Saves 5+ hours/week** of manual license-board monitoring
2. **First-mover advantage** — contact techs days after they're licensed, before they're hired
3. **Verified data** — straight from WA L&I, not scraped from job boards
4. **Agent delivers it** — zero ongoing work for you after setup

---

## 7-Day Traffic Plan (Agent-Executable Daily Tasks)

### Day 1 (Today)
- [ ] Create Gumroad product with CSV sample
- [ ] Deploy landing page to Vercel
- [ ] Post in r/HVAC: "Built a tool that alerts you when new HVAC techs get licensed in WA — looking for 3 beta testers at $29/mo"

### Day 2
- [ ] Reply to 10 Upwork "HVAC hiring" job posts with: "I run a weekly feed of newly licensed WA HVAC techs — 2 new ones this week. Want a sample?"
- [ ] Post in HVAC-Talk.com forum "Business Management" section

### Day 3
- [ ] Find 5 WA HVAC companies on LinkedIn (10-50 employees), message owners: "You're hiring techs. I send a weekly list of newly licensed HVAC contractors in WA. Want this week's list free?"

### Day 4
- [ ] Post in r/smallbusiness: "How do you find licensed tradespeople? Built a WA-state feed of newly licensed HVAC contractors — $49/mo saves 5 hrs/week"

### Day 5
- [ ] Create a 60-second Loom demo video, post to Twitter/X tagging @HVAC_School, @ACHRNews
- [ ] Email 10 WA HVAC supply houses (Ferguson, Johnstone, etc.): "Your contractors need techs. I have a weekly licensed-tech feed. Partnership?"

### Day 6
- [ ] Follow up on all Day 2-5 outreach
- [ ] If ≥3 paying signals: double down. If <3: pivot to Texas or California data.

### Day 7
- [ ] Weekly cron runs, generates fresh CSV
- [ ] Email subscribers with this week's list
- [ ] Review metrics: subscribers, churn, feedback
- [ ] Decide: continue, expand to TX/CA, or kill

---

## Success Metrics (14-Day Kill Rule)
- **Week 1:** ≥3 people ask for sample / say "take my money"
- **Week 2:** ≥14:** ≥3 paying subscribers at $49/mo
- **If either fails:** Pivot to next state (TX TDLR) or kill

---

## Technical Stack
- **Data source:** WA L&I open data (data.wa.gov) — updated daily, free, legal
- **Refresh:** Python script via cron (runs weekly, 2 min)
- **Delivery:** Email (SendGrid) + web dashboard (Vercel/Next.js)
- **Billing:** Gumroad (handles VAT, EU, refunds)
- **Landing:** Static HTML on Vercel

---

## Legal/Compliance
- WA L&I data is public record — explicitly licensed for reuse
- No PII beyond what the state publishes (business name, owner name, business phone/address)
- CAN-SPAM compliant: transactional emails to paying subscribers only
- Terms: "For recruitment purposes only. Do not resell raw data."