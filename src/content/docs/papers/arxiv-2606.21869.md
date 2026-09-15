---
title: "The Language-Energy Divide: Measuring Energy Costs of Multilingual LLM Inference"
description: "Large language models (LLMs) are increasingly deployed in multilingual settings, yet the energy costs of serving these models across different languages remain poorly understood."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2606.21869) · [PDF](https://arxiv.org/pdf/2606.21869)

## 一句话摘要

Large language models (LLMs) are increasingly deployed in multilingual settings, yet the energy costs of serving these models across different languages remain poorly understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are increasingly deployed in multilingual settings, yet the energy costs of serving these models across different languages remain poorly understood. We present a systematic study of inference energy consumption across languages with ML.Energy framework (Chung et al., 2026). We find striking disparities: energy consumption per output token varies by up to 8.3 times across languages, while total energy for a fixed set of requests varies by up to 179 times between the cheapest (English, 17.6 kJ) and the most expensive (Pashto, 3,147 kJ) languages. Our analysis shows that this disparity is driven by two compounding factors: (1) higher per-token energy costs for languages using complex or rare scripts, and (2) more tokens generated for low-resource languages. Moreover, we find a double cost + performance penalty: languages with the highest energy footprints also tend to achieve the lowest task accuracy. We reveal that the energy divide persists across models, hardware, and tasks, suggesting a systemic energy inequity in multilingual LLM deployment. Finally, we recommend that the community treat energy as a first-class evaluation axis, extend reporting checklists and model cards to include it, and adopt deployment-side mitigations for better energy efficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Naihao Deng, Alissa Shen, Yiming Feng, Joan Nwatu, Jae-Won Chung, Mosharaf Chowdhury, Yulong Chen, Rada Mihalcea
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
