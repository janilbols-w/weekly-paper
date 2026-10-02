---
title: "Chinese-Jev: Bringing System One Model to Chinese-Language Tasks"
description: "System One models such as Jev offer an efficient alternative to generative language models for tasks that require decisions rather than open-ended responses."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.36965) · [PDF](https://arxiv.org/pdf/2609.36965)

## 一句话摘要

System One models such as Jev offer an efficient alternative to generative language models for tasks that require decisions rather than open-ended responses.

## 为什么值得关注

待编辑增强。

## 摘要原文

System One models such as Jev offer an efficient alternative to generative language models for tasks that require decisions rather than open-ended responses. However, existing Jev models exhibit limited Chinese-language decision accuracy, restricting their utility in both general and specialized settings. In this paper, we introduce Chinese-Jev, a System One model that addresses this gap through a unified data processing and training pipeline. Our data processing protocol converts heterogeneous Chinese-language annotations into probability targets over candidate options, enabling a shared training formulation across domains and question formats. To enable efficient inference, Chinese-Jev adopts a lightweight encoder-only backbone for text encoding and learns to score candidate answers through decision-oriented training. To address the misalignment between the pre-training distribution and downstream Chinese-language scenarios, we first train the model on a general-purpose corpus of 10 million examples, then fine-tune it separately for the medical, legal, and financial domains. To evaluate decision accuracy and calibration in both general and domain-specific Chinese-language settings, we introduce Chinese-Jev Bench (CJ-Bench). After first-stage pre-training, Chinese-Jev exceeds the accuracy of the closed-source Jev model by 1.24% on general-domain tasks while achieving a 20.3x speedup. Subsequent domain-specific fine-tuning yields a 4.0% accuracy improvement over Jev in medicine and achieves 92% of Jev's average accuracy across specialized domains, with a 17x speedup and an average latency of only 15 ms per example. We further demonstrate on-device deployment of an INT8-quantized model on mobile devices, achieving an inference latency of approximately 1.0 second per decision. The project is available at https://gulucaptain.github.io/Chinese-Jev/.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zexiao Wang, Zihao Zhang, Xudong Wang, Pan Wang, Ziyi Ye, Haoyu Zhao, Zuxuan Wu, Shuicheng Yan
- 发布：2026-09-29；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
