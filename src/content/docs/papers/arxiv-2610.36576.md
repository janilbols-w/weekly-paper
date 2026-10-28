---
title: "Less is more: learning what to profile for GPU kernel optimization"
description: "Large language models have recently shown strong potential for automatically optimizing GPU kernels, yet their effectiveness depends critically on the hardware information available to the kernel optimization model."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2610.36576) · [PDF](https://arxiv.org/pdf/2610.36576)

## 一句话摘要

Large language models have recently shown strong potential for automatically optimizing GPU kernels, yet their effectiveness depends critically on the hardware information available to the kernel optimization model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models have recently shown strong potential for automatically optimizing GPU kernels, yet their effectiveness depends critically on the hardware information available to the kernel optimization model. Existing systems typically rely on predefined profiling strategies, leaving what to profile largely outside the optimization process. We show that effective profiling is not simply about collecting more information: increasing the number of profiling metrics does not monotonically improve kernel optimization, while the most useful profiling information varies across kernels. Our theoretical analysis further shows that, under such heterogeneous profiling utility, kernel-conditioned selection can outperform any single fixed profiling configuration. Motivated by this observation, we propose AutoProfiler, a feedback-driven framework for learning a deterministic profiling tree from optimization feedback. The tree is iteratively refined through REWRITE and SPLIT operations, with an LLM generating candidate modifications and empirical evaluation determining their acceptance. Once constructed, the tree quickly gathers the required profiling information for any kernel, allowing the LLM rewriter to be invoked only once. Experiments on KernelBench show that our approach improves kernel optimization over fixed profiling configurations under constrained profiling budgets. These results suggest that hardware profiling should evolve from static metric collection toward profiling reasoning, making profiling itself a new dimension for improving kernel optimization. The codes are available at https://github.com/Satissss/AutoProfiler.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel optimization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yihan Wang, Peiyu Liu, Runyu Chen, Wei Xu
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Satissss/AutoProfiler](https://github.com/Satissss/AutoProfiler)
- 阅读深度：metadata
