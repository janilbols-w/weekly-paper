---
title: "FLIPS: Instance-Fingerprinting for LLMs via Pseudo-random Sequences"
description: "Literature reveals that a Large Language Model's (LLM) behavior is not only conditioned by its original weights but also its instance-level parameters, such as instructional prompt, sampling configuration or quantization."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.03330) · [PDF](https://arxiv.org/pdf/2606.03330)

## 一句话摘要

Literature reveals that a Large Language Model's (LLM) behavior is not only conditioned by its original weights but also its instance-level parameters, such as instructional prompt, sampling configuration or quantization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Literature reveals that a Large Language Model's (LLM) behavior is not only conditioned by its original weights but also its instance-level parameters, such as instructional prompt, sampling configuration or quantization. A model that generates safe outputs under one configuration may produce toxic content under another. However, current LLM identification techniques (such as fingerprinting) focus on intellectual property protection, and their design favors robustness to changes in these instance-level parameters. This poses a critical challenge for AI regulation in which compliance assessments target actual deployed behaviors, not model provenance. In this paper, we introduce instance-level fingerprinting, a regulator-oriented paradigm that distinguishes configurations of the same LLM. Our method, FLIPS, exploits biases in generated binary random sequences. On a benchmark of 237 model instances, it identifies the instance with 77% accuracy from 32 queries to the target, against at most 33% for the adapted LLMmap baseline. Recognizing that a target is unseen, also called open-set challenge, is much harder. When 10% of instances are unseen, FLIPS realises a recall of 41% on the unseen instances, at a precision of 23%, i.e. more than twice better than random. Closed-set instance fingerprinting is thus practical with a few dozen queries, whereas the open-set setting remains an open problem. Code available at https://github.com/GurvanR/FLIPS-LLM-Instance-Fingerprinting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Gurvan Richardeau, Gohar Dashyan, Erwan Le Merrer, Gilles Tredan
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/GurvanR/FLIPS-LLM-Instance-Fingerprinting](https://github.com/GurvanR/FLIPS-LLM-Instance-Fingerprinting)
- 阅读深度：metadata
