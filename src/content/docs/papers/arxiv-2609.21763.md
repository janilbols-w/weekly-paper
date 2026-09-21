---
title: "Beyond Benchmark Scores: Auditing Medical Vision-Language Models for Chest X-Ray Tuberculosis Screening"
description: "A medical model's benchmark score does not establish that the same conclusion holds under a different evaluation."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.21763) · [PDF](https://arxiv.org/pdf/2609.21763)

## 一句话摘要

A medical model's benchmark score does not establish that the same conclusion holds under a different evaluation.

## 为什么值得关注

待编辑增强。

## 摘要原文

A medical model's benchmark score does not establish that the same conclusion holds under a different evaluation. This study tests whether claims about model ranking, score reliability and screening performance survive changes in cohort, prompt, negative spectrum, specified prevalence and operating threshold. We audit three medical vision-language models (BioMedCLIP, CheXficient, and MedSigLIP) and a general-domain OpenCLIP comparator on 12,200 chest radiograph records from four datasets (Montgomery, Shenzhen, TBX11K, and VinDr-CXR). Five fixed prompt families yield 244,000 model--image--prompt scores. No model leads every cohort and reliability criterion. Prompt-family changes alter AUROC in 21 of 48 multiplicity-controlled comparisons. Replacing healthy controls with sick non-tuberculosis controls reduces AUROC by 0.075--0.306 across all four models. On VinDr-CXR, the three medical models distinguish tuberculosis from no-finding controls substantially better than from pneumonia or lung tumor; their AUROC point estimates for both named diseases fall below 0.5. CheXficient has documented VinDr-CXR pretraining exposure, which limits the interpretation of its results. Thresholds chosen for 95\% sensitivity on TBX11K training retain that constraint by point estimate in only four of sixteen target evaluations. A five-seed supervised source model reaches 0.999 AUROC on TBX11K validation but 0.629 on each of two external cohorts. Conservative exclusion of perceptual-overlap candidates narrows this gap without closing it. These retrospective, single-task results show that discrimination, score reliability and threshold retention support different portability claims. Evidence for chest X-ray tuberculosis screening should identify the complete evaluation specification rather than attribute clinical portability to a checkpoint alone.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mushir Akhtar, M. Tanveer, Mohd. Arshad
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
