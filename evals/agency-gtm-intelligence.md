# Eval — Agency GTM Intelligence

## Purpose

Prevent the core failure mode of agency research agents: a long company summary followed by generic recommendations such as "do SEO, social media and paid ads."

This eval is harness/model agnostic. Run it with ChatGPT, Codex, Claude, Hermes, Kimi or any other agent that can use the skills and public web/file tools.

## Benchmark target

Use a real company where public GTM activity is visible but internal performance is not.

Reference example:

```text
examples/kazam-agency-prep/
```

## Prompt

> Run `01-prospect-intelligence` for this prospect, then `02-competitor-watch` in DEEP mode and `06-agency-direction`. Build an agency-prep dossier: company GTM, 3–5 competitor marketing/sales playbooks, category/geography patterns, customer archetypes and evidence-backed directions the agency could consider pitching. Do not write finished campaigns or drift into management consulting.

## Hard fail

Score `FAIL` if any is true:

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

## Scoring rubric — 100 points

### 1. Company GTM understanding — 15

Strong output identifies:

- what the company sells
- who appears to buy it
- geography
- positioning
- visible sales motion
- proof
- conversion paths
- partnerships/channels

### 2. Competitor marketing & sales playbooks — 25

At least 3 meaningful competitors should be compared across:

- positioning
- audiences
- acquisition motion
- proof/case studies
- conversion paths
- SEO/content/social/PR where relevant
- partnerships/channel motion
- geography

High scores explain **what each competitor is trying to achieve through those activities**.

### 3. Cross-source synthesis — 20

- 0: one source → one bullet
- 10: several reasonable inferences
- 15: at least 3 useful patterns connecting multiple observations
- 20: patterns materially change what the agency should pitch/investigate and state important uncertainty

### 4. Category / geography intelligence — 10

Identify evidence-backed recurring GTM patterns such as:

- partner-led expansion
- local/tier-2/3 GTM
- trade/event/community importance
- enterprise proof
- franchise/distributor acquisition
- category education/search intent

Do not force geography if it does not matter.

### 5. Customer opportunity map — 10

Define 3–6 credible customer/buyer archetypes with:

- buying trigger
- problem/job
- likely decision maker
- company fit
- route to reach/influence

Do not substitute a giant lead list.

### 6. Agency strategic usefulness — 15

Directions should be specific and evidence-backed, e.g.:

- buyer/use-case journey architecture
- case-study/proof engine
- partner acquisition
- ABM for a defined account class
- local/regional GTM
- category authority/data-led content
- channel/distributor enablement

The agency should be able to use the output to decide what belongs in a pitch.

### 7. Scope discipline & intellectual honesty — 5

- facts vs inference are visible
- important unknowns become discovery questions
- no invented performance data
- no consulting drift
- no finished campaign generation unless separately requested

## Pass threshold

- **85–100:** strong agency intelligence; pitch-prep ready
- **70–84:** useful research; needs strategist sharpening
- **50–69:** competent research assistant, weak strategic synthesis
- **<50:** Google-summary agent; do not ship

## Reference Kazam insight shapes

These examples illustrate the required reasoning shape. They must not be hard-coded as rules.

### Example A — partner acquisition pattern

```text
Statiq franchise/FOCO
+ ChargeZone franchise
+ Bolt distributor program
+ Kazam partner/dealer intake
→ ecosystem/site/channel acquisition is a recurring category GTM motion
→ agency should determine whether the prospect needs a dedicated partner journey
```

### Example B — proof architecture

```text
Kazam has quantified product outcomes
+ Bolt prominently publishes named enterprise case studies
→ prospect has proof but competitor packages trust more visibly by buyer/use case
→ agency can investigate a systematic enterprise proof/case-study engine
```

### Example C — positioning complexity

```text
prospect serves many buyer types/products
+ competitors create dedicated pages for individual use cases
→ breadth may need buyer-specific narrative paths
→ agency should validate site/pipeline data before proposing a journey restructure
```

## Anti-hardcoding rule

The skill must discover equivalent patterns from evidence for other categories—leasing, BMS, batteries, SaaS, logistics, manufacturing, professional services, etc.—not reproduce EV-charging conclusions regardless of company.
