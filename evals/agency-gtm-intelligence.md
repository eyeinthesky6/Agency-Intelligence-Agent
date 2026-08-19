# Eval — Agency GTM Intelligence

## Purpose

Prevent two common failures:

1. a long company summary followed by generic recommendations such as "do SEO, social media and paid ads";
2. a smart-sounding GTM story whose facts or interpretation do not survive independent verification.

This eval is harness/model agnostic. Run it with ChatGPT, Codex, Claude, Hermes, Kimi or any other agent that can use the skills and public web/file tools.

## Benchmark target

Use a real company where public GTM activity is visible but internal performance is not.

Reference example:

```text
examples/kazam-agency-prep/
```

## Prompt

> Run `01-prospect-intelligence`, `02-competitor-watch` in DEEP mode and `06-agency-direction`. Then run `07-verify-and-challenge` using fresh verifier and challenger contexts when supported. Build an agency-prep dossier covering company GTM, 3–5 competitor marketing/sales playbooks, category/geography patterns, customer archetypes and evidence-backed directions. Reopen and verify material sources, actively search for contrary evidence, reconcile the strategy, and return a terminal evidence receipt. Do not write finished campaigns or drift into management consulting.

# Evidence gate — hard fail before scoring

Score `FAIL` regardless of prose quality if any is true:

- no `claims.json` / material claim ledger exists
- no independent `verification.json` exists
- no counterfactual challenge was run for a major strategy output
- no `receipt.json` / explicit terminal state exists
- the final report presents a critical `UNSUPPORTED` or `CONTRADICTED` claim as fact
- the Reconciler introduces a new material factual claim without verification
- a material number/date/current count is cited only from a search snippet when the underlying source was accessible
- the Producer effectively self-certifies the report without a separate verification objective/context
- the system retries indefinitely until it finds supporting evidence

# Research-quality hard fail

Also fail if any is true:

- output is mainly a generic company profile
- competitor section is mostly a feature matrix
- no visible acquisition/conversion motions are compared
- no cross-source insight connects competitor activities into a GTM pattern
- recommendations are generic `SEO / social / ads / content`
- no customer archetypes / buying triggers are identified
- the agent invents internal CAC, conversion, pipeline or marketing performance
- the agent drifts into finance, pricing strategy, org design or product-engineering consulting
- no material sources are retained
- output writes the final campaign rather than preparing the agency to decide

# Scoring rubric — 100 points

## 1. Company GTM understanding — 12

Strong output identifies:

- what the company sells
- who appears to buy it
- geography
- positioning
- visible sales motion
- proof
- conversion paths
- partnerships/channels

## 2. Competitor marketing & sales playbooks — 18

At least 3 meaningful competitors should be compared across:

- positioning
- audiences
- acquisition motion
- proof/case studies
- conversion paths
- SEO/content/social/PR where relevant
- partnerships/channel motion
- geography

High scores explain **what each competitor appears to be trying to achieve through those activities**, without claiming success merely from visibility.

## 3. Cross-source synthesis — 15

- 0: one source → one bullet
- 7: several reasonable inferences
- 12: at least 3 useful patterns connecting multiple observations
- 15: patterns materially change what the agency should pitch/investigate and state important uncertainty

## 4. Category / geography intelligence — 8

Identify evidence-backed recurring GTM patterns such as:

- partner-led expansion
- local/tier-2/3 GTM
- trade/event/community importance
- enterprise proof
- franchise/distributor acquisition
- category education/search intent

Do not force geography if it does not matter.

## 5. Customer opportunity map — 8

Define 3–6 credible customer/buyer archetypes with:

- buying trigger
- problem/job
- likely decision maker
- company fit
- route to reach/influence

Do not substitute a giant lead list.

## 6. Agency strategic usefulness — 12

Directions should be specific and evidence-backed, for example:

- buyer/use-case journey architecture
- case-study/proof engine
- partner acquisition
- ABM for a defined account class
- local/regional GTM
- research/category authority distribution
- channel/distributor enablement

The agency should be able to use the output to decide what belongs in a pitch.

## 7. Evidence verification quality — 15

### 0–5
Verifier mostly rereads the report or checks citation presence.

### 6–10
Material numbers/dates/entities are independently reopened and checked; some corroboration is used.

### 11–15
Verifier:

- independently extracts material claims, including claims omitted by Producer;
- opens primary/current sources;
- checks exact number/unit/date/entity support;
- distinguishes marketing claims from externally established fact;
- corroborates critical claims when appropriate;
- records source conflict and broken links;
- forces material corrections/removals rather than rubber-stamping.

## 8. Counterfactual quality — 8

### 0–2
Generic criticism/caveats.

### 3–5
Plausible alternatives are considered and some contrary evidence is searched.

### 6–8
Challenger actively constructs the strongest alternative explanation, defines distinguishing evidence, searches for it, and **materially changes or strengthens recommendation priority when warranted**.

A counterfactual pass that never changes confidence or strategy across repeated benchmarks should be treated with suspicion.

## 9. Scope discipline & intellectual honesty — 4

- facts vs inference are visible
- important unknowns become discovery questions
- no invented performance data
- no consulting drift
- no finished campaign generation unless separately requested
- terminal state accurately reflects remaining uncertainty

# Pass threshold

Only runs that first pass the Evidence Gate are scored.

- **90–100:** strongly verified agency intelligence; pitch-prep ready
- **80–89:** strong and useful; minor strategist sharpening
- **70–79:** useful research but meaningful evidence/strategy weakness remains
- **50–69:** competent research assistant, weak intelligence loop
- **<50:** Google-summary or unreliable-agent output; do not ship

A `REVIEW_REQUIRED` run can still score well for intellectual honesty, but it is **not** presentation-ready until the named client/human questions are resolved.

A `FAILED_EVIDENCE_GATE` run fails regardless of score.

# Reference Kazam benchmark — why the validation stage matters

The Kazam example should be used to test whether the verification loop can **change** a plausible first-run strategy.

## First-run inference A — partner acquisition

```text
Statiq franchise/FOCO
+ ChargeZone franchise
+ Bolt distributor program
+ Kazam partner/dealer intake
→ partner/site/channel acquisition is a major category growth motion
```

Verification found the visible programs are real, but public evidence does not prove their relative revenue/economic importance.

Corrected conclusion:

```text
partner/site/channel acquisition is a recurring visible GTM motion
→ validate its economic importance to the prospect before pitching a dedicated partner program
```

## First-run inference B — data-led whitespace

Original:

```text
Kazam has large operating datasets
→ data-led category authority is an underused whitespace
```

Counterfactual evidence found that Kazam already operates EV Ready Homes and a Kazam/AEEE research motion; Bolt also publishes data-rich category material.

Corrected conclusion:

```text
research capability already exists
→ investigate whether its distribution/commercial use can become more systematic
```

## First-run inference C — enterprise-first priority

The public product website made enterprise/CPO/fleet/software opportunities visually prominent.

Fresh management evidence showed tier-2/3 three-wheeler/home charging is a major current revenue engine.

Corrected conclusion:

```text
separate the core 2W/3W regional/OEM engine from enterprise expansion
→ do not make an enterprise-only agency pitch without segment economics/pipeline data
```

This is the behavior the eval rewards: the validation loop is allowed to overturn a clever first answer.

# Reference insight shapes

These illustrate reasoning shape only. They must not be hard-coded as category rules.

### Competitor proof architecture

```text
prospect has quantified customer outcomes
+ competitor packages named enterprise cases visibly
→ prospect may have proof that is not organized for buyer-specific selling
→ agency can investigate proof/case-study architecture, subject to customer permissions
```

### Positioning complexity

```text
prospect serves many buyer types/products
+ competitors create dedicated use-case paths
→ breadth may create narrative complexity
→ agency must validate analytics/pipeline/sales feedback before proposing site restructuring
```

# Anti-hardcoding rule

The skill must discover equivalent patterns from evidence for other categories—leasing, BMS, batteries, SaaS, logistics, manufacturing, professional services, etc.—not reproduce EV-charging conclusions regardless of company.
