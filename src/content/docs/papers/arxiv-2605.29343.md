---
title: "Draft-OPD: On-Policy Distillation for Speculative Draft Models"
description: "Speculative decoding accelerates large language model inference by pairing a target model with a lightweight draft model whose proposed tokens are verified in parallel."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.29343) · [PDF](https://arxiv.org/pdf/2605.29343)

## 一句话摘要

Speculative decoding accelerates large language model inference by pairing a target model with a lightweight draft model whose proposed tokens are verified in parallel.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model inference by pairing a target model with a lightweight draft model whose proposed tokens are verified in parallel. A common way to build draft models, like EAGLE3 or DFlash is supervised fine-tuning (SFT) on target-generated trajectories. However, we observe that SFT quickly plateaus: the draft model's acceptance length on test data stops improving. The reason is an offline-to-inference mismatch: In SFT, the drafter learns from fixed target-generated trajectories, whereas during speculative decoding it is evaluated on blocks proposed under its own policy. This motivates on-policy distillation (OPD), where the target model supervises the drafter on draft-induced states. Yet OPD remains difficult for draft models, as they cannot reliably roll out complete sequences independently, whereas target-assisted generation makes the collected sequences follow the target distribution and thus eliminates the on-policy signal. We therefore propose Draft-OPD, which uses target-assisted rollout for stable continuations and replays drafting from the verification-exposed error positions. This allows the drafter to learn from target feedback on both accepted and rejected proposals, focusing training on the draft-induced errors that limit speculative acceptance. Experiments show that Draft-OPD achieves over $5\times$ lossless acceleration for thinking models across diverse tasks, improving over EAGLE-3 and DFlash by 23\% and 13\%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haodi Lei, Yafu Li, Haoran Zhang, Shunkai Zhang, Qianjia Cheng, Xiaoye Qu, Ganqu Cui, Bowen Zhou, Ning Ding, Yun Luo, Yu Cheng
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
