---
title: "Detecting Contaminated Code-Generation Prompt Batches via Influence Functions"
description: "Large language models (LLMs) are increasingly used for code generation, yet they remain vulnerable to prompts that elicit insecure implementations."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.14303) · [PDF](https://arxiv.org/pdf/2608.14303)

## 一句话摘要

Large language models (LLMs) are increasingly used for code generation, yet they remain vulnerable to prompts that elicit insecure implementations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are increasingly used for code generation, yet they remain vulnerable to prompts that elicit insecure implementations. Existing defenses typically rely on predefined threat models or known vulnerability patterns, limiting their effectiveness against novel attacks. We propose CodeSIFT, a threat-model-agnostic detection method that leverages influence functions to identify batches of prompts that induce anomalous model behavior. Rather than detecting specific vulnerabilities, CodeSIFT measures the parameter-space influence of generated code and uses a statistical test to determine whether a candidate prompt set deviates from a benign reference distribution. To evaluate our approach, we introduce two benchmark datasets covering a variety of vulnerabilities. We evaluate CodeSIFT on three open-weight code LLMs ranging from 3B to 7B parameters, achieving AUROC scores of up to 0.98 at moderate-to-high injection rates, while maintaining well-calibrated false positive rates and substantially outperforming static analysis baselines. These results suggest that influence-function-based detection is a promising direction for identifying malicious code-generation prompts without requiring prior knowledge of the underlying attack class.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Francesco Quinzan, Noor Munir, Yishun Lu, Stephen Roberts
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
