# Agency Intelligence Agent

A lightweight, skill-based AI workspace that helps agencies research prospects, understand clients, investigate competitors, uncover non-obvious commercial insights, think through pricing, prepare meetings, find growth opportunities, and create client-ready briefs.

**The rule:** useful bus, not interplanetary rocket.

This project intentionally starts as a portable set of Agent Skills, plain-text client memory, and tiny export scripts. It does **not** require a database, vector store, dashboard, multi-agent framework, browser farm, or custom SaaS backend.

## What it does

For each client or prospect, the agent can:

1. **Onboard context** — turn a website, proposal, brand deck, notes, reports, and competitor list into one reusable `client-context.md`.
2. **Research a prospect** — produce a pitch brief with evidence-backed hypotheses and questions to validate them.
3. **Run deep competitive intelligence** — connect product, financial, customer, pricing, channel and competitor clues into a commercial story rather than summarising search results.
4. **Watch competitors** — report meaningful *changes*, not generic profiles.
5. **Prepare a client meeting** — turn client context + recent signals + previous actions into a one-page briefing.
6. **Find growth opportunities** — recommend a small number of actions tied to evidence.
7. **Prepare a client review** — explain what changed, what the agency did, what it means, and what should happen next.
8. **Create a campaign brief** — convert an approved opportunity into an execution-ready brief.
9. **Build a pricing strategy** — for list-price or RFQ businesses, separate seller cost, buyer value, working-capital exposure and contract terms instead of guessing a market price.

## Successful patterns we deliberately copy

The architecture is based on patterns repeatedly seen in adopted agent products and open-source agents:

- **One clear job → one useful artifact.** GPT Researcher became popular by turning a research question into a sourced report rather than pretending to be a general employee.
- **Plan → research → compress → deliver.** Open Deep Research separates research, summarization/compression, and final report generation instead of asking one giant prompt to do everything.
- **Structured outputs with sources.** Claygent and Gumloop make agent research useful downstream by returning fields/tables with evidence, not just prose.
- **Persistent context.** Successful GTM skill packs store company/product context once and let later skills read it.
- **Finite tool budgets and recovery.** Browser Use exposes bounded actions and recovery loops instead of unlimited browsing.
- **Cross-source synthesis.** A deep insight must connect multiple facts and explain the commercial implication; copied search snippets do not qualify.
- **Human approval before execution.** This repo recommends actions; it does not autonomously spend ad budgets, alter campaigns, or contact customers in v0.

See [`docs/SUCCESSFUL_PATTERNS.md`](docs/SUCCESSFUL_PATTERNS.md) for the research notes and what we intentionally rejected.

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
│   ├── 06-campaign-brief/
│   └── 07-pricing-strategy/
├── templates/
│   ├── client-context.md
│   ├── signal.example.json
│   ├── client-review.example.json
│   └── weekly-intelligence.md
├── scripts/
│   ├── render_csv.py
│   ├── render_pptx.mjs
│   └── smoke_test.py
└── examples/
    ├── wakefit-prospect/
    └── sintercom-prospect/
```

## Quick start

### 1. Give the agent a client

Create `clients/acme/`, put available material there (or grant access to a Drive folder / uploads / URLs), then ask:

> Run `00-client-onboard` for Acme. Build the client context from what is available. Mark unknowns instead of inventing them.

### 2. Research a prospect

> Run `01-prospect-intelligence` for Acme. Give me three or fewer evidence-backed opportunity hypotheses and the questions I should ask to validate them.

### 3. Run deeper competitive intelligence

> Run `02-competitor-watch` in DEEP mode for Acme. Do not summarise search results. Build a product-market, customer, competitor, pricing/commercial and route-to-market story. Every major insight must combine at least two pieces of evidence and state what would falsify the inference.

### 4. Check what changed later

> Run `02-competitor-watch` in WATCH mode for Acme. Report only material changes since our last scan.

### 5. Work out pricing/commercial terms

> Run `07-pricing-strategy` for Acme. If prices are not public, do not guess them. Show the buyer's economic alternative, cost-to-serve model, working-capital exposure, contract terms, pricing corridor and what management must supply before quoting.

### 6. Prepare for a meeting

> Run `03-meeting-prep` for Acme. Use the client context, recent signals, and open actions. Give me only what matters for tomorrow's meeting.

### 7. Ask what to do next

> Run `04-growth-opportunities` for Acme. Give me the top three evidence-backed opportunities, ranked by likely impact and effort.

## What counts as an insight

A search result is evidence, not intelligence.

**Bad:**

> Company X received a ₹150 crore export order.

**Useful:**

> The order is unusually large relative to Company X's annual revenue, while its receivable/inventory cycle and bank-limit utilisation are already stretched. If the order ramps without better payment, batching or inventory terms, revenue growth can create a financing problem. The commercial recommendation is therefore not merely "win more orders"; it is to price working capital and order-smoothing into the contract.

The second statement is an inference. It must show the source facts, confidence, and the management data needed to verify it.

## Industrial/manufacturing research

For B2B manufacturers, DEEP mode explicitly looks at:

- customers and customer concentration
- single-source / multi-source status
- order wins relative to company size
- legacy vs emerging product families
- substitute manufacturing processes
- technology licensing / JVs / patents
- capacity / localization / exports
- working capital and margin pressure
- RFQ pricing architecture
- raw-material pass-through / FX / tooling / payment terms
- competitors' application breadth
- application-engineering and technical marketing gaps

The result should help the company sell, price, diversify, position or choose a product/market direction — not merely create a content calendar.

## Client memory

The primary memory is deliberately boring:

```text
clients/<client>/client-context.md
clients/<client>/signals.jsonl
clients/<client>/actions.json
clients/<client>/outputs/
```

That JSONL history is enough memory for v0. Add infrastructure only when users prove they need it.

## Outputs

Markdown/JSON remain the source of truth. Optional deterministic renderers convert client-review JSON into familiar agency artifacts:

```bash
# Excel-readable tracker/table; no dependencies
python scripts/render_csv.py templates/client-review.example.json

# Six-slide PowerPoint
npm install
node scripts/render_pptx.mjs templates/client-review.example.json

# Repository contract checks
python scripts/smoke_test.py
```

## Product boundary

### In v0

- web research using the host agent's existing search/browser tools
- client-file / Drive context when the host provides it
- deep competitive/product-market intelligence
- sourced competitor signals
- B2B/RFQ pricing strategy
- prospect briefs
- meeting prep
- growth recommendations
- client-review narratives
- campaign briefs
- PPTX + Excel-readable CSV export

### Explicitly not in v0

- autonomous ad execution
- CRM replacement
- social scheduler
- SEO crawler
- BI dashboard
- always-on browser infrastructure
- custom scraping platform
- multi-agent swarm
- vector database
- custom auth / SaaS UI

Those are future options only if an agency repeatedly asks for them and will pay for them.

## Validation target

A v0 run is useful if an agency can take a real prospect/client and, with limited editing, use at least one output in a client-facing workflow:

- pitch/proposal preparation
- client meeting prep
- competitive/product strategy
- pricing/commercial discussion
- competitor update
- monthly review
- new campaign recommendation

The core question is not "Is the AI impressive?" It is **"Did this uncover something decision-useful, save the agency time, or help it look materially smarter in front of the client?"**

## License

MIT. This repository borrows **patterns**, not copied third-party skill text, from the referenced projects.
