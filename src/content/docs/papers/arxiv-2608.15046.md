---
title: "Certifying Compressed Language Models: An Audit and a Statistical Toolkit"
description: "A fraction of a point of benchmark accuracy is the usual evidence that a compressed model is equivalent to its original."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.15046) · [PDF](https://arxiv.org/pdf/2608.15046)

## 一句话摘要

A fraction of a point of benchmark accuracy is the usual evidence that a compressed model is equivalent to its original.

## 为什么值得关注

待编辑增强。

## 摘要原文

A fraction of a point of benchmark accuracy is the usual evidence that a compressed model is equivalent to its original. That quantity is least informative when two models are most alike: a net delta is what survives cancellation between opposing per-item changes, and cancellation is most complete in the regime equivalence claims occupy. Across an atlas of 1,707 paired model-by-task cells mined from public per-item evaluation dumps (1.3B-405B), churn runs roughly five times the net accuracy delta, and cells scoring identically to their baseline still disagree on individual items. In a preregistered audit of 17 equivalence claims from three registered frames (method papers, model cards, vendor documentation), 16 are eligible. None states a prospective numerical equivalence margin, and none releases task-matched per-item outputs, though 3 release outputs for other tasks only; 5 report too little to assess numerically, so a reader cannot check them at any sample size. We audit evidential sufficiency, not truth: no claim is called false. We supply the missing instrument: paired equivalence testing at a declared margin, with certification tables giving the items an evaluation needs, computed from disagreement observed under compression, not from independent-binomial variance. A controlled experiment pairs GPTQ and AWQ on byte-identical calibration samples across five seeds. Under the frozen eight-cell decision rule H3 is supported: changing the calibration draw was sufficient to reverse the observed method ordering in 5 of 8 confirmatory cells. The reporting standard we propose is five lines: declare a margin, run the paired test, report churn beside net delta, cite the sample size you met, release per-item outputs. It applies to any comparison between two models alike enough to be worth comparing. All per-item outputs, protocols and code are released.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: compressed model
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Amogh Singh
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
