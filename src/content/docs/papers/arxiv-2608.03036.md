---
title: "LLM Serving in the Wild: An Empirical Study of Frameworks, Methods, and System Designs"
description: "Large Language Models (LLMs) are integrated into software systems and AI services, making efficient LLM serving a concern for software engineering."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.03036) · [PDF](https://arxiv.org/pdf/2608.03036)

## 一句话摘要

Large Language Models (LLMs) are integrated into software systems and AI services, making efficient LLM serving a concern for software engineering.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) are integrated into software systems and AI services, making efficient LLM serving a concern for software engineering. Serving LLMs is challenging because inference requires computation, memory, GPU resources, and execution while maintaining latency and throughput. Although prior research has proposed LLM inference, optimization, and serving techniques and frameworks, little is known about how they are adopted in practice. In this study, we investigate the use of LLM serving frameworks and serving methods in open-source software systems. We identify and analyze five LLM-specific frameworks: vLLM, SGLang, TensorRT-LLM, LMDeploy, and FlashInfer. We examine how these frameworks and techniques are adopted individually and in combination, how adoption varies across categories of LLMs, and how repositories differ in intent, focus, use case, and architectural design. Our results show that vLLM is the most visible framework in popularity and adoption, while parallel computation, memory management, and network pruning are the most frequently used serving-method categories. Multi-framework usage is limited, suggesting that developers rely on a single serving framework; however, combined frameworks connect complementary capabilities across the serving stack. Framework adoption varies across model families, modalities, model sizes, domain specializations, and deployment settings. Repository-level analysis shows that LLM serving frameworks support applications and architectures, including Reinforcement Learning (RL)-based reasoning, multimodal generation and understanding, microservices, and cloud infrastructure. Overall, this study provides a large-scale empirical characterization of LLM serving framework adoption in practice and offers insights for researchers, framework maintainers, and practitioners working on LLM systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Forough Majidi, Mohammad Mehdi Morovati, Foutse Khomh, Heng Li
- 发布：2026-08-04；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
