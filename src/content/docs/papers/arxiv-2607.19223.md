---
title: "AdaFlash: Adaptive Speculative Decoding via On-Policy Distilled Diffusion Drafters"
description: "Speculative decoding, in which a lightweight draft model first generates a draft sequence that is then verified by the target model, has become a prevalent paradigm for accelerating large language model inference."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2607.19223) · [PDF](https://arxiv.org/pdf/2607.19223)

## 一句话摘要

Speculative decoding, in which a lightweight draft model first generates a draft sequence that is then verified by the target model, has become a prevalent paradigm for accelerating large language model inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding, in which a lightweight draft model first generates a draft sequence that is then verified by the target model, has become a prevalent paradigm for accelerating large language model inference. Recent work such as DFlash further boosts drafting efficiency by leveraging diffusion drafters, whose parallel denoising mechanism enables draft generation in a single forward pass. In this work, we uncover a central pitfall of diffusion drafters: bidirectional attention is a double-edged sword. On one hand, it endows the model with parallel generation and global contextual modeling capabilities; on the other hand, this inherent global dependency introduces high variance at both the domain-level and the token-level: acceptance rates fluctuate substantially across different domains, and draft token quality also varies heterogeneously at different token positions. To tackle this issue, we propose AdaFlash framework, comprising two components: (i) an on-policy distillation (OPD) algorithm with reverse-KL divergence tailored for diffusion drafters, bringing stable convergence and effectively reducing domain-level variance; and (ii) an adaptive length head that dynamically adjusts the candidate sequence length on the fly, substantially lowering the verification cost of the target model and mitigating token-level variance. Experiments demonstrate that AdaFlash consistently improves speedup rate during deployment, with especially significant gains under high-concurrency, achieving up to 66% higher average throughput than previous SOTA. Our code is available at https://github.com/ZinYY/AdaFlash.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yu-Yang Qian, Hao-Cong Wu, Chen Chen, Jiacheng Sun, Zhenhua Dong, Peng Zhao, Zhi-Hua Zhou
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ZinYY/AdaFlash](https://github.com/ZinYY/AdaFlash)
- 阅读深度：metadata
