---
name: verify-and-challenge
description: Independently verify a major research draft, challenge its core thesis with contrary evidence, and reconcile it into a final agency-prep artifact. Use after prospect intelligence, DEEP competitor GTM research, or any agency direction based on fresh external research. This is a mandatory evidence gate before calling a major research output verified.
---

# Verify and Challenge

## Goal

Treat the first research output as a **hypothesis to audit**, not a completed answer.

This skill runs three logically separate stages:

1. **Evidence Verifier** — checks factual support.
2. **Counterfactual Challenger** — tries to disprove the story.
3. **Reconciler** — produces the most defensible final version.

When the harness supports subagents or fresh sessions, use them. Do not ask the Producer to grade itself inside the same context.

# Inputs

Required:

- producer draft (`draft.md` or equivalent)
- all source URLs used by the Producer
- claim ledger if the Producer created one
- company/client context

Optional:

- prior verified intelligence
- internal client documents
- previous verification receipts

# Stage B — Evidence Verifier

## Verifier instruction

Approach the draft skeptically and independently.

Do not assume:

- the Producer opened the right company/entity
- the cited source actually says what the draft claims
- a current number is still current
- a marketing claim is an operational fact
- a search snippet accurately represents the source
- two publications are independent if they repeat the same press release

## Step 1 — extract the claims independently

Read the draft and build/rebuild the material claim list.

Compare it with the Producer's `claims.json` if present. Add any omitted material claim.

Material claims include:

- current company facts
- numbers/percentages/currencies
- dates/periods
- customer/partner relationships
- competitor/channel/geography statements
- public offers/pricing used in the analysis
- “first/largest/leading/fastest” comparisons
- cross-source GTM patterns that drive recommendations

## Step 2 — verify exact support

For every material factual claim:

1. Open the source rather than trusting search-result snippets.
2. Confirm the source refers to the correct company/entity/time period.
3. Confirm the exact wording/value/unit/date.
4. Check whether the claim is current enough for the draft's wording.
5. Prefer primary/current sources where available.
6. For critical claims without a primary source, seek independent corroboration.
7. Record conflicts instead of choosing the more convenient source silently.

## Verification statuses

Use exactly:

- `VERIFIED_PRIMARY`
- `VERIFIED_CORROBORATED`
- `PARTIAL`
- `STALE`
- `UNSUPPORTED`
- `CONTRADICTED`

## Verification output

Write `verification.json`:

```json
{
  "run_id": "...",
  "claims": [
    {
      "id": "C-001",
      "claim": "...",
      "importance": "critical",
      "status": "VERIFIED_PRIMARY",
      "checked_sources": ["https://..."],
      "evidence_note": "What the source actually establishes",
      "problem": null,
      "required_fix": null
    }
  ],
  "missing_claims_added": [],
  "source_conflicts": [],
  "broken_or_inaccessible_links": [],
  "verifier_summary": "..."
}
```

# Repair cycle

If material factual claims are `PARTIAL`, `STALE`, `UNSUPPORTED` or `CONTRADICTED`:

- return only those failures to a fresh Producer/research run;
- allow one repair attempt by default;
- reverify the repaired claims.

Do **not** endlessly search for a source that agrees with the original story.

# Stage C — Counterfactual Challenger

Run after factual verification so the Challenger attacks interpretation rather than wasting time on obvious citation errors.

## Challenger instruction

Your job is to construct the strongest plausible case that the Producer's main GTM conclusions are wrong, incomplete or non-transferable.

Do not be contrarian for entertainment. Search for real disconfirming evidence.

For each major thesis:

### 1. State the thesis fairly

Example:

> Partner acquisition is a major category GTM motion in Indian EV charging.

### 2. Build the strongest alternative explanation

Example:

> Partner pages may exist because infrastructure companies need site hosts, but those programs may produce little revenue and may not be the prospect's strategic priority.

### 3. Define distinguishing evidence

Examples:

- actual priority stated by management
- frequency/recency of partner launches
- evidence of competing acquisition channels
- customer/revenue mix
- geography differences
- whether the competitor continues investing in the program

### 4. Search for contrary evidence

Use fresh queries/sources. Do not restrict yourself to the Producer's source list.

### 5. Grade the challenge

Use exactly:

- `OVERTURNS`
- `WEAKENS`
- `UNCHANGED`
- `STRENGTHENS`
- `UNRESOLVED`

## Challenger checklist

Test for:

- omitted strong competitors
- different buyer segments disguised as comparable competitors
- selection/survivorship bias
- visible marketing activity with no evidence it works
- geography/regulatory differences
- stale category assumptions
- base-rate alternatives (referrals, founders, dealers, tenders, existing relationships)
- channel conflict
- false whitespace (something looks absent because it is private/offline)
- correlation presented as causation
- recommendations that exceed the evidence

## Counterfactual output

Write `counterfactual.md`:

```markdown
# Counterfactual Challenge

## Thesis 1
- Producer thesis:
- Strongest alternative:
- Contrary evidence searched:
- Evidence found:
- Verdict: WEAKENS
- What changes in the agency recommendation:
- What client question resolves the remaining uncertainty:
```

# Stage D — Reconciler

The Reconciler receives:

- original draft
- verification report
- repaired claims if any
- counterfactual report

## Reconciliation rules

1. Remove factual claims that remain `UNSUPPORTED` or `CONTRADICTED`.
2. Reword `PARTIAL`/`STALE` claims narrowly enough to match evidence, or remove them.
3. Never convert a competitor/company marketing claim into an operational fact.
4. Keep verified source links attached to material claims.
5. Label inference as inference/hypothesis.
6. Lower recommendation confidence when counterfactual evidence weakens the thesis.
7. Preserve important contradictions/caveats.
8. Turn public-data unknowns into discovery questions.
9. Do not add fresh material facts during reconciliation. If a new fact is necessary, return it to verification.

# Terminal status

End with one:

## `VERIFIED`
All critical facts verified; main thesis survived counterfactual search; no material unresolved contradiction.

## `VERIFIED_WITH_CAVEATS`
Critical facts verified; supporting interpretations contain explicitly stated uncertainty that does not overturn the main agency direction.

## `REVIEW_REQUIRED`
One or more critical strategic interpretations cannot be resolved from public evidence. The agency/client must confirm them before proposal.

## `FAILED_EVIDENCE_GATE`
The factual foundation of a major recommendation remains unsupported/contradicted.

# Final outputs

Write:

```text
<run-dir>/final.md
<run-dir>/receipt.json
```

The final document should start with a small verification box:

```markdown
> Verification status: VERIFIED_WITH_CAVEATS
> Critical claims verified: 7/7
> Supporting claims unresolved: 2
> Counterfactual challenges tested: 4
> Main recommendation weakened/removed: 1
```

Do not burden the agency reader with every audit detail in the main report. Keep `verification.json` and `counterfactual.md` available as the audit trail.

# Receipt

`receipt.json` should record:

- run ID
- status
- producer/verifier/challenger identifiers if available
- count of claim statuses
- count of counterfactual verdicts
- unresolved discovery questions
- repair attempts
- completion timestamp

# Cost / stop discipline

Default:

- one Producer run
- one Verifier run
- one repair run only if needed
- one Challenger run
- one Reconciler run

The Verifier should focus on material claims, not every adjective.

The Challenger should test the 3–5 conclusions that actually change what the agency might pitch.

More model calls are not automatically more reliable. **External evidence + clear gates + stopping rules are the reliability mechanism.**
