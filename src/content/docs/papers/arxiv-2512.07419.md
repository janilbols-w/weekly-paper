---
title: "Towards Training-free Automatic Proxy Discovery via Large Language Models for Mixed Precision Quantization"
description: "TAP 用 LLM 与进化搜索自动发现混合精度量化的评价代理，并以轻量 DPO 策略控制器根据适应度信号动态调整三类提示模板的选择概率，无需微调生成代理的 LLM。作者称该方法在主流基准上达到领先表现，但摘要未给出具体数值。"
---

**评分：54/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2512.07419) · [PDF](https://arxiv.org/pdf/2512.07419)

## 一句话摘要

TAP 用 LLM 与进化搜索自动发现混合精度量化的评价代理，并以轻量 DPO 策略控制器根据适应度信号动态调整三类提示模板的选择概率，无需微调生成代理的 LLM。作者称该方法在主流基准上达到领先表现，但摘要未给出具体数值。

## 为什么值得关注

混合精度配置搜索常依赖昂贵优化或人工设计代理；自动生成并迭代代理可降低量化方案探索的人力门槛，为硬件约束下的低精度部署提供更灵活的搜索入口。

## 摘要原文

Mixed-Precision Quantization (MPQ) liberates Deep Neural Networks (DNNs) from the Out-Of-Memory (OOM) bottleneck and has garnered increasing research attention. However, conventional methods either rely on costly differentiable optimization search, which is neither efficient nor flexible, or learn a quantized DNN from a proxy (e.g., HAWQ) manually designed by human experts, which is labor-intensive and requires extensive expert knowledge. Can we design a proxy without involving any human experts or training? In this paper, we provide an affirmative answer by proposing a novel Large Language Model (LLM)-driven Training-free Automatic Proxy (dubbed TAP) discovery framework. It reforms the design paradigm of MPQ by utilizing LLMs and evolutionary search strategies to automatically find superior TAP tailored for MPQ. In addition, to bridge the gap between black-box LLMs and the challenging MPQ task, we introduce a lightweight Direct Preference Optimization (DPO)-based strategy controller that dynamically reweights the selection probabilities of the three prompt templates for evolutionary search strategies according to fitness signals, without fine-tuning the LLM. This forms a task-aware feedback loop that improves proxy generation across evolutions. Extensive experiments on mainstream benchmarks demonstrate that TAP achieves state-of-the-art performance. Finally, we believe that our TAP will significantly contribute to the MPQ community by providing a new perspective on LLM-driven design algorithms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 24 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixed precision, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata
- 限制：该工作主要改进代理发现流程，而非直接提供 LLM 推理内核；摘要也未量化搜索成本、调用模型依赖和相对基线收益。其结论面向广义 DNN 混合精度量化，对大语言模型部署的实际收益仍需单独验证。

## 元数据

- 作者：Haidong Kang, Jun Du, Guo Yu
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
