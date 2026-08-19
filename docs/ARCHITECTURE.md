# Architecture — v0.3

## Design goal

Agency Intelligence Agent is a **portable, verification-first research and GTM intelligence layer for agencies**.

The host agent (ChatGPT, Codex, Claude, Hermes, Kimi, Cursor, etc.) supplies reasoning and available web/file tools. This repository supplies the agency research method, evidence contracts, bounded validation loop, memory format and artifacts.

It is not a SaaS application and not a management-consulting suite.

## System

```text
Client / Prospect files + URLs
            ↓
     client-context.md
            ↓
┌────────────────────────────┐
│ A. PRODUCER                │
│ company + GTM + competitors│
└─────────────┬──────────────┘
              ↓
      draft.md + claims.json
              ↓
      ┌───────┴─────────┐
      ↓                 ↓
┌───────────────┐  ┌──────────────────┐
│ B. EVIDENCE   │  │ C. COUNTERFACTUAL│
│ VERIFIER      │  │ CHALLENGER       │
│ fresh sources │  │ contrary evidence│
└───────┬───────┘  └─────────┬────────┘
        │                    │
        └──────────┬─────────┘
                   ↓
          ┌─────────────────┐
          │ D. RECONCILER   │
          └────────┬────────┘
                   ↓
 final.md + verification.json
 + counterfactual.md + receipt.json
                   ↓
        agency pitch / strategy prep
```

The agency remains the decision-maker.

## Canonical client workspace

```text
clients/<slug>/
├── client-context.md
├── signals.jsonl
├── actions.json
├── source-notes/
└── outputs/
    └── <run-id>/
        ├── draft.md
        ├── claims.json
        ├── verification.json
        ├── counterfactual.md
        ├── final.md
        └── receipt.json
```

### `client-context.md`

Durable human-readable account context:

- company/business
- products/services
- target audiences/customer types
- geography
- positioning
- proof
- competitors
- visible/current GTM
- agency scope/goals when known
- constraints
- open questions

### `signals.jsonl`

Append-only **verified** GTM event memory.

A material external signal should not become trusted memory just because a watcher found it.

```text
watch draft
    ↓
evidence verification
    ↓
accepted factual delta
    ↓
signals.jsonl
```

Example:

```json
{
  "observed_at": "YYYY-MM-DD",
  "entity": "Competitor",
  "type": "gtm_move",
  "fact": "Launched a dedicated distributor program and city-specific recruitment pages",
  "source_url": "https://...",
  "confidence": "high",
  "impact": "May indicate a structured channel-acquisition motion",
  "recommended_action": "Check whether channel recruitment is strategically important to the client before proposing a dedicated funnel"
}
```

### `actions.json`

Optional agency action register for proposed/approved GTM work.

Allowed status values:

- `proposed`
- `approved`
- `in_progress`
- `done`
- `rejected`

# Stage A — Producer

The Producer optimizes for useful discovery and synthesis.

It researches:

- company GTM
- competitor marketing/sales playbooks
- category/geography patterns
- customer archetypes
- plausible agency directions

It may form hypotheses, but it must expose their factual foundations.

Required outputs:

```text
draft.md
claims.json
```

A first draft is never called verified.

## Claim contract

Minimum shape:

```json
{
  "id": "C-001",
  "claim": "Exact material claim to check",
  "kind": "fact",
  "importance": "critical",
  "source_urls": ["https://..."],
  "as_of": "YYYY-MM-DD",
  "producer_confidence": "high"
}
```

Kinds:

- `fact`
- `number`
- `date`
- `comparison`
- `inference`

A strategic inference belongs in the ledger when it materially changes what the agency would pitch.

The Verifier also scans the draft independently because the Producer may accidentally omit claims from the ledger.

# Stage B — Evidence Verifier

The Verifier should use a **fresh context/session** when supported.

It independently checks material claims by reopening external evidence.

For every material factual claim it asks:

- Is this the correct company/entity?
- Does the linked page actually support the wording?
- Is the number/unit/currency exact?
- Is the date/time period correct?
- Is it current enough for the wording?
- Is a company marketing claim being presented as independent fact?
- Does a critical claim need independent corroboration?
- Do credible sources conflict?

Statuses:

```text
VERIFIED_PRIMARY
VERIFIED_CORROBORATED
PARTIAL
STALE
UNSUPPORTED
CONTRADICTED
```

Output:

```text
verification.json
```

The Verifier does not decide whether the story is strategically clever. Its job is narrower:

> Does the evidence support the factual foundation?

# Repair cycle

Default maximum: **one** repair.

```text
Verifier rejects material claim
       ↓
failed claims only → fresh repair research
       ↓
Verifier rechecks
       ↓
pass OR stop/escalate
```

Retry-until-pass is forbidden.

If evidence does not close after the repair budget, the run ends with `REVIEW_REQUIRED` or `FAILED_EVIDENCE_GATE`.

# Stage C — Counterfactual Challenger

After factual verification, the Challenger tests the **interpretation**.

It should also use fresh context when supported and search beyond the Producer's sources.

For the 3–5 theses that actually change the agency recommendation:

1. state the Producer thesis fairly;
2. construct the strongest plausible alternative explanation;
3. identify evidence that would distinguish the two;
4. actively search for disconfirming evidence;
5. grade the result;
6. explain what changes in the agency recommendation.

Verdicts:

```text
OVERTURNS
WEAKENS
UNCHANGED
STRENGTHENS
UNRESOLVED
```

Typical challenges:

- visible marketing exists but may not work commercially;
- competitors may target different buyers;
- apparent whitespace may already exist;
- geography may make a tactic non-transferable;
- the company's real revenue engine may differ from its public website emphasis;
- referrals, founders, dealers, tenders or partnerships may dominate instead of inbound;
- the Producer may have omitted a strong competitor or substitute;
- selection/survivorship bias may make public success stories misleading.

Output:

```text
counterfactual.md
```

A counterfactual that overturns a recommendation is a **successful validation run**.

# Stage D — Reconciler

The Reconciler receives:

- Producer draft
- claim ledger
- verification report
- repaired evidence if any
- counterfactual report

It may:

- remove unsupported claims;
- narrow wording to match evidence;
- lower confidence;
- preserve conflicting evidence;
- reorder agency priorities;
- convert unresolved public-data questions into client discovery questions.

It may **not introduce a new material fact** without returning that fact to the Verifier.

Required outputs:

```text
final.md
receipt.json
```

# Evidence gate / terminal states

A run ends with exactly one status:

## `VERIFIED`

All critical factual claims verified; main theses survived counterfactual search; no material contradiction remains unresolved.

## `VERIFIED_WITH_CAVEATS`

Critical facts verified; uncertainty remains in supporting interpretation but does not invalidate the main agency direction.

## `REVIEW_REQUIRED`

One or more strategically critical interpretations cannot be resolved publicly and require agency/client confirmation before proposal.

## `FAILED_EVIDENCE_GATE`

A critical factual foundation remains unsupported or contradicted.

A model writing the word “verified” has no authority. **`receipt.json` is the run state.**

# Evidence receipt

The receipt records:

- terminal status
- run ID
- producer/verifier/challenger/reconciler identifiers when available
- claim counts by verification status
- counterfactual counts by verdict
- repair attempts
- unresolved discovery questions
- material changes from the original draft
- completion time

This makes model/harness comparisons reviewable rather than subjective.

# Independence

Independence is mainly about **information flow**, not model branding.

Strong independence:

- fresh context
- reopen original sources
- independently extract claims
- search outside the Producer's source set
- optimize for a different objective
- actively seek disconfirmation

Using a different model/provider may further reduce correlated errors and is useful for higher-value runs, but is optional.

GPT → Claude with the same wrong summary is not strong verification.

# Default loop budget

| Stage | Default |
|---|---:|
| Producer | 1 |
| Evidence Verifier | 1 |
| Repair | 0–1 |
| Counterfactual Challenger | 1 |
| Reconciler | 1 |

The Verifier audits **material** facts, not every adjective.

The Challenger tests only conclusions that could materially change agency strategy.

More calls without stronger evidence are wasted cost.

# Skill execution contract

Every major research workflow follows:

### 1. Load context
Read available client/company material before searching.

### 2. Define the agency question
Examples:

- How does this company appear to acquire customers?
- How are competitors going to market?
- What recurring GTM motions appear in this geography/category?
- Which customer archetypes deserve attention?
- What should an agency consider pitching?

### 3. Plan research surfaces
Choose relevant sources: website, use-case pages, case studies, partner pages, social/PR, events, competitor surfaces, geography/category evidence.

### 4. Gather evidence
Retain URLs/dates and distinguish marketing claims from independently established facts.

### 5. Normalize
Capture:

- audience
- positioning
- proof
- acquisition motion
- conversion path
- channel/partner motion
- geography
- content/search activity

### 6. Cross-source synthesis
Connect multiple observations into agency-relevant hypotheses.

### 7. Produce claim ledger
Expose material facts and inferences.

### 8. Verify independently
Reopen evidence and issue verification statuses.

### 9. Challenge counterfactually
Search for the strongest competing story.

### 10. Reconcile and stop
Publish only the evidence-supported version and terminal receipt.

# Research depth defaults

| Task | Default |
|---|---:|
| Main competitors | 3–5 |
| Useful company pages/sources | 5–10 |
| Competitor surfaces | 3–6 each |
| Customer archetypes | 3–6 |
| Agency GTM directions | 3–5 |
| Counterfactual theses | 3–5 |
| Repair attempts | ≤1 |
| Discovery questions | ≤10 |
| Meeting brief | ~1 page |

These are stopping guides, not evidence quotas.

# Tool interfaces

Skills may conceptually request:

- `search_web(query)`
- `fetch_url(url)`
- `read_client_files(path)`
- `search_drive(query)`
- `write_output(path, content)`

The repository does not implement these services. The host maps them to available tools.

# Failure modes

## Search-summary syndrome

**Failure:** one source becomes one bullet and no synthesis occurs.

**Fix:** require cross-source GTM patterns, claim ledger and agency implication.

## Feature-table syndrome

**Failure:** competitor comparison lists only product features.

**Fix:** compare positioning, audience, proof, acquisition, conversion, partners and geography.

## Self-certification

**Failure:** Producer says “sources verified.”

**Fix:** fresh Evidence Verifier must reopen the evidence.

## LLM voting

**Failure:** three agents agree without new evidence.

**Fix:** agreement is not proof; require source-grounded verification and disconfirming search.

## Retry-until-pass

**Failure:** agent keeps searching until it finds support.

**Fix:** one repair cycle; then honest terminal state.

## Generic-agency syndrome

**Failure:** recommendations are “SEO, social, ads, content.”

**Fix:** require who/why/job/evidence/precedent and counterfactual risk.

## Consulting drift

**Failure:** agent recommends corporate pricing, finance, product engineering or org redesign.

**Fix:** stop and mark out of scope.

# Future architecture triggers

Add infrastructure only after repeated user pain:

- **Database:** files become painful across many clients/runs.
- **Scheduler:** agencies want recurring competitor watches.
- **Browser service:** host tools repeatedly miss necessary public surfaces.
- **Drive adapter:** manual client-file movement becomes a blocker.
- **Dashboard:** agencies need cross-client/run visibility.
- **Cross-model verifier routing:** user value justifies deliberate model/provider diversity.
- **CRM/ad/content connectors:** only after agencies explicitly want approved directions pushed into execution.

Until then: **skills + files + host tools + evidence receipts**.
