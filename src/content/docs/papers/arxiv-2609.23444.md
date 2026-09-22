---
title: "WaveletECO: A Closed-Loop Physical ECO Platform and a Specialized Local Language Model"
description: "Engineering change order (ECO) is an important step in repairing timing and electrical violations during the late stages of chip design."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.23444) · [PDF](https://arxiv.org/pdf/2609.23444)

## 一句话摘要

Engineering change order (ECO) is an important step in repairing timing and electrical violations during the late stages of chip design.

## 为什么值得关注

待编辑增强。

## 摘要原文

Engineering change order (ECO) is an important step in repairing timing and electrical violations during the late stages of chip design. Existing Agentic EDA methods primarily focus on tool invocation, with less attention to model decision quality and targeted training. A central challenge in ECO is multi-round decision-making: the model must use the results of each round to determine the next repair action. We propose WaveletECO, which integrates a closed-loop execution platform with large language models to enable agents to execute ECO decisions effectively. We also train a local 9B model through supervised fine-tuning and CPO-SimPO using execution demonstrations and decision-preference data, enabling ECO decision-making with a locally deployed model. Across 594 evaluation runs on 22 designs, WaveletECO-Policy (BF16) and (INT8) score 79.63 and 79.65, respectively, compared with GPT-6 Astra's 77.44. The estimated inference cost of INT8 is about 1/147 of GPT-6 Astra's. These results show that specialized model training supports effective, low-cost multi-round ECO repair, with repair quality retained under INT8 quantization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guoxiang Xu, Guozhen Ji, Zijian Luo, Zhengrui Chen, Qi Sun, Cheng Zhuo
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
