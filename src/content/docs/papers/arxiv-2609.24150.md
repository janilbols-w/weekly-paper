---
title: "Acceptance-Aware Draft Model Training for Speculative Decoding"
description: "Speculative decoding accelerates large language model (LLM) inference by using a lightweight draft model to generate multiple candidate tokens that are verified by the target model in a single forward pass."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.24150) · [PDF](https://arxiv.org/pdf/2609.24150)

## 一句话摘要

Speculative decoding accelerates large language model (LLM) inference by using a lightweight draft model to generate multiple candidate tokens that are verified by the target model in a single forward pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model (LLM) inference by using a lightweight draft model to generate multiple candidate tokens that are verified by the target model in a single forward pass. Its speedup is largely determined by the acceptance length, yet existing draft-model training methods mainly optimize cross-entropy or Kullback-Leibler (KL) divergence as proxies. These objectives encourage distribution matching but do not directly optimize acceptance length, and the acceptance mechanism also differs between greedy and sampling-based decoding. In this work, we propose acceptance-length-aware training losses that directly optimize the expected number of accepted tokens within a speculative window. For greedy verification, we derive an expected accepted length (EAL) loss that explicitly maximizes expected acceptance length. For sampling-based decoding, we introduce a window total variation (WTV) loss that optimizes the overlap between temperature-scaled draft and target distributions while accounting for sequential acceptance dependencies. Both objectives can be further combined with a group-relative reinforcement learning stage (GRPO) using simulated acceptance length as the reward. Experiments across different target and draft models, tasks, and decoding settings show that our losses consistently improve acceptance length over KL-based training. WTV provides particularly strong gains under sampling-based decoding, while EAL better matches greedy verification. These results show that directly optimizing the acceptance objective, with losses tailored to the decoding mode, is more effective than conventional distribution-matching objectives.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianhua Xia, Mugilan Ganesan, Yifei Feng, Haiyu Wang, Maximilian Egger, Sai Qian Zhang
- 发布：2026-09-21；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
