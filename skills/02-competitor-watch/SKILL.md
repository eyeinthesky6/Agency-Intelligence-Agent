---
name: competitor-watch
description: Run either a recurring competitor-change watch or a deeper competitive/product-market intelligence investigation. Use when the agency needs to know what changed, why a company wins or loses, where competitors are moving, how products/pricing/channels differ, or what non-obvious commercial opportunity follows from multiple weak signals.
---

# Competitive Intelligence

## Goal

Do **not** summarize Google results. Build a commercially useful story by connecting facts that are individually public but whose implication is not.

The skill has two modes:

- **WATCH** — recurring scan for meaningful deltas since the last run.
- **DEEP** — first-pass or strategic investigation of product, market, customers, pricing, channels and competitive position.

If the user asks for competitor research, competitive strategy, product-market analysis, pricing context, market entry, or a deeper account thesis, use **DEEP**.

## Read first

- `clients/<slug>/client-context.md`
- `clients/<slug>/signals.jsonl` if it exists
- latest financial/client data if supplied
- recent actions and prior intelligence outputs

Default direct competitors: 3–5. Also consider **substitutes/status quo**, because industrial companies often compete against another manufacturing process, in-house production, imports or doing nothing rather than only named firms.

# DEEP mode

## 1. Build the evidence map before forming the story

Investigate across these surfaces when relevant:

### Company economics
- revenue trajectory and margins
- working capital / receivables / inventory / debt pressure
- major capex or capacity additions
- order wins / LOIs / customer concentration
- export/domestic mix
- any unusually large contract relative to company scale

### Customers and buying power
- disclosed customers / logos
- OEM vs Tier-1 vs distributor/channel mix
- concentration risk
- single-source vs multi-source status where visible
- buyer priorities: cost-down, quality, localization, lead time, warranty, compliance, weight, yield, uptime, etc.

### Product
- portfolio by application, not merely by SKU
- products tied to growing vs declining end-markets
- new technology, patents, licensing, JV/partner technology
- adjacent use cases competitors already serve
- substitution opportunity: what process/product can this replace?
- proof that turns a product into a buyer outcome

### Competitors
- direct rivals
- international competitors entering/localizing
- substitutes / alternative manufacturing processes
- adjacent companies expanding into the client's category
- competitor product breadth, application breadth, geography and customer story

### Pricing and commercial model
- public list prices when they exist
- RFQ/custom pricing when public prices do not exist
- likely pricing unit: part, kg, tooling/NRE, subscription, project, machine-hour, etc.
- raw-material pass-through or indexation clues
- tooling/amortisation, MOQ and volume economics
- freight/FX/payment-term exposure
- cost of working capital and inventory created by the contract
- buyer's total economic alternative, not only seller cost

### Channels / route to market
- direct enterprise/OEM sales
- distributors/dealers/agents
- exports
- tender/geM/public procurement
- industry exhibitions
- application engineering/co-development
- digital inbound where actually relevant

### Messaging / discoverability
- what the company claims on its website
- what customers likely buy instead
- proof/assets missing from the public story
- whether positioning describes a manufacturing process or a customer result
- discoverability for application-level searches

## 2. Cross-source synthesis — mandatory

A **deep insight** must combine at least two independent facts or sources.

Good:

> The company has a very large export order relative to annual revenue + already has stretched receivables/inventory → growth may worsen cash pressure unless commercial terms, batch scheduling and working-capital pricing are managed.

Bad:

> The company received a large export order.

For every major thesis, show:

- **Evidence A**
- **Evidence B**
- **Inference**
- **Commercial implication**
- **What would falsify it / what to verify with management**

This prevents the model from disguising a search snippet as intelligence.

## 3. Product-market map

Create a compact matrix:

| Product/application | Current end-market | Growth direction | Competitive/substitute pressure | Client strength | Commercial move |
|---|---|---|---|---|---|

Use `growth direction` as `growing / mature / declining / uncertain`, and explain uncertain calls.

For manufacturers, explicitly look for **portfolio migration**: revenue-generating legacy products that may decline and newer products that need commercialization.

## 4. Competitive matrix

Compare only dimensions that buyers actually care about. Depending on the industry this may include:

- technical capability
- part complexity / tolerance
- materials/process range
- quality/certifications
- capacity / localization
- engineering support
- lead time
- application breadth
- export capability
- cost-down potential
- design ownership / IP
- price structure
- customer concentration/reliability risk

Do not use arbitrary 1–10 scores unless evidence supports them. Prefer `advantage / parity / disadvantage / unknown` with rationale.

## 5. Commercial story

The final answer must contain a **story**, not a fact dump:

### Where the company makes money today
Legacy/current economic engine.

### What is changing underneath it
Technology, customers, market structure, cost structure or competition.

### Where the next revenue pool may come from
Specific product/application/customer/geography pathways.

### What could stop it
Concentration, cash, capability, channel, pricing, certification, sales-cycle, capacity or execution risk.

### What the agency/company should do
Maximum 5 recommendations, each tied to the story.

## 6. Marketing recommendations for industrial/B2B clients

Do not default to social media/content calendars.

Prefer commercial marketing assets such as:

- application-specific landing pages
- engineering design guides
- cost-down / conversion calculators
- before-vs-after manufacturing economics
- technical case studies
- RFQ qualification forms
- buyer-specific battlecards
- target-account lists
- localization/import-substitution campaigns
- trade-show account plans
- distributor/channel kits
- product proof packs
- sample/prototype offers
- customer expansion programs

Marketing should reduce sales friction or open accounts.

# WATCH mode

Use the named competitors from client context. Default maximum: 5.

Check high-signal surfaces:

- positioning
- pricing / packaging / contract model when visible
- product / technology / patents / launches
- customers / order wins
- capacity / localization / geography
- partnerships / acquisitions / licensing
- executive hiring relevant to direction
- major campaigns/offers

Compare findings with prior signals. Report **deltas only**.

Usually ignore cosmetic redesigns, generic thought leadership, minor awards and repetitive news.

# Signal format

Append material findings to `clients/<slug>/signals.jsonl`:

```json
{"observed_at":"YYYY-MM-DD","entity":"Competitor","type":"product_move","fact":"...","source_url":"https://...","confidence":"high","impact":"...","recommended_action":"..."}
```

# Fact → Impact → Act

For surfaced items:

- **Fact** — verifiable observation
- **Impact** — why it matters to this client
- **Act** — specific move worth considering

If impact is weak, discard the item.

# DEEP output

Create `clients/<slug>/outputs/competitive-intelligence-YYYY-MM-DD.md`:

1. Executive thesis — 3–5 bullets
2. Evidence map
3. Where the company makes money today
4. What is changing underneath it
5. Product-market map
6. Competitive/substitute map
7. Pricing/commercial-model observations
8. Route-to-market / messaging gaps
9. Three to five recommended moves
10. What management should verify
11. Sources

# WATCH output

Create `clients/<slug>/outputs/competitor-watch-YYYY-MM-DD.md`:

- Executive read
- Material deltas table
- Implications/actions
- Noise ignored
- Suggested client discussion

# Quality gate

Before finishing DEEP mode:

- At least 3 important insights must be cross-source syntheses rather than copied facts.
- At least one substitute/status-quo competitor must be considered where relevant.
- Product, customer, pricing/commercial and route-to-market perspectives must all be touched.
- Recommendations must fit the company's economics and actual buying process.
- Facts and inference must be visibly separate.
- The output should contain something a competent person would **not** get from the first page of Google results.

# Stop condition

Stop when additional sources stop changing the commercial story. Depth is synthesis, not source count.
