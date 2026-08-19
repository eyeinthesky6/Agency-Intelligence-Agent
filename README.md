# Agency Intelligence Agent

A lightweight, skill-based **research, verification and GTM intelligence layer for marketing and sales agencies**.

It helps an agency understand a company, study its competitors' marketing and sales motions, identify category/geography patterns, map likely customer segments, and decide what strategic directions are worth pitching.

**The rule:** research deeply; verify independently; challenge the story; recommend narrowly; leave execution to the agency.

This repo intentionally stays portable: Agent Skills + plain-text memory + simple artifacts. No database, vector store, multi-agent framework, custom crawler or SaaS backend is required for v0.

## Who this is for

- marketing agencies
- GTM agencies
- B2B demand-generation agencies
- sales/ABM agencies
- growth agencies
- agency founders and strategists preparing pitches
- account leads preparing client strategy/reviews

The company itself can use the skills too, but the primary product is **agency prep and intelligence**.

## What it does

1. **Client Onboard** — capture durable client/prospect context once.
2. **Prospect Intelligence** — research the company, visible GTM, buyer groups, geography and competitors.
3. **Competitor GTM Intelligence** — study how 3–5 competitors position, acquire trust, use channels/partners/content and convert interest.
4. **Meeting Prep** — turn existing intelligence into a short pre-call brief.
5. **GTM Opportunities** — identify evidence-backed marketing/sales directions rather than generic services.
6. **Client Review** — package what changed, what the agency learned and what should be discussed next.
7. **Agency Direction Brief** — synthesize the research into pitch themes, target audiences, competitor precedents, white spaces and discovery questions.
8. **Verify & Challenge** — independently verify material claims, run a counterfactual/disconfirming-evidence pass, and reconcile the result before it is called verified.

## What this repo is NOT

This is not McKinsey-in-a-box.

It does not own:

- corporate pricing strategy
- margins / working capital / finance consulting
- product engineering
- manufacturing/process consulting
- org design
- M&A / valuation
- finished content generation by default
- autonomous ad or outbound execution

Those are separate products/workflows.

# Core workflow

```text
COMPANY CONTEXT
      ↓
COMPANY GTM RESEARCH
      ↓
COMPETITOR MARKETING / SALES PLAYBOOKS
      ↓
CATEGORY + GEOGRAPHY PATTERNS
      ↓
CUSTOMER / AUDIENCE OPPORTUNITY MAP
      ↓
AGENCY GTM DIRECTIONS
      ↓
INDEPENDENT EVIDENCE VERIFICATION
      ↓
COUNTERFACTUAL / DISCONFIRMING-EVIDENCE RUN
      ↓
RECONCILIATION
      ↓
AGENCY PREP ARTIFACT + EVIDENCE RECEIPT
```

A first run is a **draft hypothesis**, not a trusted final answer.

## The verification loop

Every major fresh-research deliverable uses four logically separate stages:

### A. Producer

Researches and synthesizes the strongest useful agency thesis.

Outputs:

- draft
- source list
- claim ledger

### B. Evidence Verifier

Runs with fresh context when possible and checks the Producer literally:

- does the URL open?
- is it the correct company/entity?
- does the source actually support the exact claim?
- is the number/unit/date correct?
- is the information current?
- is a competitor's marketing claim being mistaken for fact?
- can a critical claim be independently corroborated?

Statuses:

- `VERIFIED_PRIMARY`
- `VERIFIED_CORROBORATED`
- `PARTIAL`
- `STALE`
- `UNSUPPORTED`
- `CONTRADICTED`

### C. Counterfactual Challenger

Assumes the main story may be wrong and actively searches for evidence that would overturn it.

It tests questions such as:

- What if this visible tactic is not actually working?
- What if the competitor serves a different buyer?
- What if the apparent whitespace already exists?
- What if the company's real revenue engine is somewhere else?
- What strong competitor/channel did the first run miss?
- What would make the proposed agency direction a waste of money?

Verdicts:

- `OVERTURNS`
- `WEAKENS`
- `UNCHANGED`
- `STRENGTHENS`
- `UNRESOLVED`

### D. Reconciler

Produces the final report.

It may:

- delete unsupported claims
- narrow claims to match evidence
- lower confidence
- preserve contradiction
- turn unknowns into discovery questions

It may **not introduce a new material fact without sending it back through verification**.

## Terminal states

A major run ends as exactly one of:

- `VERIFIED`
- `VERIFIED_WITH_CAVEATS`
- `REVIEW_REQUIRED`
- `FAILED_EVIDENCE_GATE`

The agent is not allowed to call its own first draft verified.

## One repair cycle, not infinite loops

Default budget:

```text
1 Producer
1 Verifier
0–1 repair pass
1 Challenger
1 Reconciler
```

If a critical claim still cannot be supported after the repair pass, the run stops with `REVIEW_REQUIRED` or `FAILED_EVIDENCE_GATE`.

The goal is **better evidence**, not more model calls.

# What counts as intelligence

A search result is evidence, not the answer.

**Weak:**

> Statiq has a franchise page.

**Useful:**

> Statiq has a dedicated FOCO/franchise funnel, ChargeZone also markets franchise ownership, Bolt.Earth recruits distributors and Kazam has partner/dealer intake. This verifies that partner/site/channel acquisition is a recurring visible category motion. However public evidence does not prove those programs are economically important for Kazam, so an agency should validate partner contribution before pitching a partner-acquisition program.

That is the standard: connect multiple public observations, verify the facts, then keep the inference no stronger than the evidence.

# What gets researched

## Company

- what it sells
- who appears to buy it
- geography
- visible sales motion
- website positioning / CTAs
- product/use-case pages
- customer proof / case studies
- partnerships and channels
- public offers/pricing where relevant to GTM
- current growth/expansion signals

## Competitors

- positioning
- target buyers/use cases
- SEO/content footprint
- social/founder/PR themes
- customer proof
- case studies
- partnerships/ecosystem
- events/community
- dealer/distributor/franchise motion
- geography/local expansion
- conversion paths
- public offers/memberships/pricing where visible

## Market / geography

- what repeated acquisition motions appear to work or at least recur
- metro vs tier-2/3 dynamics
- channel/partner importance
- local search / city pages
- category education needs
- trade/event/community importance
- public-sector/enterprise procurement where relevant

## Customer opportunity

First identify customer archetypes, not giant lead lists:

- who they are
- buying trigger
- problem/job
- likely decision maker
- why the company may fit
- route to influence/reach them

Illustrative target accounts come only after the archetype is credible.

# Repository layout

```text
Agency-Intelligence-Agent/
├── AGENTS.md
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   └── SUCCESSFUL_PATTERNS.md
├── skills/
│   ├── 00-client-onboard/
│   ├── 01-prospect-intelligence/
│   ├── 02-competitor-watch/
│   ├── 03-meeting-prep/
│   ├── 04-growth-opportunities/
│   ├── 05-client-review/
│   ├── 06-agency-direction/
│   └── 07-verify-and-challenge/
├── templates/
│   ├── claims.example.json
│   ├── verification.example.json
│   ├── counterfactual.example.md
│   └── receipt.example.json
├── scripts/
└── examples/
    └── kazam-agency-prep/
```

# Quick start

## 1. Research the company

> Run `01-prospect-intelligence` for Kazam. Build a detailed agency-prep dossier. Study the company, visible GTM, 3–5 competitors, category/geography patterns and likely customer archetypes. Do not give me a generic company profile.

## 2. Go deeper on competitors

> Run `02-competitor-watch` in DEEP mode. Compare how competitors position, generate attention, build trust, recruit partners/channels and convert buyers. Tell me what appears table stakes, what looks effective and where there is whitespace.

## 3. Decide what the agency should consider pitching

> Run `04-growth-opportunities`. Give me the strongest evidence-backed GTM/marketing directions. Do not write campaigns yet.

## 4. Compress it for the agency partner

> Run `06-agency-direction`. Give me the account story, customer map, competitor precedents, pitch themes, what not to pitch and the questions we must ask before proposal.

## 5. Verify before trusting it

> Run `07-verify-and-challenge` on the complete Kazam agency-prep output. Use a fresh verifier and a fresh counterfactual challenger if the harness supports them. Reopen every material source, independently verify critical numbers/dates/current claims, search for contrary evidence, reconcile the report, and return the evidence receipt. Do not call it verified if the evidence gate fails.

# Example benchmark — Kazam Energy

The benchmark researches Kazam against Statiq, Bolt.Earth and ChargeZone.

The original research surfaced useful patterns, but the verification loop **materially changed the result**:

- verified: partner/franchise/distributor/dealer paths are visible across the category
- weakened: public presence alone does not prove partner programs are major revenue channels
- overturned: “data-led category authority is a blank whitespace” — Kazam already runs a research motion
- overturned/reordered: enterprise GTM was over-weighted; current public management interviews say tier-2/3 three-wheeler/home charging is the major revenue engine
- retained with caveat: enterprise proof/case-study architecture remains a credible opportunity

See the full audit trail:

```text
examples/kazam-agency-prep/outputs/2026-08-19-verified/
├── claims.json
├── verification.json
├── counterfactual.md
├── final.md
└── receipt.json
```

That is the intended behavior: verification is allowed to **change the strategy**, not just check citation formatting.

# Client memory

```text
clients/<client>/client-context.md
clients/<client>/signals.jsonl
clients/<client>/actions.json
clients/<client>/outputs/<run-id>/
```

Files are enough for v0.

# Outputs

Markdown/JSON remain the source of truth.

Optional deterministic renderers:

```bash
python scripts/render_csv.py templates/client-review.example.json
npm install
node scripts/render_pptx.mjs templates/client-review.example.json
python scripts/smoke_test.py
```

# Successful patterns we reuse

The repo borrows architecture patterns—not copied text—from adopted agent systems and verification-first agent work:

- bounded research jobs
- persistent account context
- multi-source evidence
- structured outputs
- research → compression → synthesis
- independent evaluator/verifier
- counterfactual/disconfirming-evidence search
- finite retry budgets
- explicit terminal states
- human review when evidence cannot close the loop

See [`docs/SUCCESSFUL_PATTERNS.md`](docs/SUCCESSFUL_PATTERNS.md).

# Validation target

The product is useful if an agency can take a real prospect/client and say:

> "I knew most of the facts separately. I had not connected them this way — and the verifier caught what the first agent got wrong. This changed what I want to pitch or ask."

That is a better success bar than "the report is long".

## License

MIT.
