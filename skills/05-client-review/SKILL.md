---
name: client-review
description: Turn client context, supplied performance data, completed/open actions, and recent market/competitor signals into a concise client-facing review. Use for weekly/monthly/quarterly reviews, renewal conversations, or when the agency needs to show what happened, what it means, and what comes next.
---

# Client Review

## Goal

Help an agency explain value and make the next decision. Do not create a vanity-metric dump.

## Read first

- `client-context.md`
- relevant performance report/data supplied by the agency
- recent `signals.jsonl`
- `actions.json`
- previous review/meeting notes when available

Do not invent missing performance data. If data is absent, produce an intelligence/strategy review and say so clearly.

## Narrative

Use this sequence:

```text
WHAT HAPPENED → WHY IT MATTERS → WHAT WE LEARNED → WHAT WE RECOMMEND → WHAT NEEDS A DECISION
```

Separate:

- client/business performance
- agency activity/output
- external market/competitor changes
- hypotheses/inferences

Do not claim the agency caused an outcome unless evidence supports attribution.

## Output A — review Markdown

Create `clients/<slug>/outputs/client-review-YYYY-MM-DD.md`:

### 1. Executive summary
Maximum 5 bullets.

### 2. Performance / progress
Use supplied metrics and actions. Highlight movement vs goal when comparable data exists.

### 3. What changed outside the account
Only material market/competitor signals.

### 4. What we learned
Evidence-backed lessons, including what did not work.

### 5. Recommended next actions
Maximum 3, tied to evidence.

### 6. Decisions needed from client
Clear approvals/questions/blockers.

### 7. Sources / data caveats

## Output B — renderer data

Create `clients/<slug>/outputs/client-review-YYYY-MM-DD.json` with:

```json
{
  "client": "Client Name",
  "period": "Review period",
  "headline": "One-line account read",
  "executive_summary": ["..."],
  "metrics": [{"name":"","current":"","previous":"","note":""}],
  "signals": [{"fact":"","impact":"","source":""}],
  "actions_completed": ["..."],
  "recommendations": [{"action":"","why":"","priority":"high"}],
  "decisions_needed": ["..."]
}
```

This JSON is deliberately simple so PPTX/CSV rendering is deterministic.

## Six-slide default

If a presentation is requested, use:

1. Client pulse
2. Performance / progress
3. Market & competitor changes
4. What we learned
5. Recommended actions
6. Decisions / next 30 days

## Quality gate

A client should understand the account story without the agency person narrating every chart.

## Stop condition

Six slides / a short review is enough unless the user asks for detail.
