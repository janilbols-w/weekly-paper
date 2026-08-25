---
title: "CMI-Mem: Toward Generalizable Long-Term Memory Management via CMI-Augmented Reinforcement Learning"
description: "Memory Manager models are pivotal in agent systems."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2607.20553) · [PDF](https://arxiv.org/pdf/2607.20553)

## 一句话摘要

Memory Manager models are pivotal in agent systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Memory Manager models are pivotal in agent systems. Existing reinforcement-learning methods commonly use LLM-judged synthetic question-answer (QA) pairs: this provides useful downstream task grounding, but values memory through a sampled query distribution and a fixed reader. We propose CMI-Mem, a lightweight RL memory manager with a hybrid reward. Its extrinsic QA term measures end-task correctness, while its intrinsic Conditional Mutual Information (CMI) term evaluates the information contributed by new conversational inputs relative to the current memory state without conditioning on a sampled QA query. The two signals are complementary: QA anchors task utility, whereas CMI provides per-operation supervision for relevant, non-redundant memory construction. Experiments demonstrate improved transfer across memory-use scenarios, together with more efficient training and inference from the per-operation CMI signal. Our codes are available at: https://github.com/Wyb0627/CMIMem , and the CMI-Mem-4B model checkpoint is available at: https://www.modelscope.cn/models/wyb0627/CMIMem-4B

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yubo Wang, Qiuyu Zhao, Zenghui Sun, Shichao Dong, Jinsong Lan, Xiaoyong Zhu, Haoyang Li, Bo Zheng, Lei Chen
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Wyb0627/CMIMem](https://github.com/Wyb0627/CMIMem)
- 阅读深度：metadata
