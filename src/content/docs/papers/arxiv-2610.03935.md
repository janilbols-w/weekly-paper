---
title: "General Decision Models: Benchmarking and Insights Beyond Jev"
description: "General decision models, such as Jev, have recently emerged as efficient alternatives to LLMs for structured judgment and selection."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.03935) · [PDF](https://arxiv.org/pdf/2610.03935)

## 一句话摘要

General decision models, such as Jev, have recently emerged as efficient alternatives to LLMs for structured judgment and selection.

## 为什么值得关注

待编辑增强。

## 摘要原文

General decision models, such as Jev, have recently emerged as efficient alternatives to LLMs for structured judgment and selection. But what kinds of decisions can these models reliably make, and how does their behavior change when individual decisions are composed into larger systems? To study this, we introduce JEVal, a bilingual benchmark comprising 11,257 instances from 36 datasets across 10 application domains, and evaluate 25 model configurations spanning general decision models and generative LLMs. Our results show that (1) general decision models are most competitive when decisions can be resolved from available evidence, but weaken when they require specialist knowledge or faithful uncertainty estimation: they can often identify the most likely outcome while substantially overstating its probability. (2) In more dynamic and realistic systems involving long-horizon, multi-step interactions, the advantages of fast local decision making are offset by reliability failures at the system level. on $\tau$-bench, faster local decisions reduce median episode time but lower task success as decision errors accumulate over long trajectories. (3) In large-scale social simulation, decision models approach strong generative LLMs on individual response prediction at substantially lower inference cost, yet remain weaker in user profiling and exhibit larger aggregate estimation errors and systematic bias. Finally, we propose InnerJev-4B and InnerJev-27B, which internalize an open-weight LLM's own reasoning into a single-pass first-token decision through Reasoning-to-Readout Self-Distillation, with InnerJev-27B performing on par with Jev on JEVal while answering a typical query in about 0.1 s.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Feiyu Duan, Jiayu Lin, Jia Wang, Jun Xiang, Jialiang Wu, Xinnong Zhang, Hanqi Yan, Siyuan Wang, Zhongyu Wei
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
