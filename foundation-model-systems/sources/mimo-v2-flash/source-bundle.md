# MiMo-V2-Flash Source Bundle

## Canonical Sources

- tech-report: https://arxiv.org/abs/2601.02780
- tech-report-pdf: https://arxiv.org/pdf/2601.02780
- github: https://github.com/XiaomiMiMo/MiMo-V2-Flash
- github-paper-pdf: https://github.com/XiaomiMiMo/MiMo-V2-Flash/blob/main/paper.pdf
- blog-v2-flash: https://mimo.xiaomi.com/blog/mimo-v2-flash
- hf-paper: https://huggingface.co/papers/2601.02780
- hf-model-card: https://huggingface.co/XiaomiMiMo/MiMo-V2-Flash
- v2.5-blog: https://mimo.xiaomi.com/mimo-v2-5/
- v2.5-pro-blog: https://mimo.xiaomi.com/mimo-v2-5-pro/

## Local Files

- TR PDF: `/Users/chy/Research/foundation-model-systems/papers/mimo-v2-flash/mimo-v2-flash-tech-report.pdf` (31 pages, downloaded 2026-06-22)

## Source Freshness

- last checked: 2026-06-22
- source status: MiMo-V2-Flash has a full TR on arXiv; MiMo-V2.5 and MiMo-V2.5-Pro have release/blog/model-card material, but no full TR found in this pass.
- latest TR-backed source in the MiMo text-model lineage for OPD/MOPD study: MiMo-V2-Flash Technical Report.

## Citation Labels

- Default source in stage notes: `tech-report`, cited as page-only anchors like `[18]`.
- Non-default labels, only when actually cited: `[blog-v2-flash]`, `[hf-model-card]`, `[v2.5-blog]`, `[v2.5-pro-blog]`, `[github]`.

## Notes

- Treat V2-Flash as the full-TR anchor for MOPD.
- Treat V2.5 / V2.5-Pro as release deltas unless a later dedicated TR appears.
- V2.5-Pro blog says it is Xiaomi's most capable model and has 1.02T total / 42B active parameters with 1M context, but without a TR it should not be used as the source for MOPD formula or training-recipe details.
