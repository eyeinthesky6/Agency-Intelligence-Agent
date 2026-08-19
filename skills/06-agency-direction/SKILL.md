---
name: agency-direction
description: Synthesize company intelligence, competitor GTM playbooks, market/geography patterns and GTM opportunities into an agency-facing strategic direction brief. Use after research to help the agency decide what to pitch, which audiences/channels/themes deserve attention, and what needs client validation before a proposal. The first direction brief is a draft until verify-and-challenge issues a verification receipt.
---

# Agency Direction Brief

## Goal

Produce the core **prep artifact for the agency**.

This is not client-ready copy, not a campaign generator, and not a consulting report. It tells the agency what the research suggests and gives it the raw strategic material to build its own pitch/proposal/content plan.

**Important:** this skill produces an agency-direction **draft**. It becomes a verified final only after `07-verify-and-challenge` completes.

## Read first

Prefer verified upstream material when available:

- `client-context.md`
- latest prospect/company intelligence
- latest competitor GTM intelligence
- verification receipts/reports from upstream research
- latest GTM opportunities
- relevant current signals
- agency service capabilities/constraints when provided

If upstream research has not been verified, preserve that limitation explicitly and include its material claims in this run's claim ledger.

# Output

Use the active run directory:

```text
clients/<slug>/outputs/<run-id>/
```

Write/update:

```text
draft.md
claims.json
```

Do not label the draft final or verified.

## 1. The account story

A concise narrative answering:

- what the company is trying to sell/grow
- who appears to buy it
- how it goes to market now
- what competitors are doing differently
- what market/geography behavior matters
- where the agency may have a role

This should read like a strategist's synthesis, not a list of URLs.

Separate:

- verified public fact
- external company/competitor claim
- agency inference/hypothesis
- internal-data question

## 2. Competitive GTM read

Summarize:

- table-stakes/recurring visible motions
- strongest competitor precedents
- overused/noisy tactics
- white-space **hypotheses**
- any competitor the agency should study especially closely and why

Do not describe a tactic as successful merely because it is visible.

## 3. Audience / customer opportunity map

For each high-priority archetype:

| Audience/customer type | Buying trigger | Problem/job | Current evidence | Competitor approach | Best likely route to reach/influence | Key proof needed |
|---|---|---|---|---|---|---|

Keep to 3–6 archetypes.

## 4. Marketing/GTM directions

Choose the strongest 3–5 directions.

For each:

- **Direction**
- **Audience**
- **Why now**
- **Evidence**
- **Relevant competitor precedent / white-space hypothesis**
- **Possible channels/assets** — examples, not finished campaign plans
- **What success would need to mean** — client must provide actual KPI/target
- **Confidence**
- **Counterfactual risk** — one sentence on what could make this direction wrong

## 5. What the agency could pitch

Provide 2–4 modular pitch themes such as:

- enterprise demand + proof engine
- partner/channel acquisition
- local/geographic growth
- category education/search ownership
- customer advocacy/referral
- ABM for named accounts
- use-case landing pages + case-study selling
- founder/category narrative

For each include what evidence in the research makes it credible.

Do **not** write final sales copy unless asked separately.

## 6. What not to pitch

Call out tempting generic services that are unsupported by evidence.

Examples:

- "more social media"
- "brand awareness"
- "SEO" with no search/use-case hypothesis
- broad paid media with no audience/conversion logic
- expensive content machine without a buying journey
- a competitor tactic whose economic importance is unverified

## 7. Questions before proposal

10 or fewer questions that materially change scope or strategy, such as:

- revenue/customer mix
- priority customer segment
- geographic priority
- channel contribution
- typical sales cycle
- who generates leads today
- current agency/internal ownership
- best proof/case studies
- marketing budget / constraints
- sales capacity / follow-up process

Use questions to close gaps that public research cannot legitimately infer.

## 8. Agency pitch inputs

End with a concise block that the agency can lift into its own planning:

- **One-line account opportunity**
- **Top 3 evidence points**
- **Top 3 audiences**
- **Top 3 GTM directions**
- **Top competitor to benchmark**
- **Biggest unknown**

# Claim ledger requirement

Every material factual foundation and strategic inference in the direction brief must appear in `claims.json`, including:

- company revenue/scale/current priority claims used to rank the pitch
- competitor activity and proof claims
- geography/category patterns
- statements about what is table stakes
- white-space claims
- claims that a channel/motion appears important
- major customer-segment conclusions

For strategic inferences, the ledger should cite the factual premises and classify `kind` as `inference`.

# Mandatory next step

Run:

> `07-verify-and-challenge`

The Verifier must independently reopen/check material evidence. The Challenger must actively search for competing explanations and contrary evidence.

The reconciled output becomes:

```text
final.md
verification.json
counterfactual.md
receipt.json
```

Only `final.md` with an accepted receipt should be treated as the verified agency-prep artifact.

# Quality gate

Before verification:

- Can an agency partner/strategist decide what to explore in a pitch without rereading the whole dossier?
- Are facts and inferences visibly separate?
- Are public-data unknowns turned into discovery questions rather than invented answers?
- Are the strongest 3–5 directions included rather than a service menu?
- Does every major direction have a plausible counterfactual risk?
- Are all material foundations in `claims.json`?

# Scope boundary

No:

- corporate pricing strategy
- finance/working capital consulting
- product engineering roadmap
- org redesign
- M&A/valuation
- finished content/campaign production

Those belong in different workflows/repos.
