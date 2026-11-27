---
title: "Rethinking Knowledge Distillation for Diffusion Language Models"
description: "Knowledge distillation has recently proven highly effective for improving autoregressive models, but its applicability to DLMs remains poorly understood."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.33670) · [PDF](https://arxiv.org/pdf/2611.33670)

## 一句话摘要

Knowledge distillation has recently proven highly effective for improving autoregressive models, but its applicability to DLMs remains poorly understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation has recently proven highly effective for improving autoregressive models, but its applicability to DLMs remains poorly understood. We present the first systematic study of KD for DLMs and uncover two non-intuitive failures of classical forward-KL (FKL) distillation: (i) student perplexity does not improve monotonically with more teacher-generated data, and (ii) on the same teacher-generated corpus, FKL distillation underperforms simply training the student with the original DLM denoising objective. To address them, we propose a unified, data-free distillation framework for masked DLMs. First, the framework runs an off-policy distillation phase that absorbs general knowledge from a static set of teacher-generated data. Then, the framework employs on-policy distillation which consists of three techniques: a trajectory loss along the student's own reverse process, confidence reweighting that down-weights tokens where the teacher is unsure, and a trust-region anchor that stabilizes the moving target. On MDLM, the resulting student attains a GPT-2 perplexity of $24.75$, surpassing the teacher's $27.04$; on Dream-7B distillation to a 93M student model, the framework reduces Qwen-2.5 perplexity from the FKL-distilled baseline of $25.23$ to $19.83$ while preserving performance on zero-shot general capability benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuxuan Sun, Yuanjian Xu, Jianing Hao, Yu Li, Sowmen Das, Zhong Li, Sangwoong Yoon, Miguel R. D. Rodrigues
- 发布：2026-11-26；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
