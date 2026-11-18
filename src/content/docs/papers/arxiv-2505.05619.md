---
title: "LiteLMGuard: Seamless and Lightweight On-Device Guardrails for Small Language Models against Quantization Vulnerabilities"
description: "The growing adoption of Large Language Models (LLMs) has influenced the development of Small Language Models (SLMs) for on-device deployment across smartphones and edge devices, offering enhanced privacy, reduced latency, server-free functionality, and improved user experience."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2505.05619) · [PDF](https://arxiv.org/pdf/2505.05619)

## 一句话摘要

The growing adoption of Large Language Models (LLMs) has influenced the development of Small Language Models (SLMs) for on-device deployment across smartphones and edge devices, offering enhanced privacy, reduced latency, server-free functionality, and improved user experience.

## 为什么值得关注

待编辑增强。

## 摘要原文

The growing adoption of Large Language Models (LLMs) has influenced the development of Small Language Models (SLMs) for on-device deployment across smartphones and edge devices, offering enhanced privacy, reduced latency, server-free functionality, and improved user experience. However, due to on-device resource constraints, SLMs undergo size optimization through compression techniques like quantization, which inadvertently introduce fairness, ethical and privacy risks. Critically, quantized SLMs may respond to harmful queries directly, without requiring adversarial manipulation, raising significant safety and trust concerns. To address this, we propose LiteLMGuard, an on-device guardrail that provides real-time, prompt-level defense for quantized SLMs. Additionally, our guardrail is designed to be model-agnostic such that it can be seamlessly integrated with any SLM, operating independently of underlying architectures. Our LiteLMGuard formalizes deep learning (DL)-based prompt filtering by leveraging semantic understanding to classify prompt answerability for SLMs. Built on our curated Answerable-or-Not dataset, LiteLMGuard employs ELECTRA as the candidate model with 97.75% answerability classification accuracy. The on-device deployment of LiteLMGuard enabled real-time offline filtering with over 85% defense-rate against harmful prompts (including jailbreak attacks), 94% filtering accuracy and ~135 ms average latency. These results demonstrate LiteLMGuard as a lightweight robust defense mechanism for effectively and efficiently securing on-device SLMs against Open Knowledge Attacks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kalyan Nakka, Jimmy Dani, Ausmit Mondal, Nitesh Saxena
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
