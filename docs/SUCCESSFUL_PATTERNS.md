# Successful Agent Patterns We Are Reusing

This project is intentionally conservative: copy patterns that have already produced adoption, strong benchmark results, or clear commercial traction; reject complexity that does not improve the agency's output.

> This document paraphrases public product/repository patterns. It does not copy third-party skill text.

## 1. Claygent — bounded GTM research at scale

**Evidence of adoption:** Clay reported in June 2025 that Claygent had surpassed **1 billion runs**. Clay's current product positions agents around judgment-based GTM tasks such as account research, lead scoring, signal detection, and outbound preparation.

Sources:
- https://www.clay.com/blog/claygent-1-billion
- https://www.clay.com/claygent
- https://university.clay.com/docs/claygent-builder

### Pattern worth copying

- give the agent a concrete record/account/context
- ask one bounded research question
- return structured fields, not a rambling essay
- retain visibility into why the result was produced
- test prompts on real examples before scaling them
- reuse a working agent definition across many accounts

### Agency Intelligence translation

A client is our persistent account context. Each skill should do one legible job against that context and return structured, sourceable output.

**Use:** prospect research, account/client intelligence, competitor signals.

**Do not copy:** Clay's massive data-vendor ecosystem or enrichment infrastructure. We do not need it for v0.

---

## 2. GPT Researcher — question to sourced report

**Evidence of adoption:** the open-source repository has tens of thousands of GitHub stars and thousands of forks.

Sources:
- https://github.com/assafelovic/gpt-researcher
- https://github.com/assafelovic/gpt-researcher/blob/main/docs/docs/gpt-researcher/getting-started/introduction.md

### Pattern worth copying

- start with a specific research goal
- decompose into focused sub-questions
- search multiple sources rather than trusting one page
- synthesize evidence into a final artifact
- preserve citations/source links
- optimize for a report somebody can actually use

### Agency Intelligence translation

Every research-heavy skill should create a small research plan, gather enough evidence, then stop and synthesize.

**Use:** prospect intelligence, competitor research, market context.

**Do not copy:** deep-research breadth by default. Agencies usually need a decision brief, not a 30-page dossier.

---

## 3. LangChain Open Deep Research — pipeline stages beat one giant prompt

**Evidence of quality:** the project reported a #6 position on Deep Research Bench in August 2025 and remains a widely forked reference implementation.

Source:
- https://github.com/langchain-ai/open_deep_research

### Pattern worth copying

The implementation separates concerns such as:

- research/search
- summarization
- compression
- final report generation

This is useful because raw research is noisy. A compression step before the final artifact forces the system to keep signal rather than dump context.

### Agency Intelligence translation

Use a simple conceptual pipeline:

```text
collect → normalize → rank → compress → recommend → render
```

These are **stages**, not separate role-playing agents.

**Do not copy:** LangGraph/runtime infrastructure for v0. The host agent can execute the stages sequentially.

---

## 4. Browser Use — tool boundary, bounded actions, recovery

**Evidence of adoption:** Browser Use has roughly one hundred thousand GitHub stars and an active hosted product.

Sources:
- https://github.com/browser-use/browser-use
- https://github.com/browser-use/browser-use/blob/main/AGENTS.md

### Pattern worth copying

- expose a clear tool/action boundary to the model
- keep task input/output typed/structured where possible
- cap action counts
- maintain state across steps
- recover from failed actions instead of restarting the entire task
- evaluate realistic tasks, not only unit functions

### Agency Intelligence translation

If/when we add a browser adapter, it must be optional and bounded. A competitor scan should have a page/query budget and terminate cleanly.

**Do not copy:** browser infrastructure now. Existing host browsing/search is sufficient for validation.

---

## 5. GTM Co-Founder — persistent context + small skills

**Evidence of product traction:** its repository describes the project as a Product Hunt #1 Product of the Day and distributes a portable set of Agent Skills for GTM work.

Source:
- https://github.com/AIDevGTM/gtm-cofounder

### Pattern worth copying

- gather company context once
- save it in a durable markdown brief
- make every downstream skill read the brief first
- sequence skills around real decisions
- for recurring market scans, report **deltas**, not generic descriptions
- connect meaningful market changes to a specific action

### Agency Intelligence translation

`client-context.md` is the foundation of the project. The agency should not repeatedly explain the same client.

**Use:** every skill.

**Do not copy:** dev-tool-specific GTM assumptions.

---

## 6. Gumloop AI Web Research — prompt → schema → sourced file

Gumloop's current AI Web Research workflow generates structured inputs/outputs from a research prompt and returns citations; its example research agents deliver tables/CSV rather than only chat text.

Sources:
- https://docs.gumloop.com/nodes/using_ai/ai_web_research
- https://www.gumloop.com/use-cases/ai-web-scraping-agent

### Pattern worth copying

- define expected output fields before the run
- return sources with facts
- expose uncertainty/confidence
- deliver files/tables when a workflow will consume the result

### Agency Intelligence translation

Signals are structured JSONL. Client actions are structured JSON. XLSX/PPTX are renderings of those canonical structures.

---

## 7. Pomo — competitive signals become marketing actions

Pomo is a useful market validation reference because it combines brand/competitor monitoring with actionable marketing recommendations and campaign briefs. In April 2026, Business Insider reported a **$4.5M seed round** for the company.

Sources:
- https://usepomo.ai/
- https://www.businessinsider.com/pitch-pomo-deck-ai-startup-fundraise-marketing-platform-2026-4

### Pattern worth copying

```text
external signal → relevance to brand → recommended marketing action
```

That is the bridge between "research tool" and "agency intelligence."

### Agency Intelligence translation

Do this without execution APIs first. We can recommend and draft; humans decide and execute.

---

# The composite pattern for this repo

The reusable architecture is:

```text
CLIENT CONTEXT
      ↓
BOUNDED QUESTION / SKILL
      ↓
SMALL RESEARCH PLAN
      ↓
WEB + CLIENT SOURCES
      ↓
STRUCTURED FACTS + SOURCES
      ↓
COMPRESS / RANK
      ↓
FACT → IMPACT → ACT
      ↓
MARKDOWN / JSON SOURCE OF TRUTH
      ↓
PPTX / XLSX WHEN USEFUL
```

## Things successful systems often have that we are deliberately postponing

These can be valuable at scale but are not prerequisites for proving this product:

- browser fleets
- vector stores
- workflow orchestration servers
- deep CRM integrations
- custom enrichment networks
- automatic campaign execution
- observability platforms
- queues / retries infrastructure
- dashboards
- multi-agent supervisors

## V0 design tests

Before adding infrastructure, ask:

1. Did an agency user fail because this capability was missing?
2. Did the failure happen more than once?
3. Would fixing it increase willingness to pay or materially reduce manual work?
4. Can the problem be solved more simply inside a skill or deterministic script?

If the answers are not convincing, do not build it.
