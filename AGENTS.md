# AGENTS.md — Agency Intelligence Agent

## Mission

Build the smallest useful intelligence assistant for agencies.

The product helps an agency become better prepared, faster: understand a client, research a prospect, uncover non-obvious commercial insights, investigate product/market/pricing/competitor moves, prepare meetings, recommend a few actions, and package the result into familiar client-ready artifacts.

## Prime directive

**Do not make this project more sophisticated unless a real user problem requires it.**

When choosing between:

- prompt/skill vs service → choose prompt/skill
- markdown/JSON vs database → choose markdown/JSON
- host-provided web search vs custom crawler → choose host-provided search
- one agent with tools vs agent swarm → choose one agent
- deterministic script vs another LLM call → choose deterministic script
- explicit user approval vs autonomous execution → choose user approval
- understandable artifact vs impressive architecture → choose artifact

## Product contract

Every workflow should follow:

```text
CONTEXT → QUESTION → PLAN → RESEARCH → EVIDENCE → SYNTHESIS → ACTION → ARTIFACT
```

A useful result must answer:

1. What did we learn?
2. What evidence supports it?
3. What **new conclusion follows from combining the evidence**?
4. Why does it matter to this specific client/prospect?
5. What should the agency/company do next?
6. What must management verify before acting?
7. What can be handed to a human/client?

## Non-goals for v0

Do not add any of these unless the user explicitly changes scope:

- database
- vector database
- embeddings pipeline
- web app/dashboard
- authentication
- queues/workers
- Redis
- Docker requirement
- LangGraph/CrewAI/AutoGen or another orchestration framework
- custom browser automation
- always-on crawler
- social/ad execution APIs
- autonomous outbound
- multi-agent personas
- long-term semantic memory infrastructure

## Memory

The source of truth for a client is:

```text
clients/<slug>/client-context.md
clients/<slug>/signals.jsonl
clients/<slug>/actions.json
clients/<slug>/outputs/
```

Never invent missing client facts. Mark them `Unknown` or `Assumption`.

A public-source claim must retain its source URL and observation date.

## Research discipline

### Search less, synthesize better

Default research budget for a normal run:

- named competitors: maximum 5 unless the user asks for more
- sources per important claim: target 2 when practical
- focused market/category searches: maximum 5 before re-planning
- recommendations: maximum 3 primary actions for normal workflow; DEEP competitive mode may return up to 5

A DEEP investigation may exceed these budgets when new sources are materially changing the thesis, but source count is never a quality metric.

Stop when additional sources repeat the same commercial story.

### Search snippets are not insights

A deep insight must normally combine **two or more pieces of evidence**.

Use this structure:

```text
Evidence A
+ Evidence B
(+ Evidence C if useful)
→ Inference
→ Commercial implication
→ What would falsify / verify it
```

Example:

```text
Large new order relative to revenue
+ already-stretched inventory/receivable cycle
→ growth may create a financing constraint
→ price working capital / volume / inventory terms into the contract
→ verify actual payment, forecast and safety-stock terms
```

Do not disguise a public fact as a proprietary insight.

### Prefer deltas for recurring research

For recurring intelligence, compare against existing signals/context and report **what changed**. Do not repeatedly generate generic competitor profiles.

### Fact → Impact → Act

For important intelligence use:

- **Fact:** verifiable observation
- **Impact:** why it matters to this client, campaign, product, pitch, contract, or deal
- **Act:** a specific recommended next move

If there is no credible Impact, it is probably noise.
If there is no justified Act, do not manufacture one.

### Confidence

Use only:

- `high` — directly verified from an authoritative/current source
- `medium` — credible but indirect or only one reasonable source
- `low` — inference, ambiguous, stale, or weakly sourced

Never convert a competitor's marketing claim into a verified product fact without saying it is a claim.

## Industrial / B2B rule

For manufacturing and B2B companies, do not default to consumer-marketing advice.

Explicitly examine where relevant:

- revenue/margin/cash economics
- order/customer concentration
- capacity and utilization
- legacy vs emerging product families
- process substitutes (machining, forging, casting, import, in-house, etc.)
- qualification / switching costs
- application engineering
- distribution / direct OEM / Tier-1 / dealer / export channels
- pricing architecture and commercial terms
- tooling/NRE
- raw-material/FX pass-through
- inventory / receivables / payment terms
- localization / import substitution
- certifications and technical proof

Marketing recommendations should reduce sales friction, create qualified applications, expand accounts or improve pricing power.

Good industrial marketing assets include:

- technical case studies
- application landing pages
- conversion / TCO calculators
- RFQ qualification tools
- design guides
- localization/import-substitution proof
- account battlecards
- prototype/sample programs
- target-account campaigns

A content calendar is not a strategy by default.

## Pricing discipline

Never guess a private/custom industrial price merely because the user asked for pricing.

If list prices do not exist, build:

- customer economic alternative
- seller cost-to-serve
- tooling/NRE economics
- volume assumptions
- working-capital burden
- contract-term risks
- pricing corridor
- negotiation architecture

Separate exact facts from scenarios.

## Tool policy

Use tools already available in the host environment first:

- web search / URL fetch
- connected Drive / file tools
- spreadsheets / slides tooling
- Python for deterministic transforms

Adapter code belongs behind a tiny interface and is optional. Core skills must remain usable without a specific vendor.

## Execution boundary

v0 may **recommend and draft**.

v0 must not automatically:

- spend money
- launch/pause ads
- publish content
- send outbound emails/messages
- modify CRM records
- make irreversible client changes

The human approves execution.

## Artifact policy

Canonical outputs are Markdown/JSON because they are portable and inspectable.

Optional renderers may create:

- `.csv` action/signal/review tables that open in Excel/Google Sheets
- `.pptx` short client review/pitch decks

A host with native spreadsheet support may create richer `.xlsx` files from the same canonical JSON.

Keep decks short. Default: 6 slides.
Keep spreadsheets decision-oriented. Avoid decorative complexity.

## Skill design

Each skill should have:

1. clear trigger/use case
2. inputs it expects
3. files/context it should read first
4. finite workflow
5. required evidence discipline
6. exact output schema/location
7. quality gate
8. explicit stop condition

Do not create a new skill if an existing skill can absorb the use case with one small section.

## Quality gate

Before considering a run complete:

- Does every important external claim have a source?
- Did we separate facts from inference?
- For DEEP work, did we actually synthesize multiple facts into non-obvious conclusions?
- Is the output specific to the client's economics, product and buying process?
- Did we avoid generic marketing advice?
- Did we consider substitutes/status quo, not only named rivals?
- If pricing matters, did we address contract/cash economics rather than fake list prices?
- Are recommendations few and executable?
- Did we state what management needs to verify?
- Is there a usable artifact?

If yes, stop. Do not polish indefinitely.
