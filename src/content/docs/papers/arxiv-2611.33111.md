---
title: "Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching Draft and Target Distributions"
description: "Speculative decoding accelerates large language model (LLM) inference by employing a lightweight draft model to propose draft tokens and allowing the target model to verify the new tokens in parallel to improve inference-time compute utilization."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.33111) · [PDF](https://arxiv.org/pdf/2611.33111)

## 一句话摘要

Speculative decoding accelerates large language model (LLM) inference by employing a lightweight draft model to propose draft tokens and allowing the target model to verify the new tokens in parallel to improve inference-time compute utilization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model (LLM) inference by employing a lightweight draft model to propose draft tokens and allowing the target model to verify the new tokens in parallel to improve inference-time compute utilization. The speedup relies on the acceptance probability of draft tokens in target verification, which is directly related to the gap $\|p-q\|_1$ between the target distribution $p$ and the draft distribution $q$. In this paper, we study draft calibration of speculative decoding to improve the speedup of speculative decoding, where we employ post-hoc methods to calibrate the draft distribution to mitigate the distribution gap. We observe that though current community open-source draft models may learn the top candidate token correctly, they are generally underconfident compared to the target model, suggesting a consistent distribution mismatch. To mitigate the effect of this mismatch on the acceptance rate of the draft models, we try various post-hoc calibration methods, including standard temperature scaling and token-wise calibration. Our results suggest that a standard temperature scaling applied to the draft distribution improves the acceptance length by up to approximately 10\% with almost no additional cost across different tasks. Throughput analysis further verifies that this improvement in serving efficiency. Analysis of more general calibration methods reveals further potential room for improvement.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuxing Liu, Wei Zuo, Walid Krichene, Tong Zhang, Li Zhang
- 发布：2026-11-24；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
