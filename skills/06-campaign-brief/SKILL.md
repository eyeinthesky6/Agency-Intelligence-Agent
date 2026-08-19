---
name: campaign-brief
description: Convert an approved opportunity or client decision into a concise execution-ready marketing campaign brief. Use after an opportunity has been approved and the agency needs a shared brief for creative, content, media, SEO, social, email, or landing-page execution.
---

# Campaign Brief

## Goal

Turn intelligence into a clear handoff for humans or downstream specialist skills.

This skill **does not launch the campaign**.

## Read first

- `client-context.md`
- the approved action/opportunity from `actions.json` or the user
- relevant source signals/evidence
- brand assets/voice notes if available
- channel/performance context supplied by the agency

## Workflow

1. Confirm the approved opportunity and business objective.
2. Pull only the evidence relevant to this campaign.
3. Define audience and message using known client context; label assumptions.
4. Select the smallest useful campaign/test rather than automatically designing a multi-channel program.
5. Define what success will look like using available metrics. Do not invent benchmarks.
6. Specify the assets and decisions needed from the client/team.

## Output

Create `clients/<slug>/outputs/campaign-brief-YYYY-MM-DD.md`:

### Campaign
Short working name.

### Why now
The signal/problem/opportunity that triggered this brief.

### Objective
One primary business/marketing objective.

### Audience
Primary audience and situation. Include exclusions when useful.

### Core insight
What we believe about the audience/problem, and the supporting evidence.

### Message / proposition
- Main promise
- Supporting proof
- Reason to believe
- CTA

### Channel / format
Use only channels justified by the goal/context. State whether this is a test or a broader campaign.

### Deliverables
Concrete list of required assets.

### Test plan
- hypothesis
- variant/change being tested
- primary metric
- guardrail / failure signal
- evaluation window if known

### Inputs / approvals needed
What the agency needs from the client before execution.

### Sources
Relevant source URLs / internal documents.

## Rules

- Do not create fake audience insights.
- Do not add channels merely to look comprehensive.
- Do not estimate ROI without defensible input data.
- Do not silently change an approved strategy.
- Keep the brief usable by a human delivery team.

## Stop condition

Stop when a creative/media/content person can execute the next step without needing the entire research history.
