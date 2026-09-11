---
title: "PELM: Power Efficient On-Device LLM Inference with Speculative Decoding and Dynamic Voltage Frequency Scaling"
description: "Deploying Large Language Models (LLMs) directly on mobile platforms at the edge is gaining traction due to a myriad of benefits, such as increased privacy, personalization, and reduced latency."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.09662) · [PDF](https://arxiv.org/pdf/2609.09662)

## 一句话摘要

Deploying Large Language Models (LLMs) directly on mobile platforms at the edge is gaining traction due to a myriad of benefits, such as increased privacy, personalization, and reduced latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying Large Language Models (LLMs) directly on mobile platforms at the edge is gaining traction due to a myriad of benefits, such as increased privacy, personalization, and reduced latency. However, LLMs have heavy computational requirements, which are difficult for resource-constrained mobile and edge platforms to fulfill. In addition to limited compute resources, mobile and edge systems often have a compact form factor and lack physical mechanisms to dissipate heat generated from high processor usage rates (e.g., fans) to prevent throttling and reduced processing power, which LLMs can easily cause. To mitigate these effects, prior works have proposed various power governing strategies, such as dynamic voltage and frequency scaling (DVFS), for reducing power and heat generation for heavy computational tasks on mobile platforms. Recently, DVFS methods tailored for mobile LLMs have also been proposed. However, these methods mostly focus on optimizing hardware parameters and processor frequencies, and they fall short under some thermally constrained scenarios. Drawing from recent advances in machine learning, we identify and take advantage of the key insight that not all tokens require full-depth inference to maintain high-quality generation. Motivated by this, we present PELM, a solution that augments traditional DVFS processor frequency tuning with two additional workload-specific knobs: 1) speculative decoding and 2) variable verification depth to expand the optimization space to multiple dimensions for more power efficient on-device LLM inference. In extensive evaluations across hardware platforms and datasets, PELM demonstrates superior performance compared to state-of-the-art power governing methods, with up to 23.1% speedup and 52.4% reduction in energy consumption, while maintaining comparable task performance. The source code is available at https://github.com/imec-nu/PELM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Weisi Yang, Stephen Xia
- 发布：2026-09-09；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/imec-nu/PELM](https://github.com/imec-nu/PELM)
- 阅读深度：metadata
