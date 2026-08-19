---
name: growth-opportunities
description: Turn client context, recent performance inputs, competitive signals, and agency observations into a maximum of three evidence-backed growth actions. Use when the agency asks what should we do next, needs ideas for a client, or wants to convert research into an actionable plan.
---

# Growth Opportunities

## Goal

Recommend **fewer, better actions**. This is the bridge between intelligence and useful agency work.

## Read first

- `client-context.md`
- recent `signals.jsonl`
- current/open `actions.json`
- supplied campaign/performance data
- latest client-review / meeting notes if relevant

Use fresh web research only to verify or complete a specific opportunity hypothesis.

## Opportunity sources

Look for evidence in four places:

1. **Client gap** — stated goal vs current execution/performance.
2. **Market signal** — demand/category/audience behavior that changed.
3. **Competitor move** — a threat or opening worth acting on.
4. **Operational opportunity** — something the agency can do faster/better with existing client assets.

## Ranking

Return at most 3 primary opportunities.

Score mentally or explicitly on:

- likely impact
- evidence strength
- fit with client goal
- fit with agency capability/scope
- effort / speed to test

Do not choose ideas merely because AI can generate them.

## Output

Create `clients/<slug>/outputs/growth-opportunities-YYYY-MM-DD.md`.

For each opportunity:

### [Opportunity name]

- **Evidence:** facts/signals/metrics supporting it
- **Why now:** why it deserves attention now
- **Recommended action:** concrete next move
- **First test:** smallest way to validate it
- **Expected outcome:** directional, not fabricated precision
- **Effort:** low / medium / high
- **Confidence:** high / medium / low
- **Dependencies:** data/assets/approval needed

Then add:

### Recommended sequence
What to do first, second, third and why.

### Do not do yet
Maximum 3 tempting but lower-priority ideas, only when useful.

## Action register

When the user approves an opportunity, add/update it in `actions.json` with status `approved`.

Do not silently mark a recommendation approved.

## Quality gate

Reject any recommendation that could be pasted unchanged into ten unrelated client reports.

## Stop condition

Three credible opportunities are enough. Do not produce an idea dump.
