# Experiment Design

Use this for experiment planning, run records, result interpretation, and paper-story iteration.

## Design Standard

Do not claim improvement without:

- a clear hypothesis
- a fair baseline
- a meaningful metric
- at least one ablation or control that isolates the mechanism
- a known failure mode the experiment can falsify

Prefer the smallest clean experiment that answers the question before running a broad sweep.

## Run Record

For projects that run experiments, record:

```text
experiments/<project>/runs/YYYYMMDD_HHMM_<slug>/
  config.yaml
  command.txt
  git_commit.txt
  stdout.log
  stderr.log
  metrics.json
  notes.md
```

`notes.md` should answer:

```markdown
# Run Notes

## Purpose

## Expected Outcome

## Result

## Interpretation

## Problems

## Next Minimal Experiment
```

## Result Interpretation

After each run, answer:

- Is the result trustworthy?
- Did it answer the hypothesis?
- What is the next minimal experiment?

If the result is noisy or under-instrumented, say that before drawing research conclusions.
