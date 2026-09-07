---
title: "Distilled Continuous Diffusion Language Models Can Write Code in Few Steps---or One"
description: "Language generation is almost universally treated as a sequential process: autoregressive models emit one token at a time, while diffusion language models replace token-level seriality with a long trajectory of iterative refinement."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.04531) · [PDF](https://arxiv.org/pdf/2609.04531)

## 一句话摘要

Language generation is almost universally treated as a sequential process: autoregressive models emit one token at a time, while diffusion language models replace token-level seriality with a long trajectory of iterative refinement.

## 为什么值得关注

待编辑增强。

## 摘要原文

Language generation is almost universally treated as a sequential process: autoregressive models emit one token at a time, while diffusion language models replace token-level seriality with a long trajectory of iterative refinement. In this work, we introduce PlaidQ, a 0.7B continuous diffusion language model for code generation, and show that its trajectory can be aggressively distilled into only a few denoising steps---or even one, enabling efficient code generation. PlaidQ repurposes a pretrained autoregressive model as a bidirectional denoiser over continuous token embeddings. We distill PlaidQ with distribution matching for few-step generation and paired-trajectory supervision for one-step generation. At matched model scale, PlaidQ is competitive with discrete diffusion language models on code generation. Distillation then shifts the quality--compute frontier: a 16-step student reaches 31.78 and 40.49 pass@10 on HumanEval and MBPP+, surpassing the same PlaidQ teacher sampled for 512 steps. At the extreme, paired-trajectory distillation achieves 7.07 pass@1 on HumanEval with a single denoising step, producing functionally correct programs. Together, these results establish continuous diffusion as a viable path to few-step and one-step code generation. Broadly, continuous diffusion is not merely another representation for language: it provides an interface through which language models can inherit the acceleration and distillation machinery of continuous diffusion modeling. Training and inference code and model checkpoints are available at https://github.com/pengzhangzhi/plaidq.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Fred Zhangzhi Peng, Kaiwen Zheng, Anru R. Zhang
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/pengzhangzhi/plaidq](https://github.com/pengzhangzhi/plaidq)
- 阅读深度：metadata
