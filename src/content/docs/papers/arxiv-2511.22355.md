---
title: "AutoTailor: Automatic and Efficient Adaptive Model Deployment for Diverse Edge Devices"
description: "On-device machine learning (ML) has become a fundamental component of emerging mobile applications."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2511.22355) · [PDF](https://arxiv.org/pdf/2511.22355)

## 一句话摘要

On-device machine learning (ML) has become a fundamental component of emerging mobile applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-device machine learning (ML) has become a fundamental component of emerging mobile applications. Adaptive model deployment delivers efficient inference for heterogeneous device capabilities and performance requirements through customizing neural architectures. SuperNet-based approaches offer a promising solution by generating numerous model variants from a pre-trained ML model. However, applying SuperNet in existing frameworks requires tedious model-aware development and time-consuming hardware-aware profiling, which limits their practical adoption. We present AutoTailor, the first framework to enable automated, end-to-end SuperNet-based adaptive model deployment for edge devices. Unlike manual SuperNet construction, AutoTailor employs a computation graph-guided compilation approach to automatically transform user-provided ML models into SuperNets. To support efficient specialization, AutoTailor incorporates learning-free latency and accuracy predictors, enabling low-cost yet accurate performance prediction. Our extensive evaluations demonstrate that AutoTailor reduces the lines of code for SuperNet construction by 10.8--34.5$\times$, reduces predictor profiling time by 2.2--11.5$\times$, and achieves up to 15.60\% absolute accuracy improvement and 60.03\% latency reduction compared to state-of-the-art approaches across diverse models and devices. AutoTailor's source code is publicly available at \url{https://github.com/liu-mengyang/AutoTailor}.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Mengyang Liu, Chenyu Lu, Haodong Tian, Fang Dong, Ruiting Zhou, Wei Wang, Dian Shen, Guangtong Li, Ye Wan, Li Li
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/liu-mengyang/AutoTailor}](https://github.com/liu-mengyang/AutoTailor})
- 阅读深度：metadata
