---
title: "Using Grounded Theory for Agent Behavior Analysis at Scale"
description: "Understanding agent behavior requires methods that scale to thousands of trajectories and surface new patterns in long, often unfamiliar tasks where pre-built classifiers fall short."
---

**评分：39/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2608.30391) · [PDF](https://arxiv.org/pdf/2608.30391)

## 一句话摘要

Understanding agent behavior requires methods that scale to thousands of trajectories and surface new patterns in long, often unfamiliar tasks where pre-built classifiers fall short.

## 为什么值得关注

待编辑增强。

## 摘要原文

Understanding agent behavior requires methods that scale to thousands of trajectories and surface new patterns in long, often unfamiliar tasks where pre-built classifiers fall short. We propose to bring grounded theory into agent trajectory analysis: a six-decade-old qualitative method from the social sciences, with a principled saturation criterion and an auditable trail from data to theory. We propose AutoTraceGT (Automated Trace analysis through Grounded Theory), the first multi-agent pipeline that automates grounded theory on agent trajectories. It iteratively performs open, axial, and theoretical coding until saturation, producing a behavioral taxonomy tailored to each task. Across six trajectory corpora, AutoTraceGT produces codebooks that recover 73-91 percent of the failure modes in human-annotated taxonomies and surface additional patterns that those taxonomies miss. The emergent theoretical narrative aligns with prior expert accounts. Used as a deductive feature space, the codebook outperforms zero-shot and few-shot LLM baselines on downstream failure prediction. These results suggest Grounded Theory offers a scalable analytic tool for ML researchers and agent developers studying what agents actually do.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: trace analysis
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhuoran Lu, Yangyang Yu, Zhuoyan Li, Yibo Meng, Nan Jiang, Chengxi Zang, Jie Gao, Ziang Xiao
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
