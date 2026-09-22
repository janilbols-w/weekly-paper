---
title: "Tool-Augmented On-Policy Distillation for LLM Domain Adaptation in Sequence-Based Omics Tasks"
description: "Multi-omics sequences contain complex biological patterns, yet deciphering their mechanisms for automated scientific discovery remains challenging."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.23435) · [PDF](https://arxiv.org/pdf/2609.23435)

## 一句话摘要

Multi-omics sequences contain complex biological patterns, yet deciphering their mechanisms for automated scientific discovery remains challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-omics sequences contain complex biological patterns, yet deciphering their mechanisms for automated scientific discovery remains challenging. As large language models (LLMs) interpret these sequences, evaluating both predictions and scientific reasoning is critical. However, existing benchmarks for multi-omics sequence tasks rely on classification and regression metrics, neglecting whether models grasp the underlying biological evidence. We introduce OmicsBench, the first reasoning benchmark for multi-omics sequences, comprising 1,160 expert-validated questions across six tasks spanning DNA regulation, RNA processing, and protein function. OmicsBench requires traceable evidence chains, evaluated using instance-specific rubrics developed with domain experts. Evaluating 17 LLMs reveals an inverse relationship: while scientific LLMs outperform general-purpose LLMs in sequence classification accuracy, they fail to provide valid evidence to support their predictions. One plausible interpretation is shortcut learning: specialized models may rely on statistical patterns rather than the biological mechanisms needed for scientific discovery. Motivated by this finding, we introduce tool-augmented on-policy distillation (TA-OPD), a post-training method to align sequence prediction with evidence-grounded biological reasoning. Across five Qwen3.5 models spanning 0.8B to 27B parameters, TA-OPD consistently strengthens biological evidence grounding while improving predictive performance on most tasks. These gains persist across model scales, indicating that stronger sequence reasoning does not arise solely from increased model capacity, but can be improved through evidence-aware training. Together, OmicsBench and TA-OPD provide a framework for diagnosing reasoning failures in multi-omics LLMs and a path toward models whose predictions are better grounded in biologically meaningful evidence.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jie Ying, Zhefan Wang, Zihong Chen, Zhengqing Li, Jinzhe Li, Gang Li, Jian Liu, Fang Hu, Tao Luo, Zhonghang Yuan, Wanli Ouyang, Stan Z. Li, Fan Yang, Nanqing Dong
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
