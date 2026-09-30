---
title: "HiFloat4 Format for Language Model Pre-training on Ascend NPUs"
description: "Training large foundation models at low numerical precision is one of the most promising directions for reducing the compute and memory cost of modern AI."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2604.08826) · [PDF](https://arxiv.org/pdf/2604.08826)

## 一句话摘要

Training large foundation models at low numerical precision is one of the most promising directions for reducing the compute and memory cost of modern AI.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training large foundation models at low numerical precision is one of the most promising directions for reducing the compute and memory cost of modern AI. Recent 4-bit floating-point formats such as MXFP4 and NVFP4 can be applied to linear GEMM operations in LLMs, but their limited dynamic range introduces numerical instability that prior work addresses by stacking stabilization mechanisms, typically executed at higher precision and partially eroding the efficiency gains that motivate FP4. In this work, we argue that numerical format design is itself a first-class lever for stable FP4 training, and present the first systematic study of FP4 LLM pretraining on energy-efficient Huawei Ascend NPUs. We compare the recently proposed HiFloat4 (HiF4) format against both MXFP4 and NVFP4, holding one recipe fixed across all three formats across dense (OpenPangu-1B, Llama3-8B) and Mixture-of-Experts (Qwen3-MoE-30B) architectures and executing all linear and expert GEMMs in FP4. At matched storage --- NVFP4 and HiF4 both spend 4.5 bits per value --- the three formats differ far more in what they require before they will train at all than in final accuracy. HiF4 reaches a relative loss of 1.55\% with no stabilization, below fully stabilized MXFP4 (1.79\%) and below NVFP4 carrying the per-tensor scaling it cannot train without (2.00\%); NVFP4 diverges under every combination of stochastic rounding and Hadamard transform we tried. Our results suggest that stable, accurate FP4 training does not require an ever-growing stack of stabilization techniques; it requires the right numerical format.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mehran Taghian, Yunke Peng, Xing Huang, Yao Wang, Yaoyuan Wang, Wei Guo, Yuanyong Luo, Tianchi Hu, Junsong Wang, Xin Wang, Hu Liu, Yu Cheng, Ziwei Yu, Hongliang Li, Mehdi Rahimifar, Lei Yan, Xuefei Wang, Zhuang Ma, Lei Liu, Hui Yu, Anandharaju Durai Raju, Hoang Le, Hei Yi Mak, Tanzila Rahman, Shadan Golestan
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
