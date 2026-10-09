---
title: "Generative Spatiotemporal Intent Sequence Recommendation via Implicit Reasoning in Amap"
description: "Real-world user behavior rarely consists of isolated actions; instead, it often forms intent flows governed by spatiotemporal dependencies."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.28888) · [PDF](https://arxiv.org/pdf/2605.28888)

## 一句话摘要

Real-world user behavior rarely consists of isolated actions; instead, it often forms intent flows governed by spatiotemporal dependencies.

## 为什么值得关注

待编辑增强。

## 摘要原文

Real-world user behavior rarely consists of isolated actions; instead, it often forms intent flows governed by spatiotemporal dependencies. To provide integrated service recommendations, we focus on the task of Generative Spatiotemporal Intent Sequence Recommendation (GSISR), which aims to generate intent sequences that are logically coherent and physically executable within complex spatiotemporal contexts. While LLMs offer strong reasoning potential for GSISR, direct industrial deployment is limited by high inference latency and context-mismatched or physically infeasible plans. To address these challenges, we propose a generative framework, GPlan, that internalizes LLM reasoning into lightweight models through two components. First, to enable reasoning under strict latency constraints, we introduce Progressive Implicit CoT Distillation, which compresses explicit reasoning processes into reserved latent tokens, allowing small models to inherit complex planning logic without generating long reasoning text. Second, to address the disconnect between general knowledge and real-world constraints, we design Spatiotemporal Counterfactual DPO. By aligning the model with counterfactual context-plan pairs, we improve sensitivity to spatiotemporal context and reduce context-mismatched plans. Offline experiments and online A/B testing demonstrate that our approach improves sequence coherence and context responsiveness. Our implementation and the anonymized GSISR dataset are available at https://github.com/alibaba/GPlan.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Sicong Wang, Ruiting Dong, Yue Liu, Bowen Zheng, Jun Meng, Jie Li, Shuaijun Guo, Yu Gu, Fanyi Di, Xin Li
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/alibaba/GPlan](https://github.com/alibaba/GPlan)
- 阅读深度：metadata
