---
name: client-onboard
description: Create or refresh the durable client context used by every Agency Intelligence skill. Use when onboarding a new client/prospect, when the agent lacks business context, or when major positioning/goals/campaign information has changed.
---

# Client Onboard

## Goal

Create a compact, trustworthy `clients/<slug>/client-context.md` so later skills do not repeatedly ask the agency to explain the client.

## Inputs

Use whatever is available:

- client/prospect name and website
- proposal / scope of work
- brand or product deck
- previous reports
- strategy notes
- Drive/client-folder documents
- campaign notes
- competitor list
- user corrections

Do **not** require every input before starting.

## Workflow

1. Inspect available client files and URLs before asking questions.
2. Extract only useful durable context: what the company sells, to whom, why customers choose it, proof, competitors, brand/voice, goals, active work, metrics, constraints.
3. When public web research materially improves missing context, use at most 3 focused searches.
4. Separate:
   - `Known` — supported by client material or authoritative public source.
   - `Assumption` — plausible but not verified.
   - `Unknown` — genuinely missing.
5. Prefer the client's/customer's own language over invented marketing copy.
6. Keep the document concise enough that another skill can read it quickly.
7. Save/refresh `clients/<slug>/client-context.md` using the repository template.

## Required sections

- Company snapshot
- Offer / products / services
- Target audience / ICP
- Buyer and user roles (if relevant)
- Customer problems / jobs
- Positioning / value proposition
- Proof points
- Competitors and alternatives
- Brand voice / language
- Business and marketing goals
- Known metrics
- Current campaigns / agency scope
- Constraints / exclusions
- Open questions
- Sources
- Last updated

## Quality gate

Before finishing:

- No invented customer quotes, metrics, pricing, or claims.
- Important assumptions are visibly labelled.
- Named competitors are real or explicitly provided by the user.
- The context says what the agency is trying to achieve, not only what the client company does.
- The file is useful even if some sections remain `Unknown`.

## Stop condition

Stop when the context is good enough for another skill to make a client-specific recommendation. Do not turn onboarding into a market-research project.
