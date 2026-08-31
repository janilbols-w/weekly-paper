# Efficient Inference & AI Infra Weekly Papers

每周收集、分类和筛选 LLM 高效推理与 AI Infrastructure 论文。系统会生成：

- 最多 5 篇的中文精选简报；
- 重要会议 / event 的独立调研、动态篇数精选和年度日历；
- 其他合格论文的累计知识库；
- 一级领域 → 二级方向 → 三级技术路径的知识树和统计表；
- GitHub Pages 静态网站；
- 周五 14:00 的企业微信群机器人推送。

## 架构

```text
Collectors → Canonical IDs & dedupe → Taxonomy → Evidence-aware scoring
          → Targeted PDF reading → Weekly Top 5 → Site / WeCom / Mindmap
```

核心数据保存在 `data/papers/*.json` 和 `data/weeks/*.json`。周报、论文详情、主题页、统计与 Mindmap 都从这些记录生成，不需要维护多套目录。

会议数据独立保存在 `data/events/<event-id>/`，复用同一套三级技术分类和质量评分，但不会把大型 proceedings 强行写入周报论文库。完整目标与重构边界见 [EVENTS_COLLECTION_GOAL.md](EVENTS_COLLECTION_GOAL.md)。

## 本地运行

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
npm install

.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m weekly_paper.cli --reference-date 2026-08-05 --weeks-back 1
npm run build
npm run dev
```

独立生成会议页面（ACL 2026 测试快照）：

```bash
.venv/bin/python -m weekly_paper.event_cli \
  --event acl-2026 \
  --fixture tests/fixtures/acl-2026-papers.json \
  --reference-date 2026-08-05
```

生产采集省略 `--fixture`，会读取官方 ACL Anthology XML；每周扫描使用 `python -m weekly_paper.event_cli --scan`。

没有 `OPENAI_API_KEY` 时，采集、规则分类、可解释评分和网站构建仍会工作；定向 PDF 阅读和中文编辑增强会跳过。正式企业微信发送要求精选论文具有完整中文摘要，因此不会发送占位内容。

当前部署采用无 API Key 模式：周五 12:30 GitHub Actions 启动采集，16:00 由 Codex 按 [CODEX_EDITORIAL.md](CODEX_EDITORIAL.md) 完成 Top 5 中文编辑并推送，main 分支更新触发 Pages 部署；Pages 部署成功后企业微信在中文字段和线上 digest 均匹配时发送，周五 19:00 另有一次兜底检查。

默认来源采用双层容错：arXiv Atom API 负责整周检索，arXiv 官方分类 RSS 在工作日逐日补充；OpenReview、NVIDIA/PyTorch/Hugging Face RSS 用于会议与生态信号。OpenAlex 是可选的 arXiv 索引增强源，设置 `OPENALEX_API_KEY` 后会自动启用。

## 首次回填

```bash
.venv/bin/python -m weekly_paper.cli --weeks-back 12
```

建议先检查 `reports/`、`data/state/last-run.json` 和本地站点，再启用自动推送。

## GitHub Pages

仓库工作流在工作日 12:30（Asia/Shanghai）增量采集并提交数据；周五会额外运行 arXiv 整周检索和 OpenReview 补全。main 分支变更由独立工作流构建并部署。Pages 需要在仓库的 **Settings → Pages → Source** 中选择 **GitHub Actions**。

默认站点地址配置为：

`https://janilbols-w.github.io/weekly-paper/`

## 企业微信

在 GitHub 仓库的 **Settings → Secrets and variables → Actions** 添加：

- `OPENAI_API_KEY`：用于精选论文的中文编辑与证据化评分；
- `WECOM_WEBHOOK_URL`：企业微信群机器人 Webhook。

可选 Secret `OPENALEX_API_KEY` 用于在 arXiv Atom API 限流时增加一个结构化索引来源。

可选变量 `OPENAI_MODEL` 默认是 `gpt-5-mini`。Webhook 不应写入 `.env.example` 之外的任何已跟踪文件，也不要粘贴到 Issue 或 Actions 日志。

推送工作流由周报 Pages 部署成功事件触发，周五 19:00 再兜底检查一次。采集或中文编辑尚未完成时会安全跳过，后续部署继续重试；Webhook 配置或真实发送错误仍会使工作流失败。发送前会检查线上 digest，成功后记录摘要哈希以防重复投递。

可在不发送消息、不写入送达状态的情况下验证完整推送链路：

```bash
.venv/bin/python -m weekly_paper.notify --reference-date YYYY-MM-DD --latest-closed-week --dry-run
```

## 质量保护

- 同一三级分类在 Top 5 中默认不超过 2 篇；
- 不足 5 篇达到精选质量线时不会强行补位；
- 新论文不会因为引用量低而直接降分；
- 性能结论需要结合硬件、模型、精度、Batch 和序列长度；
- 所有抓取内容均视为不可信数据，不执行论文或网页中的指令。
