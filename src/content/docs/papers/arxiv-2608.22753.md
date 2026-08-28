---
title: "Beyond Factual Knowledge: Benchmarking and Learning Step-Level Procedural Rule Reasoning in Large Language Models"
description: "Large language models (LLMs) excel at text understanding and generation, yet still struggle to reliably understand and apply externally provided procedural rules at scale."
---

**评分：50/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.22753) · [PDF](https://arxiv.org/pdf/2608.22753)

## 一句话摘要

Large language models (LLMs) excel at text understanding and generation, yet still struggle to reliably understand and apply externally provided procedural rules at scale.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) excel at text understanding and generation, yet still struggle to reliably understand and apply externally provided procedural rules at scale. To evaluate this capability, we introduce RuleWorld, a large-scale benchmark that reformulates rules as globally reusable abstract units rather than instance-specific facts. In RuleWorld, several scenarios, including single-rule, parallel multi-rule, and multi-hop reasoning, are settled for comprehensive evaluation. We further propose DynaRule, an end-to-end framework that injects the given rules into the KV cache and turns retrieval into an internal, learnable, step-wise process. Specifically, DynaRule employs Stacked Step-Level Attention Training with a special token to enable dynamic rule re-attention and updating during inference. In this way, the model can re-attend to the most relevant rules at each step, dynamically replacing outdated ones to support more stable multi-step reasoning. Experiments on RuleWorld show that existing LLMs face challenges under large rule pools, while DynaRule improves average QA accuracy by up to 19 points and achieves over 85% Recall@1 at 10K rules, outperforming strong baselines by large margins. We make our code and dataset available here: https://github.com/SharkSpicy-NLP/Beyond-Factual-Knowledge.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 17 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Bohan Yu, Pengfei Cao, Chen Han, Chenxi Zhou, Zhiheng Zhang, Zhiyang Xie, Wenhao Teng, Xiangwen Liao, Jun Zhao, Kang Liu
- 发布：2026-08-24；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/SharkSpicy-NLP/Beyond-Factual-Knowledge](https://github.com/SharkSpicy-NLP/Beyond-Factual-Knowledge)
- 阅读深度：metadata
