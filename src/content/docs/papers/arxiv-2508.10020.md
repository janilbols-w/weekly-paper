---
title: "FedCoT: Communication-Efficient Federated Reasoning Enhancement for Large Language Models"
description: "Enhancing LLM reasoning in federated settings is nontrivial due to stringent computational, communication, and privacy constraints, especially in healthcare, where clinically consequential decisions require not only accuracy but also interpretable, auditable rationales to meet safety, accountability, and regulatory requirements."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2508.10020) · [PDF](https://arxiv.org/pdf/2508.10020)

## 一句话摘要

Enhancing LLM reasoning in federated settings is nontrivial due to stringent computational, communication, and privacy constraints, especially in healthcare, where clinically consequential decisions require not only accuracy but also interpretable, auditable rationales to meet safety, accountability, and regulatory requirements.

## 为什么值得关注

待编辑增强。

## 摘要原文

Enhancing LLM reasoning in federated settings is nontrivial due to stringent computational, communication, and privacy constraints, especially in healthcare, where clinically consequential decisions require not only accuracy but also interpretable, auditable rationales to meet safety, accountability, and regulatory requirements. Conventional federated fine-tuning largely imitates final answers rather than cultivating step-by-step reasoning, often relying on privacy-sensitive centralized distillation and still incurring substantial communication overhead. We address this gap with \textbf{\ours{}}, a federated reasoning framework that combines lightweight chain-of-thought resampling with a compact discriminator for selection, and client-aware LoRA stacking with weighted classifier aggregation to accommodate heterogeneity while reducing aggregation noise and communication; clients generate candidate chains and supervision locally, and only lightweight modules are aggregated on the server. Experiments on medical reasoning benchmarks show consistent gains under tight resource budgets while keeping data local and respecting privacy, offering an interpretable and resource-efficient solution. Our code is made publicly available at https://github.com/DIaacKr/FedCoT

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Chuan Li, Qianyi Zhao, Fengran Mo, Cen Chen
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/DIaacKr/FedCoT](https://github.com/DIaacKr/FedCoT)
- 阅读深度：metadata
