---
title: "Learning What Not to Forget: Long-Horizon Agent Memory from a Few Kilobytes of Learning"
description: "Long-running language-model systems accumulate interaction history that outgrows the context window, so they must continually evict."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.20954) · [PDF](https://arxiv.org/pdf/2606.20954)

## 一句话摘要

Long-running language-model systems accumulate interaction history that outgrows the context window, so they must continually evict.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-running language-model systems accumulate interaction history that outgrows the context window, so they must continually evict. When an eviction policy drops a task-critical detail, for example an access token issued at login or a path the next call needs, the action fails. We present LRE (Learned Relevance Eviction), a kilobyte-scale, CPU-only, language-model-free scorer that learns which units of history are task-critical and keeps them by verbatim extraction. Under a matched-budget comparison, in our experiment, no baseline dominates LRE on the accuracy-cost plane. On agents, LRE recovers 93% of the aggregate accuracy of keeping the entire history (41.1 vs. 44.0) and exceeds it by 27% on the simplest tasks, while requiring zero compressor calls and cutting the worst-case peak prompt by 52%. A controlled study trace shows LRE completes tasks where the others loop, finishing one such task in 37% fewer calls than keeping everything and solving 14 tasks where no other run policy does. On conversational memory, LRE outranks dense and token-pruning encoders at zero neural cost while being 295-1569x smaller in size. In downstream evaluation, LRE gives the best budgeted answer quality on LoCoMo reading 68% fewer tokens. Its supervision can also be annotation-free: training only on the system's own behavior recovers 95% of the supervised scorer's effectiveness. We argue that, because memory eviction in LLM agents is a fidelity problem, it requires a deployable proactive policy where the future query is unavailable and exact state is decisive, and that cheap learned relevance can be sufficient.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Nusrat Jahan Lia, Aritra Mazumder
- 发布：2026-09-04；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
