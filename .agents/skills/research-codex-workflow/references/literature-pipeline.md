# Literature Pipeline

Use this for literature discovery, survey processing, batch paper cards, queue repair, source briefs, and validator issues.

## Default Flow

```text
queue/search -> lookup/audit -> bounded source brief -> Codex judgment -> card/report -> validate
```

Natural-language user requests should map to project-local tools internally. Users should not need to remember script names or generated artifact paths.

## Card Gates

- Queue row is not a card.
- Survey mention is recall evidence, not paper evidence.
- Do not write a formal L1 card from survey text alone.
- A formal L1 card needs original-paper evidence: PDF, HTML, source markdown, or a bounded paper brief derived from the original paper.
- Old card content is reference material, not authority.
- If historical survey-only cards or notes are discovered, treat them as invalid legacy artifacts: move them out of the formal notes set or mark them invalid, and do not count them as official cards.

## Scripts

Use project-local scripts only as mechanical helpers:

- `status`: count queue, cards, briefs, PDFs, validation issues
- `lookup`: check whether a paper already exists in queue/card/brief/PDF
- `audit`: find mechanical gaps and duplicates
- `pack`: prepare bounded inputs for the next few candidates
- `validate`: hygiene checks before reporting completion

Do not encode research judgment in validators: importance, paper type, method family, novelty risk, failure-mode quality, and idea value remain Codex/user judgments.

## Discovery and Triage

Default to high-precision recall before broad systematic search:

- known-item recovery
- exact arXiv/OpenReview/venue queries
- cross-reference grep over existing cards/briefs
- cutoff-after-survey checks when a seed survey is used

Queue broadly enough to avoid losing candidates. Write cards only when the paper has enough original evidence and the project-local criteria justify it.

Suggested triage language:

- S/A: direct competitor, strong baseline, method anchor, or high novelty-risk
- B: relevant background or future queue
- C/off-scope: record exclusion if it may be rediscovered later

Project-specific venue/code rules, taxonomies, and decision axes belong in project docs, not this skill.

## Writing L1 Cards

Write cards in small batches, usually 1-3 at a time unless the project has a mature pack/validate loop.

Preserve information the researcher reuses:

- one-line claim
- core method and mechanism
- actual innovation
- decision axes or design choices
- solved failure mode
- lineage, baselines, and alternatives
- evaluation signal that matters for research judgment
- source anchors

Avoid long experiment setup prose unless it changes the research decision. Put reproduction details and subjective verdicts in L2 notes or comparison files.

## Validation

Run the project validator before reporting batch work as complete. Report the important counts when relevant: queue, valid cards, original-paper briefs/evidence, invalid legacy notes, and validation errors.

If no project-local automation exists, do not invent a heavy pipeline immediately. For small tasks, write 1-3 source-backed cards manually; for larger projects, first add a minimal helper scaffold.
