---
title: "Learning When to Commit: Schedule Distillation for Fast Diffusion Language Models"
description: "Diffusion large language models (dLLMs) can generate multiple tokens in parallel, but often require many decoding rounds to complete a response."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.35804) · [PDF](https://arxiv.org/pdf/2610.35804)

## 一句话摘要

Diffusion large language models (dLLMs) can generate multiple tokens in parallel, but often require many decoding rounds to complete a response.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion large language models (dLLMs) can generate multiple tokens in parallel, but often require many decoding rounds to complete a response. Efficient generation depends not only on which tokens are easy to predict, but also on how committing to them helps predict the remaining positions. A highly predictable token may provide little useful context, while revealing a less predictable token can help several other positions become predictable sooner. We propose dSpark, a new schedule distillation-based framework for learning when to commit tokens for faster diffusion language generation. To achieve this, we construct unmasking schedules that prioritize tokens whose reveal makes other positions easier to predict, reducing uncertainty earlier in decoding. We then distill these schedules into the model to enable faster parallel sampling, with a KL-divergence regularizer to help preserve generation quality. We extensively evaluate our approach across mathematical reasoning and code generation tasks. On GSM8K, our method achieves remarkable 10.12$\times$ and 5.12$\times$ speedups over the various baselines on LLaDA-8B-Instruct and Dream-7B-Instruct, respectively, while maintaining superior task performance. Our code is available at https://github.com/VILA-Lab/dSpark.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Aidar Myrzakhan, Zhiqiang Shen
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/VILA-Lab/dSpark](https://github.com/VILA-Lab/dSpark)
- 阅读深度：metadata
