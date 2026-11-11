---
title: "HyPLM Technical Report"
description: "Protein language models (PLMs) are standard tools for variant-effect prediction, protein annotation and design, but the compute needed to train and serve them keeps growing."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.12000) · [PDF](https://arxiv.org/pdf/2611.12000)

## 一句话摘要

Protein language models (PLMs) are standard tools for variant-effect prediction, protein annotation and design, but the compute needed to train and serve them keeps growing.

## 为什么值得关注

待编辑增强。

## 摘要原文

Protein language models (PLMs) are standard tools for variant-effect prediction, protein annotation and design, but the compute needed to train and serve them keeps growing. We present HyPLM-Flash, an efficient and open PLM trained by Hyra 2.0, the research agent developed by our team. HyPLM-Flash is a 650-million-parameter masked language model trained on 726 billion tokens, 0.73 times the data of ESM-2 650M and a fifth to an eighth of the data of E1-600M and ESM C 600M. It runs on an inference engine with fused kernels and INT8 matrix multiplication, embedding about 130,000 residues per second on a single NVIDIA H20 GPU, 1.9 to 2.7 times faster than other 600M-class encoders. In a matched evaluation against 28 public checkpoints on 32 tasks, HyPLM-Flash reaches a ProteinGym zero-shot Spearman correlation of 0.409, statistically tied with ESM-2 650M, ESM C 600M and E1-600M, and the highest organismal-fitness score among self-supervised single-sequence models. It gives the best long-range contact precision of all models evaluated, including ESM-2 15B and ESM C 6B, and a lower masked-residue loss than ESM-2 650M, ESM C 600M and E1-600M on held-out sequences and on recently released PDB chains. Matching state-of-the-art accuracy at a fraction of the training and inference cost, HyPLM-Flash sets a new Pareto frontier for protein language models. We have released the model weights and the inference engine at https://github.com/Tencent-Hunyuan/hyra-results/tree/main.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Haowei Lin, Cai Zhou, Xiangxin Zhou
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Tencent-Hunyuan/hyra-results/tree/main](https://github.com/Tencent-Hunyuan/hyra-results/tree/main)
- 阅读深度：metadata
