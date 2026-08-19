# Architecture — v0.2

## Design goal

Agency Intelligence Agent is a **portable research and GTM intelligence layer for agencies**, not a SaaS application and not a business-consulting suite.

The host agent (ChatGPT, Codex, Claude, Hermes, Kimi, Cursor, etc.) supplies reasoning and whatever web/file tools it already has. This repository supplies the agency-specific research method, memory format, skill contracts and artifacts.

## System

```text
Client / Prospect files + URLs
            ↓
     client-context.md
            ↓
   prospect intelligence
  (company + current GTM)
            ↓
 competitor GTM intelligence
  (marketing/sales playbooks)
            ↓
category + geography patterns
            ↓
 customer/audience opportunity map
            ↓
    GTM opportunities
            ↓
   agency direction brief
            ↓
 pitch / strategy decisions made by agency
```

Recurring use adds:

```text
competitor watch → signals.jsonl → meeting prep / client review
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

Human-readable durable context:

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

Append-only GTM event memory.

Example:

```json
{
  "observed_at": "YYYY-MM-DD",
  "entity": "Competitor",
  "type": "gtm_move",
  "fact": "Launched a dedicated distributor program and city-specific recruitment pages",
  "source_url": "https://...",
  "confidence": "high",
  "impact": "Shows channel acquisition becoming a structured category motion",
  "recommended_action": "Check whether channel recruitment is a priority audience for the client"
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

## Skill execution contract

Every research skill follows:

### 1. Load context
Read available client/company material before searching.

### 2. Define the agency question
Examples:

- What does this company appear to be doing to acquire customers?
- How are competitors going to market?
- What works in this geography/category?
- Which customer archetypes are worth investigating?
- What should an agency consider pitching?

### 3. Plan research surfaces
Choose only relevant sources: website, use-case pages, case studies, social/PR, partner pages, events, competitor sites, geography/category evidence.

### 4. Gather evidence
Keep URLs/dates and distinguish company claims from independent evidence.

### 5. Normalize
Capture structured observations:

- audience
- positioning
- proof
- acquisition motion
- conversion path
- channel/partner motion
- geography
- content/search activity

### 6. Cross-source synthesis
Connect multiple observations into a GTM implication.

### 7. Compare
Identify:

- table stakes
- strong competitor playbooks
- repeated category patterns
- white spaces
- unsupported/noisy tactics

### 8. Translate for agency
Convert evidence into a few GTM/marketing directions and questions to validate.

### 9. Deliver artifact
Create a sourced Markdown/JSON artifact.

### 10. Stop
Stop when additional research no longer changes the GTM story.

## Research depth defaults

| Task | Default |
|---|---:|
| Main competitors | 3–5 |
| Useful company pages/sources | 5–10 |
| Competitor surfaces | 3–6 each |
| Customer archetypes | 3–6 |
| Agency GTM directions | 3–5 |
| Discovery questions | ≤10 |
| Meeting brief | ~1 page |

These are stopping guides, not hard evidence quotas.

## Tool interfaces

Skills may conceptually request:

- `search_web(query)`
- `fetch_url(url)`
- `read_client_files(path)`
- `search_drive(query)`
- `write_output(path, content)`

The repository does not implement these services. The host environment maps them to available tools.

## Failure modes

### Search-summary syndrome

**Failure:** report restates one source at a time.

**Fix:** require cross-source patterns and agency implications.

### Feature-table syndrome

**Failure:** competitor comparison lists product features.

**Fix:** compare positioning, audiences, proof, acquisition, conversion, channels and geography.

### Generic-agency syndrome

**Failure:** recommendations are "SEO, social, paid ads, content."

**Fix:** require who/why/channel/job/evidence and competitor/category precedent.

### Consulting drift

**Failure:** agent starts recommending margins, finance, product engineering, org design or business restructuring.

**Fix:** stop and mark as out of scope. This repo owns marketing/sales GTM research.

### Lead-list dumping

**Failure:** hundreds of company names without rationale.

**Fix:** define customer archetypes and buying triggers first; add illustrative accounts only after.

## Future architecture triggers

Add infrastructure only after repeated user pain:

- **Database:** files become operationally painful across many clients.
- **Scheduler:** agencies want automatic weekly competitor/market briefs.
- **Browser service:** host search tools repeatedly miss necessary public surfaces.
- **Drive adapter:** manual client-file movement becomes a blocker.
- **Dashboard:** agencies need cross-client portfolio views.
- **CRM/ad/content connectors:** only after agencies explicitly want approved intelligence pushed into execution systems.

Until then: **skills + files + host tools**.
