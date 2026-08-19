---
name: competitor-watch
description: Research and monitor competitors from a marketing and sales go-to-market perspective. Use to compare positioning, target buyers, campaigns, partnerships, content/SEO, case studies, channel programs, geography, conversion paths and public offers; or to track meaningful changes over time for an agency client/prospect. Research batches must produce claims and pass verify-and-challenge before being treated as verified.
---

# Competitor Marketing & GTM Intelligence

## Goal

Help an agency understand **how competitors are going to market**, not merely what products they have.

This skill has two modes:

- **DEEP** — build competitor GTM playbooks and identify market patterns/white spaces.
- **WATCH** — monitor meaningful changes after the baseline has been created.

# Read first

- `clients/<slug>/client-context.md`
- latest prospect/company intelligence output
- prior `signals.jsonl`
- any agency notes about competitors, lost pitches, customer feedback or geography

# DEEP mode

Choose 3–5 meaningful competitors. Include indirect alternatives when they compete for the same customer/budget.

## For each competitor, investigate

### Positioning
- homepage headline / category language
- core promise
- buyer/use-case framing
- differentiation claims

### Audience
- primary customer type
- industry/use-case pages
- enterprise vs SMB vs consumer
- investor/franchise/dealer/partner audiences if relevant
- geography emphasis

### Proof
- customer logos
- testimonials
- case studies
- deployment/network/user numbers
- certifications/partners
- quantified outcomes

### Marketing activity
- search/SEO pages and topics
- blog/editorial themes
- social/LinkedIn themes
- founder/executive thought leadership
- PR/news cadence
- campaigns/promotions/community programs
- events/exhibitions/webinars
- product launches as marketing moments

### Sales / conversion motion
- demo / consultation / quote / RFQ
- self-serve purchase/trial
- app/download
- franchise/dealer/distributor inquiry
- partner program
- enterprise sales form
- location/store/network finder
- offers, memberships or public pricing when visible

### Ecosystem motion
- OEM partnerships
- platform/integration partners
- channel partners
- landlords/properties/fuel stations/distributors
- government/industry associations
- interoperability/network alliances

### Geographic motion
- new city/state/country announcements
- localized landing pages
- regional partnerships
- tier-2/3 vs metro focus
- highway/corridor/site-cluster strategies where relevant

# Compare the playbooks

Use a table:

| Competitor | Positioning | Buyer | Acquisition/GTM motion | Proof | Conversion path | Content/SEO | Partnerships/channels | Geography | Agency takeaway |
|---|---|---|---|---|---|---|---|---|---|

Do not score companies on arbitrary 1–10 scales.

# Cross-source insight rule

The point is not to list activities. Connect them.

Example:

> Competitor A has dedicated franchise pages + publishes setup/profit guides + announces each new city/station → it appears to be deliberately recruiting investors/site partners, not merely creating consumer awareness.

For each important pattern:

- Evidence from at least two signals/surfaces where practical
- What competitor appears to be trying to achieve
- Why that matters to the client/prospect
- What the agency should investigate or consider
- What public evidence **does not** establish (for example revenue contribution or actual campaign effectiveness)

Never upgrade “visible activity” into “this works” without evidence.

# Market pattern output

After comparing competitors, identify recurring GTM patterns such as:

- category education as acquisition
- partner-led expansion
- enterprise case-study selling
- franchise recruitment
- local SEO
- founder-led category narrative
- ecosystem/interoperability positioning
- memberships/loyalty
- free trials/demos/diagnostics
- customer-community effects
- channel/distributor recruitment

Distinguish:

- **table stakes** — recurring visible behavior among credible competitors
- **strong precedent** — a competitor packages the motion especially clearly with credible proof
- **white-space hypothesis** — apparently underused opportunity that must survive counterfactual search
- **noise** — activity with no clear connection to acquisition/trust/conversion

Avoid the phrase “winning pattern” unless there is actual evidence of commercial performance.

# WATCH mode

Once a baseline exists, scan for deltas only:

- new positioning/category language
- new audience/use-case pages
- new case studies / logos / proof
- new partner/channel/franchise program
- major content/SEO push
- new geography
- campaign/offer/membership launch
- conversion-flow changes
- visible sales-motion change

A WATCH batch still needs evidence validation before its facts are appended as trusted signals.

Signal example:

```json
{"observed_at":"YYYY-MM-DD","entity":"Competitor","type":"gtm_move","fact":"Launched a dedicated franchise acquisition program and investor guide","source_url":"https://...","confidence":"high","impact":"Adds a structured site/investor acquisition path in the category","recommended_action":"Evaluate whether site/investor partners are economically important to the client before proposing a dedicated funnel"}
```

# Mandatory auditable output — DEEP

Create or use the current research run directory:

```text
clients/<slug>/outputs/<run-id>/
```

Write/update:

```text
draft.md
claims.json
```

The competitor section of `draft.md` should contain:

1. Executive read
2. Competitor playbook table
3. Individual competitor notes
4. Repeated market/geography patterns
5. Strong precedents and their evidence
6. White-space hypotheses
7. Implications for agency pitch or strategy
8. Questions to verify with the client
9. Sources

Add to `claims.json`:

- every material competitor fact
- all numbers/dates/current footprint claims
- customer/partner relationship claims
- every category-level pattern that changes the agency recommendation
- every white-space inference

A pattern is a claim too. It must be challengeable.

# Mandatory auditable output — WATCH

For a watch batch, create a small run directory with:

```text
draft.md
claims.json
```

The draft contains:

- Material GTM deltas
- Why they may matter
- Agency/client discussion implications
- Noise ignored
- Sources

Do not append a material signal to trusted `signals.jsonl` until the evidence-verification stage has accepted the factual delta. When the watch interpretation drives a strategic recommendation, run the counterfactual stage as well.

# Mandatory next step

After DEEP research—and after any WATCH batch that creates a strategic recommendation—run:

> `07-verify-and-challenge`

Use fresh verifier and challenger contexts when supported.

Do not call the competitor research “verified” before that gate passes.

# Scope boundary

This skill may mention public prices, offers or commercial packaging when they are part of GTM/positioning.

It does **not** recommend corporate pricing strategy, margins, working-capital structures, valuation, product engineering, org design or management consulting.

# Quality gate

Before handing the draft to verification:

- Does the analysis explain what competitors are *doing to acquire, convince and convert customers*?
- Does it go beyond feature comparison?
- Are competitor activities tied to plausible GTM intent without claiming unproven effectiveness?
- Are market/geography patterns evidence-backed?
- Are material facts and strategic inferences captured in `claims.json`?
- Does the output give the agency useful strategic direction without pretending to know internal performance?

If not, it is still a Google summary. Keep working before verification.
