# Agency Intelligence Agent

A lightweight, skill-based research and GTM intelligence layer for marketing and sales agencies.

It helps an agency understand a company, study its competitors' marketing and sales motions, identify category/geography patterns, map likely customer segments, and decide what strategic directions are worth pitching.

**The rule:** research deeply; recommend narrowly; leave execution to the agency.

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

## Core workflow

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
AGENCY PREP ARTIFACT
```

## What counts as intelligence

A search result is evidence, not the answer.

**Weak:**

> Statiq has a franchise page.

**Useful:**

> Statiq has a dedicated FOCO/franchise funnel, publishes business-model/setup education and promotes each local deployment. ChargeZone also markets franchise ownership, while Bolt.Earth recruits distributors and Kazam has partner/dealer intake. Together this suggests that partner/site acquisition is a category-level GTM motion in India, not merely a support function. An agency should therefore check whether the prospect needs a dedicated partner-acquisition journey rather than a generic contact form.

That is the standard: connect multiple public observations into an agency-relevant implication.

## What gets researched

### Company

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

### Competitors

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

### Market / geography

- what repeated acquisition motions appear to work
- metro vs tier-2/3 dynamics
- channel/partner importance
- local search / city pages
- category education needs
- trade/event/community importance
- public-sector/enterprise procurement where relevant

### Customer opportunity

First identify customer archetypes, not giant lead lists:

- who they are
- buying trigger
- problem/job
- likely decision maker
- why the company may fit
- route to influence/reach them

Illustrative target accounts come only after the archetype is credible.

## Repository layout

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
│   └── 06-agency-direction/
├── templates/
├── scripts/
└── examples/
    └── kazam-agency-prep/
```

## Quick start

### 1. Research the company

> Run `01-prospect-intelligence` for Kazam. Build a detailed agency-prep dossier. Study the company, visible GTM, 3–5 competitors, category/geography patterns and likely customer archetypes. Do not give me a generic company profile.

### 2. Go deeper on competitors

> Run `02-competitor-watch` in DEEP mode. Compare how competitors position, generate attention, build trust, recruit partners/channels and convert buyers. Tell me what appears table stakes, what looks effective and where there is whitespace.

### 3. Decide what the agency should consider pitching

> Run `04-growth-opportunities`. Give me the strongest evidence-backed GTM/marketing directions. Do not write campaigns yet.

### 4. Compress it for the agency partner

> Run `06-agency-direction`. Give me the account story, customer map, competitor precedents, pitch themes, what not to pitch and the questions we must ask before proposal.

## Example benchmark — Kazam Energy

The benchmark researches Kazam (reported FY25 revenue around ₹40 crore) against Statiq, Bolt.Earth and ChargeZone.

It surfaces patterns such as:

- partner/site/channel acquisition is a real category GTM motion
- use-case-specific landing pages are increasingly table stakes
- recognizable deployment/customer proof is critical trust currency
- enterprise case studies are strong sales-enablement assets
- tier-2/3/local expansion needs different GTM support than national brand messaging
- Kazam's broad technology stack can be reframed into simpler buyer journeys

See:

```text
examples/kazam-agency-prep/
```

## Client memory

```text
clients/<client>/client-context.md
clients/<client>/signals.jsonl
clients/<client>/actions.json
clients/<client>/outputs/
```

Files are enough for v0.

## Outputs

Markdown/JSON remain the source of truth.

Optional deterministic renderers:

```bash
python scripts/render_csv.py templates/client-review.example.json
npm install
node scripts/render_pptx.mjs templates/client-review.example.json
python scripts/smoke_test.py
```

## Successful patterns we reuse

The repo borrows architecture patterns—not copied text—from adopted agent systems:

- bounded research jobs
- persistent account context
- multi-source evidence
- structured outputs
- research → compression → synthesis
- finite tool budgets
- human approval before execution

See [`docs/SUCCESSFUL_PATTERNS.md`](docs/SUCCESSFUL_PATTERNS.md).

## Validation target

The product is useful if an agency can take a real prospect/client and say:

> "I knew most of the facts separately. I had not connected them this way, and this changed what I want to pitch or ask."

That is a better success bar than "the report is long".

## License

MIT.
