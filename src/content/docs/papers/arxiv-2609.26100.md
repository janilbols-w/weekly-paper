---
title: "TSS: Target-Side Sparsification for Speculative Decoding in Domain-Specific Large Language Models"
description: "Speculative decoding accelerates large language model inference through collaboration between a lightweight draft model and a target verifier."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.26100) · [PDF](https://arxiv.org/pdf/2609.26100)

## 一句话摘要

Speculative decoding accelerates large language model inference through collaboration between a lightweight draft model and a target verifier.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model inference through collaboration between a lightweight draft model and a target verifier. Existing methods mainly improve the draft side, while the target model is typically kept dense and unchanged. We show that, under domain-specific inference, full-depth target verification is not always the optimal choice. Counter-intuitively, skipping selected target layers can reduce verification cost while simultaneously increasing draft acceptance and preserving, or even improving, downstream task performance. Based on this observation, we propose TSS, a target-side sparsification framework for speculative decoding. TSS employs an acceptance- and metric-aware breadth search to explore multi-layer skip configurations without imposing a fixed priority between the two objectives. The selected configurations are stored in a domain-to-configuration mapping and applied by a lightweight skip controller, allowing one complete target model to support multiple sparse verification paths without retraining or permanent parameter pruning. Experiments on Spec-Bench across multiple domains, model scales, and speculative decoding methods show consistent improvements in draft acceptance and downstream task performance. In Translation setting, TSS increases the average accept length from 2.70 to 4.53 (+67.8%), improves BLEU from 0.131 to 0.237 (+80.9%), and raises end-to-end throughput from 75.6 to 127.3 tokens/s, corresponding to a 1.68X speedup.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Haibo Hu, Lianming Huang, Qiao Li, Nan Guan, Chun Jason Xue
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
