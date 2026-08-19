---
name: pricing-strategy
description: Analyze pricing and commercial terms for a client, product, RFQ, contract or market. Use when public list prices are unavailable, when the company sells custom/manufactured products, when a large order may stress margins/cash, or when the agency needs a value/pricing story rather than a guessed price.
---

# Pricing Strategy

## Goal

Answer **how should this company price and package the commercial deal?** without hallucinating a market price that is not public.

For industrial/manufacturing businesses, pricing is often a contract architecture rather than a sticker price.

## Read first

- `client-context.md`
- relevant competitive-intelligence output
- financial/working-capital inputs
- known RFQ/order/LOI terms
- cost, volume, tooling, freight, FX or payment data supplied by the user

## Pricing modes

Identify the actual pricing mode:

- public list price
- distributor/dealer price
- RFQ/custom part price
- cost-plus
- indexed/raw-material pass-through
- project/tooling + unit price
- capacity reservation
- volume-tier price
- annual contract / blanket PO
- outcome/value-based proposal

Do not force SaaS-style tiering onto industrial companies.

## Step 1 — identify the buyer's economic alternative

The competitor may be:

- machined/forged/cast version of the part
- imported component
- another supplier
- in-house manufacture
- existing design/process
- manual process

Build a `current alternative → client offer` comparison.

Consider:

- material use / scrap
- machining / secondary operations
- assembly count
- weight
- energy
- tool wear
- cycle time
- quality/rejection
- freight/import duties
- inventory
- lead time
- warranty/reliability
- local-content/regulatory benefits
- engineering effort

Pricing headroom comes from **customer value**, not merely seller cost.

## Step 2 — should-cost / floor-price architecture

Where data exists, map:

```text
material
+ conversion/manufacturing
+ secondary operations
+ tooling amortisation / NRE
+ quality/testing
+ packaging/freight
+ warranty/rejection reserve
+ inventory/safety stock carrying cost
+ receivable financing cost
+ FX/commodity exposure
+ sales/application engineering cost
= economic cost-to-serve
```

Then add required contribution/margin.

If inputs are unavailable, output the model with blanks and identify the three inputs management must supply. Do not invent them.

## Step 3 — contract terms that change real margin

For B2B manufacturing, explicitly inspect/recommend where relevant:

- raw-material index/pass-through formula
- FX adjustment
- annual price-down clauses
- minimum order quantity
- volume bands
- take-or-pay / committed volume
- tooling/NRE ownership and amortisation
- engineering-change charges
- prototype/sample pricing
- freight/incoterms
- payment days
- advance / milestone / LC structure
- safety-stock ownership
- forecast freeze window
- cancellation/obsolescence protection
- quality/warranty liability
- capacity reservation

A 5% higher quoted price can be worse than a lower price with better cash/volume terms; judge the whole contract.

## Step 4 — working-capital price

When receivable/inventory days are high, show the hidden financing burden.

Use:

```text
Working-capital exposure ≈ annual contract revenue × net funded days / 365
```

where `net funded days` should reflect the actual cash cycle, not automatically receivables + inventory - payables if the inputs are not comparable.

Estimate financing cost only when a defensible interest/cost-of-capital assumption is provided. Otherwise show a sensitivity table with user-visible assumptions.

## Step 5 — pricing corridors

Provide a decision framework, not a fake exact quote:

- **Floor:** minimum economically acceptable deal
- **Target:** price/terms that meet strategic margin and cash goals
- **Stretch/value price:** justified by buyer savings / localization / performance / scarcity
- **Walk-away conditions:** terms that make growth destructive

For each corridor identify what evidence would justify it.

## Step 6 — value communication

Industrial sales material should communicate the **economic conversion case**.

Useful assets:

- cost-down calculator
- forging/machining/import vs proposed-process comparison
- part-consolidation case
- material-yield comparison
- localization/TCO sheet
- weight/energy/quality comparison
- tooling payback by annual volume
- prototype-to-series pricing roadmap

Do not lead with `low cost` if the company has stronger engineering, localization, exclusivity or reliability value.

## Output

Create `clients/<slug>/outputs/pricing-strategy-YYYY-MM-DD.md`:

1. Pricing thesis
2. What the customer is really buying
3. Economic alternative / value drivers
4. Known cost-to-serve and missing inputs
5. Contract-term risks/opportunities
6. Pricing corridor
7. Recommended quote/negotiation architecture
8. Sales/marketing proof needed
9. Management questions
10. Sources / assumptions

## Quality gate

- Never state an exact market price without a source or supplied quote.
- Separate seller economics from customer value.
- Include working-capital/commercial terms for manufacturing contracts.
- Consider volume/tooling economics.
- Make clear which conclusions are facts vs scenario assumptions.
- Recommend a negotiation architecture that a commercial head could actually use.

## Stop condition

Stop when the commercial decision is clear and missing inputs are explicitly listed. Do not pretend uncertain costing is precision.
