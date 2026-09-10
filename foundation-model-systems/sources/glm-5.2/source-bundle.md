# GLM-5.2 Source Bundle

## Canonical Sources

- blog-glm-52: https://z.ai/blog/glm-5.2
- hf-blog-glm-52: https://huggingface.co/blog/zai-org/glm-52-blog
- hf-model-card: https://huggingface.co/zai-org/GLM-5.2
- github-readme: https://github.com/zai-org/GLM-5
- glm5-tr: https://arxiv.org/abs/2602.15763
- glm5-tr-html: https://ar5iv.labs.arxiv.org/html/2602.15763
- indexshare-paper: https://arxiv.org/abs/2603.12201

## Local Files

- GLM-5.2 TR PDF: none found in initial intake.
- GLM-5 TR PDF: not downloaded for this GLM-5.2 intake; use only if later comparing lineage.

## Source Freshness

- last checked: 2026-06-22
- source status: GLM-5.2 has official blog/model card/GitHub release material; no dedicated GLM-5.2 technical report found.
- release date used in metadata: 2026-06-17, from HF blog publication date.

## Citation Labels

- Default source in this dossier is not a PDF. Use semantic source labels:
  - `[blog-glm-52]`: GLM-5.2 official release blog or HF mirror.
  - `[hf-model-card]`: HF model card / model usage / benchmark table mirror.
  - `[github-readme]`: GLM-5 repository README.
  - `[glm5-tr]`: GLM-5 TR, lineage/background only.
  - `[indexshare-paper]`: IndexShare / IndexCache paper, only if later reading architecture in depth.

## Notes

- Treat GLM-5.2 as a blog-bundle source, not a model-tr source.
- The GLM-5 TR may explain base architecture, DSA, slime, OPD, and the GLM-5 training pipeline, but those facts should not be silently promoted to GLM-5.2 unless the GLM-5.2 blog/model card explicitly says they carry over.
- This dossier emphasizes GLM-5.2 increment over GLM-5.1/GLM-5: 1M context, IndexShare/MTP serving path, long-horizon agentic RL, anti-hacking, and eval methodology.
