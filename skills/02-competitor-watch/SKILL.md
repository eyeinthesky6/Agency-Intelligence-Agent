---
name: competitor-watch
description: Check a client's named competitors for material changes and turn verified deltas into sourced signals and actions. Use for weekly/monthly intelligence, before client reviews, or when a competitor is known to have launched, repriced, rebranded, or changed positioning.
---

# Competitor Watch

## Goal

Answer one question: **what changed around this client that the agency should care about?**

Do not produce generic competitor profiles on every run.

## Read first

- `clients/<slug>/client-context.md`
- `clients/<slug>/signals.jsonl` if it exists
- recent actions if relevant

Use the named competitors from client context. Default maximum: 5.

## Per-competitor checks

Check only high-signal surfaces:

- homepage / core positioning
- pricing / packaging when public
- product/changelog/launches
- major campaign/offer if visible
- relevant partnership/acquisition/funding only if it changes competitive behavior
- current search/news for meaningful changes

Default maximum: 4 pages/sources per competitor plus focused search.

## Delta rule

Compare findings with prior signals or the baseline client context.

A finding is worth recording when it is materially new, such as:

- positioning moved onto the client's wedge
- pricing/package changed
- important new product/capability/offer
- meaningful target-segment expansion
- category terminology shifted
- strong campaign/creative/message worth reacting to
- competitor withdrew, failed, was acquired, or left an opening

Usually ignore:

- cosmetic redesigns
- generic thought-leadership posts
- funding with no apparent GTM/product implication
- minor features irrelevant to the client
- repetitive news

## Signal format

Append each material finding to `clients/<slug>/signals.jsonl`:

```json
{"observed_at":"YYYY-MM-DD","entity":"Competitor","type":"positioning_change","fact":"...","source_url":"https://...","confidence":"high","impact":"...","recommended_action":"..."}
```

Use `recommended_action` only where justified.

## Fact → Impact → Act

For every surfaced item:

- **Fact** — what verifiably changed
- **Impact** — why this matters to this specific client
- **Act** — what the agency/client should consider doing

If Impact is weak, discard the item.

## Output

Create `clients/<slug>/outputs/competitor-watch-YYYY-MM-DD.md`:

### Executive read
Maximum 5 bullets.

### Material changes
Table:

| Competitor | Fact / delta | Impact | Recommended act | Confidence | Source |
|---|---|---|---|---|---|

### What not to react to
Optional short section for tempting but irrelevant noise.

### Suggested discussion for client
Maximum 3 points.

## No-change behavior

`No material competitive change found` is a valid result. State what was checked and stop.

## Stop condition

Stop after named competitors and category-level checks are covered or evidence begins repeating. Never browse indefinitely to manufacture a weekly update.
