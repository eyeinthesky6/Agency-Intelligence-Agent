# Architecture — v0.1

## Design goal

Agency Intelligence Agent is a **portable intelligence layer**, not a SaaS application yet.

The host agent (Codex, Claude Code, ChatGPT with tools, Cursor, etc.) supplies reasoning and whatever web/file tools it already has. This repository supplies the **agency-specific operating method, memory format, and artifacts**.

## System

```text
                           ┌────────────────────┐
                           │ Client / Prospect  │
                           │ files + URLs       │
                           └─────────┬──────────┘
                                     │
                                     v
                         ┌──────────────────────┐
                         │ client-context.md    │
                         │ durable human memory │
                         └─────────┬────────────┘
                                   │
             ┌─────────────────────┼──────────────────────┐
             │                     │                      │
             v                     v                      v
     prospect intelligence  competitor watch       meeting prep
             │                     │                      │
             └──────────────┬──────┴──────────────┬───────┘
                            │                     │
                            v                     v
                      signals.jsonl          actions.json
                            │                     │
                            └──────────┬──────────┘
                                       v
                           growth opportunities
                                       │
                           ┌───────────┴───────────┐
                           v                       v
                    campaign brief          client review
                                                   │
                                      ┌────────────┴────────────┐
                                      v                         v
                                  Markdown                 PPTX / CSV
```

## Canonical client workspace

```text
clients/<slug>/
├── client-context.md
├── signals.jsonl
├── actions.json
├── source-notes/
└── outputs/
```

### `client-context.md`

Human-readable durable context: business, offer, ICP/audience, positioning, proof, competitors, brand voice, goals, known metrics, current campaigns, constraints, and open questions.

### `signals.jsonl`

Append-only event memory. One JSON object per line.

Minimum schema:

```json
{
  "observed_at": "YYYY-MM-DD",
  "entity": "Name",
  "type": "pricing_change",
  "fact": "Verifiable observation",
  "source_url": "https://...",
  "confidence": "high",
  "impact": "Why this matters to the client",
  "recommended_action": "Optional justified action"
}
```

### `actions.json`

Small action register. Suggested schema:

```json
[
  {
    "id": "A-001",
    "created_at": "YYYY-MM-DD",
    "action": "Test new comparison landing page",
    "why": "Competitor adopted client's core positioning",
    "priority": "high",
    "owner": "Unassigned",
    "status": "proposed",
    "evidence": ["source URL"],
    "source_signal_ids": []
  }
]
```

Allowed status values in v0:

- `proposed`
- `approved`
- `in_progress`
- `done`
- `rejected`

## Skill execution contract

Every skill follows the same internal shape:

### 1. Load context
Read the minimum relevant client files first.

### 2. Define the question
Do not browse until the decision/output is explicit.

### 3. Plan
For research-heavy tasks, define 2–5 focused questions or checks.

### 4. Gather evidence
Use host web/file tools. Retain source URLs and dates.

### 5. Normalize
Convert observations into structured facts/signals.

### 6. Compress
Remove repeated/noisy facts. Rank by relevance to the client.

### 7. Interpret
Use `Fact → Impact → Act`.

### 8. Deliver
Create a concise Markdown artifact and update memory only where warranted.

### 9. Stop
Do not keep researching after the decision is supported.

## Interfaces, not infrastructure

A skill may conceptually request:

- `search_web(query)`
- `fetch_url(url)`
- `read_client_files(path)`
- `search_drive(query)`
- `write_output(path, content)`

But v0 does not implement these services. The host environment maps them to available tools.

This keeps the repo portable.

## Research budgets

Default maximums unless the user changes them:

| Task | Default budget |
|---|---:|
| Competitors per scan | 5 |
| Focused web queries | 5 |
| Pages per competitor | 4 |
| Primary recommendations | 3 |
| Meeting brief length | 1 page-ish |
| Client review deck | 6 slides |

Budgets exist to stop research agents turning every question into a thesis.

## Failure modes

### Missing context
Proceed with public information, label assumptions, and list the minimum missing inputs that would improve the result.

### Source inaccessible
Record the limitation and use another credible source. Do not fabricate the missing content.

### Conflicting sources
Prefer the authoritative/current source and explicitly record the conflict when material.

### No meaningful change
Return "No material change found". This is a valid successful run.

### Too many opportunities
Rank and return three. Put the rest in a short parking-lot section only if unusually important.

## Future architecture triggers

Add infrastructure only when validation produces a repeated pain:

- **Database:** agency has enough clients/signals that files become operationally painful.
- **Scheduler:** agencies repeatedly ask for automatic weekly delivery.
- **Browser service:** host web tools cannot access critical sources reliably.
- **Drive adapter:** repeated manual file movement becomes a blocker.
- **Dashboard:** agencies repeatedly ask for cross-client visibility that artifacts cannot satisfy.
- **Execution connectors:** agencies trust recommendations and explicitly want approved actions pushed into ad/CRM/content systems.

Until then, files + skills remain the architecture.
