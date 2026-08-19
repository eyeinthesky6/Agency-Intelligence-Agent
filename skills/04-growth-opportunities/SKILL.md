---
name: growth-opportunities
description: Turn company research, competitor GTM intelligence, geography/category patterns and available performance context into a small set of evidence-backed marketing and sales GTM directions for an agency to consider. Use after research when the agency asks what should we pitch, what should this company try next, or where is the GTM whitespace.
---

# GTM & Marketing Opportunities

## Goal

Convert research into **agency strategy directions**, not finished campaigns and not management consulting.

The output should help an agency decide what to propose, investigate or prioritize with the client.

## Read first

- `client-context.md`
- latest `prospect-intelligence` output
- latest competitor GTM intelligence
- recent `signals.jsonl`
- campaign/performance data if supplied
- agency's own service capabilities if known

## Opportunity sources

Look for evidence across:

1. **Positioning gap** — company story is generic/complex while competitors own clearer buyer language.
2. **Audience gap** — important buyer/customer archetype lacks a dedicated message/funnel.
3. **Proof gap** — company has strong deployments/customers/results but does not package them into trust assets.
4. **Channel gap** — competitors use partnerships, distributors, franchise, local search, events, enterprise case studies, referrals or ecosystem channels more systematically.
5. **Geography gap** — regional/tier/city opportunity is visible but GTM remains national/generic.
6. **Conversion gap** — traffic/interest has weak next-step paths: generic contact form instead of demo/RFQ/partner/franchise/use-case conversion.
7. **Customer expansion gap** — existing client/customer base could support cross-sell, referral, advocacy or account expansion if evidence supports it.
8. **Category education gap** — buyers need education before purchase and competitors are winning through guides/tools/case studies.
9. **Sales-enablement gap** — buyers/partners need clearer comparisons, use-case proof, ROI/TCO context, implementation proof or objection handling.

## Ranking

Return at most **5** directions, with a recommended top 3.

For each consider:

- evidence strength
- fit with visible company goals/GTM
- competitive urgency
- likely audience relevance
- agency ability to influence it
- effort to validate/test

Do not claim ROI or conversion uplift without client data.

## Output

Create:

`clients/<slug>/outputs/gtm-opportunities-YYYY-MM-DD.md`

For each direction:

### [Direction]

- **Observed evidence:** company + competitor/category signals
- **GTM hypothesis:** what may be missing or underused
- **Who it is for:** customer/buyer/partner archetype
- **What the agency could propose:** strategic direction only
- **Why it may work:** evidence/category pattern
- **How to validate:** smallest research/test/client question
- **Confidence:** high / medium / low

Examples of appropriate directions:

- create a dedicated enterprise use-case proof engine
- build partner/franchise acquisition funnels
- strengthen local/tier-2 search and city landing pages
- package customer deployments into case-study selling
- establish founder/executive category narrative
- build account-based marketing around 30 named enterprise buyers
- create channel/distributor recruitment and enablement
- use calculators/tools/guides as lead qualification
- build lifecycle/referral motion for existing customers

Inappropriate directions for this repo:

- change manufacturing process
- restructure pricing/margins
- working-capital changes
- acquisition/M&A strategy
- org redesign
- product engineering roadmap
- detailed corporate finance recommendations

## Recommended sequence

End with:

1. **Pitch now** — strongest 1–3 directions.
2. **Ask first** — important hypotheses needing client data.
3. **Keep in reserve** — promising ideas not yet evidenced enough.

## Quality gate

Reject any recommendation that:

- could be pasted into ten unrelated company reports
- is based on only "they should post more"
- confuses business consulting with marketing/GTM
- ignores how competitors actually acquire/convert customers
- assumes internal performance metrics that are not known

## Stop condition

The agency needs a few defensible directions, not an idea dump.
