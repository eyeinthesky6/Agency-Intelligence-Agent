# Agency Intelligence Agent

A lightweight, skill-based AI workspace that helps agencies research prospects, understand clients, track competitors, prepare meetings, find growth opportunities, and create client-ready briefs.

**The rule:** useful bus, not interplanetary rocket.

This project intentionally starts as a portable set of Agent Skills, plain-text client memory, and tiny export scripts. It does **not** require a database, vector store, dashboard, multi-agent framework, browser farm, or custom SaaS backend.

## What it does

For each client or prospect, the agent can:

1. **Onboard context** — turn a website, proposal, brand deck, notes, reports, and competitor list into one reusable `client-context.md`.
2. **Research a prospect** — produce a concise pitch brief with likely problems, market context, competitors, opportunities, and questions to ask.
3. **Watch competitors** — report meaningful *changes*, not generic competitor summaries.
4. **Prepare a client meeting** — turn client context + recent signals + previous actions into a one-page briefing.
5. **Find growth opportunities** — recommend a small number of actions tied to evidence.
6. **Prepare a client review** — explain what changed, what the agency did, what it means, and what should happen next.
7. **Create a campaign brief** — convert an approved opportunity into an execution-ready brief.

## Successful patterns we deliberately copy

The architecture is based on patterns repeatedly seen in adopted agent products and open-source agents:

- **One clear job → one useful artifact.** GPT Researcher became popular by turning a research question into a sourced report rather than pretending to be a general employee.
- **Plan → research → compress → deliver.** Open Deep Research separates research, summarization/compression, and final report generation instead of asking one giant prompt to do everything.
- **Structured outputs with sources.** Claygent and Gumloop make agent research useful downstream by returning fields/tables with evidence, not just prose.
- **Persistent context.** Successful GTM skill packs store company/product context once and let later skills read it.
- **Finite tool budgets and recovery.** Browser-use exposes bounded actions and recovery loops instead of unlimited browsing.
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
│   └── 06-campaign-brief/
├── templates/
│   ├── client-context.md
│   ├── signal.example.json
│   └── weekly-intelligence.md
├── scripts/
│   ├── render_xlsx.py
│   └── render_pptx.py
└── examples/
    └── demo-client/
```

## Quick start

### 1. Give the agent a client

Create:

```text
clients/acme/
```

Put available client material there, or give the agent access to a Drive folder / uploaded files / URLs.

Then ask:

> Run `00-client-onboard` for Acme. Build the client context from what is available. Mark unknowns instead of inventing them.

The result is:

```text
clients/acme/client-context.md
```

### 2. Research before a meeting

> Run `03-meeting-prep` for Acme. Use the client context, recent signals, and open actions. Give me only what matters for tomorrow's meeting.

### 3. Check competitors

> Run `02-competitor-watch` for Acme. Check the named competitors and report only material changes since our last scan. Store sourced signals and recommend an action only where justified.

### 4. Ask what to do next

> Run `04-growth-opportunities` for Acme. Give me the top three evidence-backed opportunities, ranked by likely impact and effort.

## Client memory

The primary memory is deliberately boring:

```text
clients/<client>/client-context.md
clients/<client>/signals.jsonl
clients/<client>/actions.json
clients/<client>/outputs/
```

A signal should look like:

```json
{
  "observed_at": "2026-08-19",
  "entity": "Competitor A",
  "type": "pricing_change",
  "fact": "Introduced a lower-priced starter plan",
  "source_url": "https://example.com/pricing",
  "confidence": "high",
  "impact": "Reduces the entry-price gap against the client",
  "recommended_action": "Test value-led starter positioning before considering a discount"
}
```

That JSONL history is enough memory for v0. We will add infrastructure only when users prove they need it.

## Outputs

The canonical output is Markdown. Two optional scripts convert structured review data into familiar agency artifacts:

- `scripts/render_xlsx.py` → action / signal tracker
- `scripts/render_pptx.py` → short client intelligence deck

Markdown stays the source of truth so the system remains inspectable and portable across Codex, Claude Code, Cursor, Windsurf, and other Agent-Skills-compatible environments.

## Product boundary

### In v0

- web research using the host agent's existing search/browser tools
- client-file / Drive context when the host provides it
- sourced competitor signals
- prospect briefs
- meeting prep
- growth recommendations
- client-review narratives
- campaign briefs
- PPTX/XLSX export

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
- competitor update
- monthly review
- new campaign recommendation

The core question is not "Is the AI impressive?" It is **"Did this save the agency time or help it look smarter in front of a client?"**

## License

License to be selected before public reuse of third-party-derived material. This repository currently borrows **patterns**, not copied skill text, from external projects.
