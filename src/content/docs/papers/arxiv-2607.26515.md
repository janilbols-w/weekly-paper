---
title: "HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models"
description: "We present, to our knowledge, the first end-to-end FP4 RL post-training, in which both the rollout and training policies, including their forward and backward passes, operate at 4-bit precision."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.26515) · [PDF](https://arxiv.org/pdf/2607.26515)

## 一句话摘要

We present, to our knowledge, the first end-to-end FP4 RL post-training, in which both the rollout and training policies, including their forward and backward passes, operate at 4-bit precision.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present, to our knowledge, the first end-to-end FP4 RL post-training, in which both the rollout and training policies, including their forward and backward passes, operate at 4-bit precision. A systematic study reveals that the dominant source of degradation in FP4 RL is not training-side quantization error but rollout activation quantization: outliers stretch the dynamic range so far that a large number of activation values underflow to zero under FP4. Counterintuitively, restoring the training policy to higher precision while keeping the rollout in FP4 makes accuracy worse than full FP4 baseline, exposing rollout--training mismatch as the principal failure mode and ruling out standard pretraining-style fixes. We address this with Rollout Residual Quantization (Rollout-ResQ): a single residual correction term constrained to a hardware-friendly sparsity pattern, added only to the FP4 rollout matmul -- a lightweight correction that recovers most of the precision lost to outlier-driven underflow without inflating the rollout's compute footprint. On Qwen2.5-3B, Rollout-ResQ paired with the HiFloat4 (HiF4) format -- whose three-level hierarchical scaling preserves resolution under FP4's tight 4-bit budget -- closes the accuracy gap to BF16 from 3.59% to 1.39%, bringing fully quantized FP4 RL within close reach of full precision. Applied to the open-standard MXFP4, the same recipe narrows the gap from 13.6% to 5.3%, revealing that FP4 format choice is a key factor that determines the ceiling on recoverable accuracy. The experimental results on Qwen2.5-Math-7B further confirm the recovery benefits of Rollout-ResQ with HiF4. Together, these results establish HiF4 as the enabling format for end-to-end FP4 RL post-training, and Rollout-ResQ as the activation-side mechanism that makes the gap to BF16 closable.

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

- taxonomy keywords: fp4, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hei Yi Mak, Shadan Golestan, Hoang Le, Mehran Taghian Jazi, Yunke Peng, Yaoyuan Wang, Yao Wang, Junsong Wang, Tianchi Hu, Fengchen He, Guipeng Hu, Tanzila Rahman, Anandharaju Durai Raju
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
