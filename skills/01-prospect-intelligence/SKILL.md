---
name: prospect-intelligence
description: Build a detailed company and go-to-market intelligence dossier for an agency before a pitch or strategy discussion. Research what the company sells, who buys it, how it appears to acquire customers, how it positions itself, what competitors are doing in market, which geographies and customer segments matter, and where an agency could credibly improve GTM or marketing. Major runs produce an auditable draft and claim ledger that must pass verify-and-challenge before being treated as final.
---

# Prospect Intelligence — Agency Prep

## Goal

Give an agency enough **commercial and marketing context** to walk into a prospect conversation sounding as if it has studied the account, category and competitors properly.

This is not a generic company profile and not management consulting.

The skill should answer:

1. What does this company really sell and to whom?
2. How does it appear to go to market today?
3. How do its main competitors market and sell differently?
4. What appears to work in this category/geography?
5. Which customer segments/accounts could the company plausibly pursue?
6. What marketing/GTM directions are worth discussing with the prospect?

## Read first

If available:

- `clients/<prospect>/client-context.md`
- prior proposal / agency notes
- uploaded pitch decks, brochures, reports, sales collateral
- website and social URLs supplied by the user

Do not require internal data to start. Public evidence is enough for a useful first-pass agency brief.

# Research map

Do not browse randomly. Work through the following layers.

## 1. Company

Capture:

- products/services and important product lines
- business model at a practical level
- geography / city / state / country presence
- customer types and named customers when public
- partnerships / channels / distributors / franchise models
- current growth/expansion signals
- public pricing/offers only where visible and relevant
- current website positioning and primary CTAs
- proof points: customers, deployments, results, certifications, case studies

Financial facts are useful only as context for company scale. Do not perform valuation, working-capital or corporate-finance consulting.

## 2. Current visible GTM

Investigate how the company currently appears to create demand and trust:

- website structure and conversion paths
- SEO/search-oriented pages
- landing pages by use case / industry / geography
- customer case studies
- partner announcements
- events, exhibitions and webinars
- PR / founder-led narrative
- LinkedIn/social themes and cadence when visible
- dealer/distributor/franchise recruitment
- referral/community programs
- product demos / free trials / consultations / RFQ paths
- sales contact flow
- marketplace/app/network effects where relevant

Do not equate posting frequently with having a good GTM strategy.

## 3. Competitor marketing playbooks

Choose 3–5 relevant competitors or substitutes.

For each, inspect:

- headline positioning
- target buyers/use cases
- geography emphasis
- proof and customer logos
- acquisition/conversion offers
- use-case/industry landing pages
- case studies
- partnerships and ecosystem motion
- SEO/content topics
- events / communities / channel programs
- franchise/dealer/distributor motion where relevant
- public pricing/promotions/membership only where useful
- visible sales motion: enterprise demo, self-serve, partner-led, retail, field sales, app, franchise, etc.

The output should explain **what each competitor is trying to make the market believe and how it seems to acquire customers**.

## 4. Geography / category pattern

Research what appears to matter in the target geography.

Examples:

- metro vs tier-2/3 growth
- fragmented local channels vs national brands
- government/enterprise procurement
- channel partner importance
- customer trust signals
- regional language/local search
- trade events / associations
- ecosystem partnerships
- offline + digital combinations

Only make a geography claim when evidence supports it.

## 5. Potential customer universe

Do not create a giant scraped lead list.

Identify 3–6 **customer archetypes** the company could plausibly pursue next based on:

- who already buys from them
- who buys from competitors
- adjacent use cases
- geography
- partner ecosystems
- public category adoption

For each archetype give:

- who they are
- buying trigger
- problem/use case
- likely decision maker
- why this company might fit
- how an agency could reach/influence them
- 3–5 illustrative target accounts only if credible public examples exist

## 6. Cross-source synthesis

A useful insight should normally connect more than one observation.

Good:

> Competitors are building dedicated franchise-investor landing pages + publishing economics/how-to content + using local expansion announcements → the category is not only selling charging to drivers; it is also recruiting capital/site partners. The prospect may therefore need to investigate whether this is a priority audience.

Bad:

> Competitor X has a franchise page.

For important insights show:

- **Observed evidence**
- **What it suggests**
- **Agency implication**
- **What should be verified with the prospect**

# Mandatory auditable output

A new research run is **not final**.

Create a run directory:

```text
clients/<prospect>/outputs/<YYYY-MM-DD-run-slug>/
```

Write:

```text
draft.md
claims.json
```

## `draft.md`

Use this structure:

### 1. Agency executive brief
5–8 bullets maximum.

### 2. Company GTM snapshot
- company / category / scale
- products/services
- geography
- likely buyers
- visible sales motion
- current positioning
- proof points
- visible CTAs / conversion paths

### 3. Current marketing & sales footprint
Explain what the company is actually doing today across website, content, partnerships, social/PR, events, channels and conversion.

### 4. Competitor GTM comparison

| Competitor | Positioning | Core buyer/use case | Marketing motion | Proof/assets | Conversion path | Geography/channel angle | What stands out |
|---|---|---|---|---|---|---|---|

### 5. What appears to work in this market/geography
3–6 evidence-backed patterns.

### 6. Customer opportunity map
3–6 target customer archetypes with triggers and outreach/marketing routes.

### 7. White spaces / agency hypotheses
Maximum 5.

For each:
- Evidence
- Hypothesis
- Marketing/GTM direction
- Why it could matter
- Confidence
- What to ask the prospect

These are directions for the agency, **not finished campaigns or content**.

### 8. Suggested pitch themes
3–5 themes the agency could choose from when building its own pitch.

Do not draft the final proposal unless asked separately.

### 9. Discovery questions
Questions that validate the most important unknowns: channel contribution, target segments, sales cycle, lead quality, partner strategy, geographic priorities, marketing ownership and constraints.

### 10. Sources
Keep source URLs for material claims.

## `claims.json`

Add every material factual claim and every strategic inference that materially changes an agency recommendation.

Required fields:

```json
{
  "id": "C-001",
  "claim": "Exact claim",
  "kind": "fact | number | date | comparison | inference",
  "importance": "critical | supporting",
  "source_urls": ["https://..."],
  "as_of": "YYYY-MM-DD",
  "producer_confidence": "high | medium | low"
}
```

Do not hide difficult claims by omitting them from the ledger. The Verifier will independently extract claims from the draft too.

# Mandatory next step

After producing the draft:

> Run `07-verify-and-challenge` on this run directory using fresh verifier and counterfactual contexts where supported.

Do not present `draft.md` as a verified final dossier.

# Research depth

Default:

- company: 5–10 useful sources/pages
- competitors: 3–5 competitors, 3–6 useful surfaces each
- category/geography: enough evidence to establish recurring patterns

Stop when further browsing repeats the same GTM story. Verification and counterfactual search happen in the next skill.

# Quality gate

Before handing the draft to verification:

- Does the brief describe **how the company appears to sell**, not just what it sells?
- Does it compare competitor **marketing/GTM activity**, not just features?
- Are at least 3 insights cross-source syntheses?
- Does it identify customer archetypes rather than a random lead list?
- Does it say what appears to work in the relevant geography/category?
- Are agency recommendations marketing/GTM scoped rather than management consulting?
- Are material claims present in `claims.json`?
- Would an agency strategist find something useful beyond the first page of Google results?

If not, research/synthesize further before verification.
