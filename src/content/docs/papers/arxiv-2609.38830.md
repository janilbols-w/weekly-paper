---
title: "SparLeak: Privacy Leakage from Sparse Attention in LLM Inference on Shared GPUs"
description: "Sparse attention is widely used to accelerate long-context inference in modern large language models (LLMs), but its input-dependent execution behavior introduces previously unexplored privacy risks."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.38830) · [PDF](https://arxiv.org/pdf/2609.38830)

## 一句话摘要

Sparse attention is widely used to accelerate long-context inference in modern large language models (LLMs), but its input-dependent execution behavior introduces previously unexplored privacy risks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse attention is widely used to accelerate long-context inference in modern large language models (LLMs), but its input-dependent execution behavior introduces previously unexplored privacy risks. We identify a new GPU micro-architectural side channel, termed Sparsity-Induced Memory Access (SIMA), which arises from secret-dependent key-value cache access patterns induced by sparse attention. Based on this observation, we present SparLeak, a phase-aware side-channel attack that extracts SIMA traces during LLM inference and enables two practical privacy extractions: query attribute inference from prefill-phase traces and autoregressive response reconstruction from decoding-phase traces. By reconstructing approximate token-level sparsity profiles from page-level observations and applying profiling-based learning, SparLeak accurately recovers sensitive information, including user-query attributes and private LLM response content. Extensive evaluation across three LLM architectures, three sparse attention mechanisms, and three privacy-sensitive datasets shows that SparLeak achieves average attack success rates of 90.9% for attribute inference and 87.3% for response reconstruction under real-world LLM serving settings, highlighting the significance to account for SIMA leakage when deploying sparse-attention-based LLM systems. We provide anonymized SIMA traces, trained attack models, evaluation scripts, and documentation as artifacts at https://anonymous.4open.science/r/Janus_artifacts/.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Fahao Chen, Linkang Du, Jinhao Zhou, Peng Li, Zhou Su
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
