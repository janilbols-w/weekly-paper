---
title: "CD4LM: Consistency Distillation and aDaptive Decoding for Diffusion Language Models"
description: "Diffusion language models (DLMs) accelerate generation by decoding multiple tokens in parallel, but pushing them to fast decoding often sacrifices accuracy."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2601.02236) · [PDF](https://arxiv.org/pdf/2601.02236)

## 一句话摘要

Diffusion language models (DLMs) accelerate generation by decoding multiple tokens in parallel, but pushing them to fast decoding often sacrifices accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (DLMs) accelerate generation by decoding multiple tokens in parallel, but pushing them to fast decoding often sacrifices accuracy. We attribute this to a static-to-dynamic mismatch: training optimizes local denoising under fixed schedules, while fast inference skips steps and encounters irregular mask patterns. Existing accelerators largely address only one side of this problem. Training-free inference methods speed up decoding without changing the model, leaving the mismatch unresolved; training-side distillation methods adapt the model, but often tie the student to a specific decoding trajectory, limiting composability and still suffering accuracy loss. We propose CD4LM, a composable framework for accurate DLM acceleration. Its core training component, Discrete-Space Consistency Distillation (DSCD) trains a trajectory-invariant student on diverse masked states, reducing the mismatch without fixing a decoding policy. We pair DSCD with a lightweight ConfidenceAdaptive Decoder, while keeping the trained student compatible with external inference-side accelerators. On GSM8K, CD4LM preserves accuracy while achieving a 5.18x speedup; stacking CD4LM with per-step cache accelerators further pushes speedup to 9.73x at teacher-level accuracy, suggesting a scalable path for combining training-side robustness with future decoding advances. Code is available at https://github.com/yihao-liang/CDLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Yihao Liang, Ze Wang, Ximeng Sun, Jiang Liu, Jialian Wu, Hao Chen, Xiaodong Yu, Emad Barsoum, Zicheng Liu, Niraj K. Jha
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/yihao-liang/CDLM](https://github.com/yihao-liang/CDLM)
- 阅读深度：metadata
