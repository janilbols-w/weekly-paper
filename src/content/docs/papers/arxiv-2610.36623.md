---
title: "God Does Not Play Dice: Enforcing Batch Invariance in Agentic Kernel Generation"
description: "Large language model (LLM) serving systems dynamically batch user requests for GPU execution, so the same request may be processed alongside different requests across runs."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2610.36623) · [PDF](https://arxiv.org/pdf/2610.36623)

## 一句话摘要

Large language model (LLM) serving systems dynamically batch user requests for GPU execution, so the same request may be processed alongside different requests across runs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) serving systems dynamically batch user requests for GPU execution, so the same request may be processed alongside different requests across runs. If the GPU kernels lack batch invariance (BI), this changing batch context can alter the numerical output for an unchanged input, undermining reproducibility. Existing kernel generation agents focus on correctness and efficiency but \emph{overlook BI}. We find 19 confirmed BI violations among 83 batch-applicable released artifacts. To address this limitation, we propose \tool, which combines contract-guided static dependency analysis with dynamic validation of bitwise consistency across batch contexts. \tool is designed as a plug-in component for general kernel agents, allowing their original optimization capabilities to be reused while adding BI enforcement. We integrate it as successive acceptance gates in the optimization loop, rejecting structurally risky or dynamically non-invariant candidates before performance benchmarking and returning feedback to the agent. Experiments across three agent frameworks under baseline and BI-aware generation on real world LLM serving tasks show that \tool improves the BI pass rate from 67.6\% to 91.9\% while retaining 91.8\% of the baseline geometric mean speedup. These results demonstrate that \tool can be incorporated into kernel optimization by agents as an additional reliability objective alongside correctness and speed.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kernel generation, kernel optimization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Youwei Bao, Chengpeng Wang, Simin Chen
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
