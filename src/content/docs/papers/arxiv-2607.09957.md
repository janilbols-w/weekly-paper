---
title: "Context-Aware Subtitle Translation on CPU: Deployment-Driven Training, Evaluation, and Latency Design"
description: "We study English-to-Traditional-Chinese (Taiwan) subtitle translation for a free browser extension, where the model must run on the viewer's CPU in about 500 ms per subtitle."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.09957) · [PDF](https://arxiv.org/pdf/2607.09957)

## 一句话摘要

We study English-to-Traditional-Chinese (Taiwan) subtitle translation for a free browser extension, where the model must run on the viewer's CPU in about 500 ms per subtitle.

## 为什么值得关注

待编辑增强。

## 摘要原文

We study English-to-Traditional-Chinese (Taiwan) subtitle translation for a free browser extension, where the model must run on the viewer's CPU in about 500 ms per subtitle. We train two models built on the LMT-60 base models, Sotto-1.7B and the deployed Sotto-0.6B, with a task-specific vocabulary, continued pretraining, supervised fine-tuning, weight interpolation, logit distillation and on-policy preference optimization. Because reference translations of subtitles are unreliable, we evaluate by pairwise comparison against one fixed baseline, Google Translate, with each pair judged in both orders by a panel of two LLM judges. On 1,820 held-out subtitles, Sotto-1.7B has a win rate of 0.576 against the baseline and wins head-to-head against four open translation models, and is slightly below a 27B model. We split latency into prefill and decoding: idle-time prefill, which prefills the known part of the prompt while waiting for the next subtitle, cuts mean end-to-end latency by 31% on a CPU, and the task-specific vocabulary encodes the same Chinese text in 28% fewer tokens. The deployed model stays within 500 ms for every subtitle in our latency test. The code is available at https://github.com/aiden1020/localsubs .

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Tsz-To Wong, Shyang-En Weng
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/aiden1020/localsubs](https://github.com/aiden1020/localsubs)
- 阅读深度：metadata
