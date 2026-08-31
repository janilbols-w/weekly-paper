# Codex weekly editorial runbook

This project intentionally does not require an OpenAI API key. The scheduled Codex task performs the editorial step with the model available in Codex; GitHub Actions performs deterministic collection, deployment, and WeCom delivery.

Every Friday after the 12:30 Asia/Shanghai collection (the scheduled Codex run starts at 16:00 to allow for GitHub Actions queue delays):

1. Run `git pull --ff-only` and inspect `data/state/last-run.json` plus the current file in `data/weeks/`.
2. Read the abstracts and evidence for every `featured_id`. Use targeted PDF sections only when the abstract cannot support a safe conclusion; do not perform full-paper reading by default.
3. For each featured paper, fill `summary_zh`, `why_it_matters_zh`, `limitations_zh`, and `reading_depth` in its canonical `data/papers/*.json` record. Do not invent results, hardware, datasets, venue status, or code availability.
4. Keep exactly the selected Top 5 when five papers pass the quality line. If fewer qualify, do not pad the briefing with weak papers.
5. Run `python -m weekly_paper.generate`, `python -m unittest discover -s tests -v`, and `npm run build`.
6. Commit only the editorial and regenerated artifacts, then push `main`. The push deploys GitHub Pages. The notification workflow runs after a successful Pages deployment and sends only after Chinese fields and the deployed digest both match; Friday 19:00 is a fallback check.

If collection is incomplete, the website is stale, or evidence is insufficient, leave delivery blocked and report the reason instead of sending placeholders.
