# Codex weekly editorial runbook

This project intentionally does not require an OpenAI API key. The scheduled Codex task performs the editorial step with the model available in Codex; GitHub Actions performs deterministic collection, deployment, and WeCom delivery.

Every Friday after the 12:30 Asia/Shanghai collection (the scheduled Codex run starts at 16:00 to allow for GitHub Actions queue delays):

1. Start from `main` with a clean worktree. Fetch `origin/main`; fast-forward when only behind, or rebase unpushed local commits onto `origin/main` when the clean branch has diverged. Never reset or discard user changes. Push and verify `HEAD == origin/main` before editorial work so an unrelated pending commit cannot be stranded by a later editorial gate.
2. Inspect `data/state/last-run.json` plus the current file in `data/weeks/`. A missing or stale edition, empty `featured_ids`, missing canonical records, a core-source failure, or insufficient paper evidence blocks editorial publication. An HTTP 403 from auxiliary OpenReview conference sources is a warning rather than a blocker when the current arXiv-backed edition, selected records, and editorial evidence are complete.
3. Read the abstracts and evidence for every `featured_id`. Use targeted PDF sections only when the abstract cannot support a safe conclusion; do not perform full-paper reading by default.
4. For each featured paper, fill `summary_zh`, `why_it_matters_zh`, `limitations_zh`, and `reading_depth` in its canonical `data/papers/*.json` record. Do not invent results, hardware, datasets, venue status, or code availability.
5. Keep exactly the selected Top 5 when five papers pass the quality line. If fewer qualify, do not pad the briefing with weak papers.
6. Run `python -m weekly_paper.generate`, `python -m unittest discover -s tests -v`, and `npm run build`.
7. Commit only the editorial and regenerated artifacts. Fetch again before the final push; if the remote advanced, rebase the clean local commits onto the latest `origin/main`. Retry a non-fast-forward push after fetching and rebasing, then fetch once more and verify `HEAD == origin/main`. Always run `git push origin main`, even when there is no new commit; never create an empty commit merely to force activity.

The push is a required acceptance check, independent of whether editorial publication proceeds. Authentication failures, network failures, dirty worktrees, and rebase conflicts must be reported as failed runs rather than hidden; external infrastructure can still prevent a guaranteed push. A successful push deploys GitHub Pages. The notification workflow runs after a successful deployment and sends only after Chinese fields and the deployed digest both match; Friday 19:00 is a fallback check.

If a hard editorial gate fails, leave delivery blocked and report the reason instead of sending placeholders, but still push and verify any already-committed local work when it is safe to do so.
