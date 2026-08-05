# Conference / Event Collection Goal

## 1. 需求重述

在现有「LLM 高效推理与 AI Infra 每周论文」流程之外，增加一条**会议与行业活动驱动的独立调研流程**：

1. 每周检查重要的 LLM、机器学习系统、体系结构与基础设施会议、meeting 和 event，确认当周是否处于会议举行、议程发布、录用列表发布或奖项发布等值得跟踪的时间点。
2. 命中条件后，为该会议或活动创建独立调研任务，不把它混入普通周报 Top 5 的固定名额。
3. 对论文型会议，收录官方论文全集或与本站主题相关的完整子集，复用现有三级分类和可解释评分；另建「精选论文」页面，篇数由质量阈值和主题多样性决定，不硬凑固定数量。
4. 对非论文型 meeting/event，记录议程、主题、重要演讲、发布内容与工程启示，并保留官方来源和核验时间。
5. 所有事件页面进入统一会议索引和知识入口，并可从周报、三级主题页和论文详情交叉跳转。
6. 第一个回填测试为 **ACL 2026**。

本文中的 Conference 对应需求原文里的 “confluence”，实现与页面中统一使用“会议 / Conference”。

## 2. 范围与原则

### 2.1 首期关注范围

- NLP / LLM：ACL、EMNLP、NAACL、COLM。
- 通用 ML：NeurIPS、ICML、ICLR。
- ML Systems：MLSys。
- 系统与基础设施：SOSP、OSDI、NSDI、EuroSys、FAST。
- 体系结构与并行计算：ASPLOS、ISCA、HPCA、PPoPP。
- 重要活动：上述会议的官方 workshop/tutorial/keynote，以及 NVIDIA GTC、PyTorch Conference 等具备明确 LLM/AI Infra 技术议程的活动。

会议清单使用配置文件管理，可扩展，不把名称和年份写死在采集代码中。

### 2.2 来源优先级

按以下顺序核验，每个核心事实尽量由官方来源支持：

1. 会议官网、官方 CFP、program、accepted papers / proceedings、award 页面。
2. ACL Anthology、OpenReview、PMLR、USENIX、ACM DL、IEEE Xplore 等正式论文库。
3. 主办方或研究机构官方博客、演讲视频与 slides。
4. arXiv、作者项目页与代码仓库，用于补充摘要、版本、artifact 和复现信息。
5. 高质量科技媒体只作为发现信号或背景信息，不作为录用、奖项和性能结论的唯一依据。

### 2.3 非目标

- 首期不把所有会议论文强行合并进现有全局 `data/papers/`，避免破坏周报的去重和时间语义。
- 不因会议名气直接判定单篇论文质量。
- 不对每篇论文做全文精读；只有进入精选候选的论文才升级阅读深度。
- GitHub Actions 不依赖 `OPENAI_API_KEY`；规则采集与评分必须可重复运行。

## 3. 事件三级分类

事件本身采用三级分类，与论文技术分类并行：

| 一级：领域 | 二级：社区 | 三级：活动类型 |
|---|---|---|
| LLM / NLP | ACL Family、COLM | Conference、Workshop、Tutorial、Keynote |
| Machine Learning | NeurIPS、ICML、ICLR | Conference、Workshop、Expo |
| ML Systems | MLSys | Conference、Workshop、Artifact |
| Systems | USENIX、ACM SIGOPS、EuroSys | Conference、Workshop、Industry Track |
| Architecture / HPC | SIGARCH、IEEE TCCA、SIGPLAN | Conference、Workshop、Artifact |
| Industry | NVIDIA、PyTorch 等 | Summit、Developer Conference、Release Event |

论文继续使用现有的「一级领域 → 二级方向 → 三级技术路径」分类。一个事件可覆盖多个技术叶子；事件页展示技术分布和精选论文，而不是另造一套论文 taxonomy。

## 4. 每周触发与状态机

每周事件扫描采用“固定 watchlist + 官方页面核验”，不进行无边界的全网爬取。

### 4.1 触发点

- `announced`：日期、地点或 CFP 首次确认。
- `papers_released`：录用列表或 proceedings 首次公开。
- `program_released`：议程、tutorial、workshop 或 keynote 首次公开。
- `event_week`：活动开始日前 3 天至结束日后 3 天。
- `awards_released`：best paper / distinguished paper 等结果公开。
- `manual_backfill`：手动指定历史事件，例如 ACL 2026。

### 4.2 去重

`event_id + trigger_type + source_digest` 构成执行键，记录到事件状态文件。只有来源内容或状态发生变化才重新生成，防止每周重复提交相同页面。

### 4.3 独立任务

事件调研使用独立 CLI 与 GitHub Actions job；周报流程只读取已完成事件的简短引用。这样单个大型会议抓取失败不会阻塞普通周报。

## 5. 论文采集、筛选与评分

### 5.1 漏斗

```text
官方论文全集
  → 标题/摘要主题召回
  → 现有三级分类（仅保留 LLM efficient inference / AI Infra）
  → 元数据质量评分
  → 高分候选的摘要、PDF 关键段和 artifact 定向核验
  → 动态阈值精选 + 主题去重
  → 独立会议页面
```

### 5.2 质量评分（100 分）

复用现有六维评分并补充会议证据：

- 主题相关性 25：与 LLM 推理效率或 AI Infra 的直接程度。
- 方法新颖性 15：是否提出新机制、系统或可推广洞见。
- 实验严谨性 20：基线、消融、工作负载、硬件和可比性是否充分。
- 工程影响 20：吞吐、时延、显存、成本、能耗、可靠性或可扩展性收益。
- 可复现性 10：代码、artifact、数据、配置及 artifact evaluation。
- 可信度 10：正式录用、oral/spotlight、奖项、证据完整性；会议声望只作为弱信号。

会议标签（oral、award、artifact）必须来自官方页面，并作为可解释证据展示。精选采用质量阈值，不设固定篇数；同时限制同一三级技术路径的重复占位。

### 5.3 高效阅读策略

- 全集阶段只读标题、摘要、track、作者和官方标签。
- 候选阶段读取 PDF 首页、方法概览、关键结果表、限制和 artifact 链接。
- 只有性能结论不清楚、评分接近阈值或进入最终精选时才进一步阅读正文。
- 摘要中区分“作者声称”和“已核验事实”；缺失硬件、模型、精度、batch 或序列长度时降低结论置信度。

## 6. 数据与页面结构

首期采用与周报松耦合的事件存储：

```text
config/events.yaml                    # 会议 watchlist 与触发策略
data/events/index.json                # 事件索引
data/events/<event-id>/event.json     # 官方事实、状态、来源与摘要
data/events/<event-id>/papers.json    # 相关论文全集、评分与精选标记
data/state/event-runs.json            # 执行去重状态
reports/events/<event-id>.md          # 可审阅的研究报告
src/content/docs/events/index.md      # 会议日历/统一入口
src/content/docs/events/<event-id>.md # 单次会议精选页
src/data/events.json                  # 页面结构化数据
```

事件页面信息顺序：

1. 会议状态卡：日期、地点、类型、官方链接、数据更新时间。
2. 一分钟结论：为何值得关注、与 LLM 推理 / AI Infra 的关系。
3. 关键议程：keynote、tutorial、workshop、奖项或重要发布。
4. 精选论文：中文一句话摘要、工程价值、评分、证据、限制和原文链接。
5. 全部相关论文：可搜索表格，按三级分类、track、评分筛选。
6. 技术分布：会议论文在现有三级知识树中的计数，并链接到全局主题页。
7. 来源与方法：官方来源、采集时间、覆盖范围和已知缺口。

## 7. 实现阶段

### Phase A — 最小闭环（本次）

- 新增事件配置、数据模型、ACL Anthology / 官方 accepted-papers 采集器。
- 新增事件 CLI，支持 `--event acl-2026` 手动回填。
- 复用现有 taxonomy 和评分，增加会议证据与动态精选。
- 生成会议索引、ACL 2026 独立精选页面和研究报告。
- 添加测试并验证 Astro 构建。

### Phase B — 每周自动发现

- 按官方日历扫描生命周期状态，写入 `event-runs.json`。
- 新增独立 GitHub Actions workflow 和 Codex 编辑任务。
- 周报首页显示“本周会议 / 活动”，企业微信在有事件时附加入口。

### Phase C — 体系化增强

- 增加交互式会议日历、年度视图、跨会议技术趋势和论文交叉引用。
- 支持更多 proceedings 适配器（OpenReview、PMLR、USENIX、ACM/IEEE）。
- 对奖项、oral、artifact 与代码可用性做持续更新。

## 8. ACL 2026 验收用例

- 官方确认会议名称、日期、地点、议程阶段和 proceedings 来源。
- 抓取 ACL 2026 正式论文元数据，记录覆盖范围与总量。
- 找出与 LLM efficient inference / AI Infra 直接相关的论文并完成三级分类。
- 根据质量阈值生成不限篇数的精选列表，提供中文摘要、工程价值、评分证据与限制。
- 生成 `/events/` 索引和 `/events/acl-2026/` 页面，并通过单元测试与 `npm run build`。
- 页面上的事实和论文链接可回溯到官方来源。

## 9. 需要暂停沟通的重大重构边界

以下情况不在本次默认授权的增量实现范围内，出现时暂停并征求反馈：

- 需要迁移或改写现有 `data/papers/`、周报 ID、历史 URL。
- 需要把数千篇会议论文全部合并进现有全局论文详情和搜索索引，显著增加站点构建体积。
- 需要替换 Astro/Starlight、现有部署方式或企业微信消息结构。
- 需要付费 API、登录态抓取或绕过出版商访问限制。

## 10. 完成标准

首期完成意味着：ACL 2026 可由一条独立命令重复生成；数据、精选逻辑、报告和网页均可审阅；无 API Key 也能运行；失败不会影响普通周报；新增会议只需扩展配置和对应 proceedings 适配器。
