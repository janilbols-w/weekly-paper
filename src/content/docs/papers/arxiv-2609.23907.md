---
title: "A discrete generative model of neuronal spiking activity on microelectrode arrays"
description: "Generative models of neural activity could help characterize tissue dynamics, compare experimental conditions, and simulate population activity for applications ranging from disease and drug-response studies to closed-loop experimentation."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.23907) · [PDF](https://arxiv.org/pdf/2609.23907)

## 一句话摘要

Generative models of neural activity could help characterize tissue dynamics, compare experimental conditions, and simulate population activity for applications ranging from disease and drug-response studies to closed-loop experimentation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Generative models of neural activity could help characterize tissue dynamics, compare experimental conditions, and simulate population activity for applications ranging from disease and drug-response studies to closed-loop experimentation. Existing approaches, however, typically assume a fixed set of sorted neurons, whereas high-density microelectrode arrays produce extremely sparse, array-wide binary spike volumes in which the observed subset of electrodes varies across assays. We introduce a discrete generative model that represents this activity using a shared vocabulary of spatiotemporal motifs. A residual vector-quantized autoencoder learns the motif vocabulary, while a factorized masked transformer predicts where activity occurs and which motif appears at each active location. We evaluate the model on 31 assays spanning human brain organoids and acute \emph{ex vivo} human hippocampal tissue. The learned motifs are broadly reused: assay identity explains only $9%$ of the entropy in motif use, and motif overlap across tissue types is comparable to overlap within them. When representation quality is evaluated independently of the generative prior, our approach achieves $5.2\times$ the voxel-level reconstruction average precision of a matched flat tokenizer. For masked completion and free generation, the full model achieves $1.4$--$2.6\times$ the site-level average precision of the matched generative baseline and outperforms it across all four families of generation metrics. These results establish a compact, reusable representation for array-wide spiking activity without learned assay-specific parameters, providing a scalable foundation for generative modeling across diverse neural preparations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Md Sayed Tanveer, Mohammed A. Mostajo-Radji, Ge Wang
- 发布：2026-09-20；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
