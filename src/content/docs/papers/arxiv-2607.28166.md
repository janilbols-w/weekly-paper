---
title: "Commit Locally, Exit Globally: Coordinating Adaptive Sampling and Early Exit in Diffusion Language Models"
description: "Diffusion language models predict tokens in parallel but still require many iterative forward passes."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2607.28166) · [PDF](https://arxiv.org/pdf/2607.28166)

## 一句话摘要

Diffusion language models predict tokens in parallel but still require many iterative forward passes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models predict tokens in parallel but still require many iterative forward passes. Adaptive sampling accelerates local token commitment, while recent global stopping methods seek to end generation early. Our trajectory analysis shows that short answers can stabilize early in decoding, whereas reasoning outputs often require more steps to settle. A fixed progress threshold therefore struggles to avoid both redundant computation on short-answer tasks and premature termination on reasoning tasks. We introduce C$^4$, a training-free framework that combines local decoding acceleration with adaptive global early exit. Confidence-Verified Early Exit (CVEE) determines when to end generation, skipping the remaining steps once its stopping criterion is met. It combines confidence and temporal agreement to adapt stopping to the observed revision history. Commit-Core-Then-Confirm (CCTC) accelerates token commitment while generation continues, reducing the decoding steps needed to complete each block. It extends confidence-threshold parallel decoding with a boundary-anchored core and one-step confirmation of deferred predictions, constraining additional commitments to mitigate premature freezing under unresolved context. With CVEE calibrated once on LLaDA, the same numerical settings transfer across all 12 zero-shot tasks and to Dream without recalibration. Under this configuration, C$^4$ reduces decoding steps by 64-95% and achieves measured decoding-loop speedups of 2.6x-18.6x, with task performance close to full decoding. Component analyses show complementary contributions: early exit supplies most savings on short-answer tasks, while local acceleration contributes more on reasoning and code generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Chia-Ming Lee, Shao-Kai Liu, Ming-Ching Chang, Xin Li, Yu-Lun Liu, Chih-Chung Hsu
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
