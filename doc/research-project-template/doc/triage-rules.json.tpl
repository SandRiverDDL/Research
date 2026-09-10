{
  "description": "<PROJECT_TITLE> project-local triage rules.",
  "hard_gates": [
    "Queue row is not a card.",
    "Survey mention is recall evidence, not paper evidence.",
    "No original paper PDF/HTML brief, no formal L1 card.",
    "Formal L1 cards in notes/ root must pass scripts/autoresearch.py validate before being reported as complete."
  ],
  "required_frontmatter": [
    "title",
    "year",
    "venue",
    "paper_type",
    "lifecycle_role"
  ],
  "required_nested_frontmatter": {},
  "allowed": {
    "paper_type": [
      "core-method",
      "survey",
      "benchmark-eval",
      "background",
      "adjacent"
    ],
    "lifecycle_role": [
      "survey-seed",
      "canonical-anchor",
      "strong-baseline",
      "frontier-candidate",
      "background",
      "low-confidence-novelty-risk"
    ],
    "boundary_risk": [
      "none",
      "adjacent",
      "eval",
      "recipe",
      "infra"
    ]
  },
  "select_rules": [
    "<SELECT_RULE_1>",
    "<SELECT_RULE_2>"
  ],
  "maybe_rules": [
    "<MAYBE_RULE_1>"
  ],
  "move_elsewhere_rules": [
    "<MOVE_ELSEWHERE_RULE_1>"
  ],
  "overrides": {
    "select": {},
    "maybe": {},
    "skip": {}
  }
}
