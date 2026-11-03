---
title: "CLIC: Closed-Loop Intent Consistency for Securing LLM-Driven Control in Open RAN"
description: "With the progressive capabilities of large language models (LLMs), researchers are finding ways to integrate them into the control loops of Open Radio Access Network (O-RAN) to enable slicing and resource management through user intents."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.40744) · [PDF](https://arxiv.org/pdf/2610.40744)

## 一句话摘要

With the progressive capabilities of large language models (LLMs), researchers are finding ways to integrate them into the control loops of Open Radio Access Network (O-RAN) to enable slicing and resource management through user intents.

## 为什么值得关注

待编辑增强。

## 摘要原文

With the progressive capabilities of large language models (LLMs), researchers are finding ways to integrate them into the control loops of Open Radio Access Network (O-RAN) to enable slicing and resource management through user intents. However, integration of LLMs in the O-RAN control loop via the RAN Intelligent Controller (RIC) makes the system vulnerable to \textit{runtime prompt injection threats}, which manipulate control decisions without violating interface authentication, and \textit{residual virtual prompt injection (VPI)} attacks that plant trigger mechanisms to silently steer the behaviour during fine-tuning. Existing studies address only the runtime threat and do not enforce consistency across the full control path, i.e. from the certified A1 intent, through the multi-step LLM trajectory, to the final E2 action. We propose a closed-loop intent-consistency layer (CLIC) that jointly mitigates both threats. The proposed CLIC defines a formal consistency score using a small quantized language model, which is deployed as a Non-RT rApp for model-integrity certification along with a Near-RT xApp for runtime enforcement. We implement CLIC on the OpenAI Cellular (OAIC) platform and evaluate it under domain-adapted JailbreakBench, AdvBench, and VPI workloads. The experimental results show that the proposed CLIC reduces the attack success rate from 0.92 to 0.29 and residual VPI attacks from 0.37 to 0.04, while improving isolation and fairness at slightly higher latency costs, i.e. approximately 27 ms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sunder Ali Khowaja, Kapal Dev, Joongheon Kim, Angelos Antonopoulos, Nikolaos Bartzoudis
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
