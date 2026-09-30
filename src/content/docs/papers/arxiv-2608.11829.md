---
title: "Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling"
description: "On-policy distillation (OPD) has emerged as a promising post-training technique for enhancing LLM reasoning."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.11829) · [PDF](https://arxiv.org/pdf/2608.11829)

## 一句话摘要

On-policy distillation (OPD) has emerged as a promising post-training technique for enhancing LLM reasoning.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) has emerged as a promising post-training technique for enhancing LLM reasoning. Under the reverse KL objective, the idealized optimum of OPD aligns the student distribution with that of the teacher. When the teacher consistently outperforms the student, this naturally suggests that OPD should yield broad improvements over the pre-OPD student. However, do such improvements extend across the entire range of test-time sampling budgets? In this work, we revisit this expectation through the lens of test-time scaling by varying the sampling budget $K$ and evaluating performance with pass@$K$. Across multiple settings, we observe two distinct patterns: OPD can improve pass@$K$ at both small and large sampling budgets, but it can also improve small-budget performance while reducing large-budget pass@$K$. We show one condition that guarantees such a reversal and an idealized reverse KL counterexample where it occurs even when the teacher has higher accuracy on every problem. To choose between two candidate teachers at a target sampling budget, we propose the \textit{Teacher Advantage Score at $K$} (TAS@$K$), which can be computed before OPD training to predict which teacher will lead to a larger improvement in pass@$K$. Across three domains and thirteen benchmarks, the ordering predicted by TAS@$K$ agrees with the observed pass@$K$ improvements of the resulting OPD models in 83.6\% of experiments, providing a useful signal for teacher selection at the target pass@$K$.

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

- 作者：Xinmu Ge, Zizhuo Zhang, Yu Huang, Jianing Zhu, Lin Yuan, Wanli Gu, Weichang Wu, Weiran Huang, Bo Han, Xiaolu Zhang, Jiangchao Yao
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
