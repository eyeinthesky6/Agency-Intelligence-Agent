# Eval — Industrial Deep Intelligence

## Purpose

Catch the most common failure mode of research agents: a well-formatted Google summary presented as intelligence.

This eval is model/harness agnostic. Run it with ChatGPT, Codex, Claude, Hermes, Kimi, or any other agent that can use the repository skill and public web/file tools.

## Test target

Use a real ₹50–200 crore industrial/manufacturing company with enough public evidence to research.

Reference example in this repo:

```text
examples/sintercom-prospect/
```

## Prompt

> Run `02-competitor-watch` in DEEP mode for this company. Build a commercial intelligence story across product, customer, competitor/substitute, pricing/commercial terms, route to market and financial constraints. Do not merely summarize search results. Separate facts from inference and state what management must verify.

## Hard fail

Score `FAIL` if any is true:

- output is mainly a company profile / SWOT
- major "insights" are each restatements of a single source
- no substitute/status-quo manufacturing process is considered
- pricing section invents exact market prices without evidence
- marketing recommendations default to generic SEO/social/content
- no connection between financial/operational economics and GTM recommendations
- no management-verification questions
- recommendations could be pasted into an unrelated manufacturer report

## Scoring rubric — 100 points

### 1. Cross-source synthesis — 25

- 0: search summary
- 10: some inference, weakly tied to evidence
- 20: at least 3 useful insights combining multiple facts
- 25: insights materially alter recommended commercial action and show falsifiers/verification needs

### 2. Product / portfolio intelligence — 15

Must identify where relevant:

- current cash engine
- legacy/at-risk products
- emerging/new products
- product-market adjacency
- product substitution logic

### 3. Customer / account intelligence — 15

Look for:

- customer concentration
- buyer type
- single-source / switching dynamics
- share-of-wallet / expansion hypothesis
- diversification need

### 4. Competitive / substitute intelligence — 15

Must include more than named rivals.

Examples:

- competing manufacturing process
- import
- in-house production
- existing design/status quo

### 5. Pricing / commercial intelligence — 15

For custom/RFQ businesses:

- no invented prices
- buyer economic alternative
- tooling/NRE
- volume economics
- raw-material / FX exposure where relevant
- receivable/inventory/working-capital terms where material
- floor / target / value logic

### 6. Route-to-market / marketing usefulness — 10

Recommendations should improve industrial sales friction, proof, qualification or account penetration.

Good examples:

- technical RFQ tool
- design guide
- conversion/TCO calculator
- account-specific proof
- application pages
- prototype program

### 7. Actionability / intellectual honesty — 5

- recommendations are few and specific
- assumptions visible
- management questions identify critical unknowns

## Pass threshold

- **85–100:** strong; usable for agency/client strategy
- **70–84:** useful but needs human sharpening
- **50–69:** research assistant, not intelligence agent
- **<50:** superficial summary; do not ship

## Reference Sintercom insight examples

These are examples of the *shape* of acceptable synthesis, not facts the model should hard-code:

### Example A

```text
large new order relative to current revenue
+ long receivable/inventory cycle
+ high banking utilization
→ order growth could create working-capital stress
→ price/contract cash terms, forecast and safety stock explicitly
```

### Example B

```text
legacy ICE/transmission product portfolio
+ emerging EV/SMC capability/licensing
+ competitors diversified across more applications
→ portfolio transition is strategic, not just a new-product announcement
→ separate cash-engine and growth-engine GTM/account plans
```

### Example C

```text
company markets manufacturing process as "high precision / low cost"
+ buyer can choose forging/machining/import rather than another PM vendor
+ PM economics depend strongly on application/volume
→ build conversion-economics/RFQ tooling rather than generic awareness content
```

## Anti-hardcoding rule

The exact Sintercom conclusions above must **not** be added to the core skill as company-specific rules. The skill should rediscover equivalent insights from evidence on any suitable manufacturer.
