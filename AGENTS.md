# AGENTS.md — Agency Intelligence Agent

## Mission

Build the smallest useful intelligence assistant for agencies.

The product helps an agency become better prepared, faster: understand a client, research a prospect, notice meaningful competitor changes, prepare meetings, recommend a few actions, and package the result into familiar client-ready artifacts.

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
CONTEXT → PLAN → RESEARCH → EVIDENCE → INTERPRET → ACTION → ARTIFACT
```

A useful result must answer:

1. What did we learn?
2. What evidence supports it?
3. Why does it matter to this specific client/prospect?
4. What should the agency do next?
5. What can be handed to a human/client?

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

### Search less, decide better

Default research budget for one skill run:

- named competitors: maximum 5 unless the user asks for more
- sources per important claim: target 2 when practical
- new market/category searches: maximum 5 focused queries
- recommendations: maximum 3 primary actions

Stop researching when additional sources are repeating the same conclusion.

### Prefer deltas

For recurring intelligence, compare against existing signals/context and report **what changed**. Do not repeatedly generate generic competitor profiles.

### Fact → Impact → Act

For important intelligence use:

- **Fact:** verifiable observation
- **Impact:** why it matters to this client, campaign, pitch, or deal
- **Act:** a specific recommended next move

If there is no credible Impact, it is probably noise.
If there is no justified Act, do not manufacture one.

### Confidence

Use only:

- `high` — directly verified from an authoritative/current source
- `medium` — credible but indirect or only one reasonable source
- `low` — inference, ambiguous, stale, or weakly sourced

Never convert a competitor's marketing claim into a verified product fact without saying it is a claim.

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

- `.xlsx` action/signal tracker
- `.pptx` short client review/pitch deck

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
- Is the output specific to the client/prospect?
- Did we avoid generic marketing advice?
- Are recommendations few and executable?
- Is there a usable artifact?
- Would an account manager understand it in under five minutes?

If yes, stop. Do not polish indefinitely.
