---
title: "Distilling What Matters: Confidence-Aware Selective Distillation for Large Language Models"
description: "Knowledge Distillation (KD) trains a smaller-capacity student model to imitate a larger-capacity teacher model by matching output distributions, implicitly assuming the teacher to be a reliable oracle."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.36734) · [PDF](https://arxiv.org/pdf/2609.36734)

## 一句话摘要

Knowledge Distillation (KD) trains a smaller-capacity student model to imitate a larger-capacity teacher model by matching output distributions, implicitly assuming the teacher to be a reliable oracle.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge Distillation (KD) trains a smaller-capacity student model to imitate a larger-capacity teacher model by matching output distributions, implicitly assuming the teacher to be a reliable oracle. In large language models (LLMs), this assumption often fails: teacher predictions can exhibit high entropy and hallucinations, causing standard KD to degrade well-calibrated student priors. We propose CaRE-KD, a confidence-gated distillation framework that replaces static objectives with uncertainty-adaptive optimization. CaRE-KD has two components: a token-level loss (CaRE-Divergence) that adaptively switches between Forward and Reverse KL divergence based on teacher--student confidence, and a batch-level epistemic rejection mechanism (Revival) that suppresses updates when the teacher is more uncertain than the student. We provide a gradient-level analysis showing how this dual-granularity design induces a conditional calibration mechanism that prior static divergences cannot reproduce. Empirically, across eight teacher--student pairs and eleven benchmarks spanning instruction following, chat alignment, code generation, and mathematical reasoning, CaRE-KD delivers consistent gains over strong baselines (Skewed-KL, $\alpha$--$\beta$ divergence). Highlights include up to $+3.2$ average ROUGE-L on instruction-following tasks, $+2.1$ pass@1 on MBPP, $+1.7$ accuracy on GSM8k, and $+1.8$ accuracy on CollegeMath over the strongest baseline, with consistent gains in LLM-as-a-judge factuality (up to $+2.5$ per task over Skewed-RKL). Revival further acts as a principled, loss-agnostic plug-in that systematically strengthens existing distillation objectives by filtering epistemically unreliable teacher supervision.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ayan Sengupta, Vaibhav Seth, Tanmoy Chakraborty
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
