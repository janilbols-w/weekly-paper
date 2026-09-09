---
title: "A Ticket from Marginals to Joints: Coupled-Noise Distillation for One-Step Block Generation in Diffusion Language Models"
description: "Autoregressive language models commit one token per forward pass; diffusion language models commit a block of tokens over several steps."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.06324) · [PDF](https://arxiv.org/pdf/2609.06324)

## 一句话摘要

Autoregressive language models commit one token per forward pass; diffusion language models commit a block of tokens over several steps.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive language models commit one token per forward pass; diffusion language models commit a block of tokens over several steps. We ask whether a block can be committed in a single forward pass. We study this with a noise-conditioned masked denoiser: a data-independent Gaussian noise field is added to the mask embeddings so that, in principle, each sampled field selects one joint mode of the block. The established way of training such a model is to sample several fields per example and let them compete for the data, by winner-take-all or importance weighting. This gives the noise only coarse control: in our experiments, the information it carries grows roughly with the logarithm of the number of competing fields, and one-step outputs remain rarely coherent across the model sizes tested. We propose CONDOR (Coupled-Noise Distillation for One-Step Readout). A noise-conditioned teacher is trained with a random number of masked positions and winner-take-all. A student proposes a one-step block, retains selected tokens, and learns from the block obtained when the teacher refills the other positions in several steps under the same noise field; a noise-free masked-LM term on the ground truth anchors the student. Human evaluation on TinyStories shows a large gain in one-step legality while different noise fields still yield different blocks, at one forward pass per block.

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

- 作者：Lin Yao
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
