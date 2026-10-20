---
title: "Parallel Language Models via Variational Decoding"
description: "Autoregressive language models emit one token per forward pass."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.26693) · [PDF](https://arxiv.org/pdf/2610.26693)

## 一句话摘要

Autoregressive language models emit one token per forward pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive language models emit one token per forward pass. This causes high inference latency, in particular as models are scaled up for quality. In this paper, we introduce Parallel Language Models (PLMs), which generate mutually consistent tokens in one forward pass by routing dependencies through latent auxiliary variables. PLMs are trained using a variational bound that reduces to an autoregressive loss plus a parallel decoding loss. Empirically, PLMs are on a faster and better Pareto frontier than autoregressive and discrete diffusion baselines. Pretrained PLMs achieve near-autoregressive pretraining loss on model scales of 80M to 3B parameters, and speedup follows a power law in model size. When post-trained, our 1.3B model matches or exceeds an identically trained autoregressive model on math, coding, and instruction-following benchmarks, speeding up inference $2.3\text{-}5.7\times$. Together, we show that parallel generation can be trained from a single training objective at autoregressive quality. We will make our code available at https://github.com/mandt-lab/plm.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Felix Draxler, Robin C. Geyer, Daniel Geyfman, Farrin Marouf Sofian, Justus Will, Philipp Hildebrandt, Giosue Migliorini, Prakhar Srivastava, Gagan Sai Trinadh Duggaraju Peddiraju, Kushagra Pandey, Jorge da Silva Gon\c{c}alves, Elijah Tavares, Jan Niklas Groeneveld, Yang Meng, Julia E. Vogt, Stephan Mandt
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/mandt-lab/plm](https://github.com/mandt-lab/plm)
- 阅读深度：metadata
