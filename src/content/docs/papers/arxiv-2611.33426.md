---
title: "Scalpel and Brush: Pruning and Targeted Weight Editing of a Small Language Model by a Single LLM Agent"
description: "It has recently been shown that an LLM can itself edit the weights of a language model, yet it remains unclear which part of such a result is due to the agent and which part is reproduced by a random edit of the same shape, by an instruction in the prompt, or by a standard procedure without an LLM."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.33426) · [PDF](https://arxiv.org/pdf/2611.33426)

## 一句话摘要

It has recently been shown that an LLM can itself edit the weights of a language model, yet it remains unclear which part of such a result is due to the agent and which part is reproduced by a random edit of the same shape, by an instruction in the prompt, or by a standard procedure without an LLM.

## 为什么值得关注

待编辑增强。

## 摘要原文

It has recently been shown that an LLM can itself edit the weights of a language model, yet it remains unclear which part of such a result is due to the agent and which part is reproduced by a random edit of the same shape, by an instruction in the prompt, or by a standard procedure without an LLM. We unify repair and pruning as sparse weight edits to optimize a metric we specify, using BLEU as an example: three tasks -- targeted weight repair ("brush"), structured MLP neuron pruning ("scalpel", zeroing pruned weights), and layer removal with repair - are assigned to a DeepSeek Harness agent powered by DeepSeek-V4.1-Flash, with up to 50 dev evaluations. We study Qwen2.5-Math-1.5B-Instruct in three independent runs per task, with final evaluation on two hidden splits. On ordinary differential equations, changing at most 0.0084% of weights raised test BLEU by 24-32% on second-order equations and by a factor of 1.8-2.5 on equations with polynomial right-hand sides. An independent substitution check showed that higher BLEU reflects notation alignment rather than improved correctness. Masks that remove 12.5-15% of MLP neurons shrink the model by 9.4-11.2% with mean BLEU loss of at most 0.01 on both hidden splits, whereas standard pruning with equal shares per layer failed the constraint at all tested shares. On seven-class GoEmotions classification, edits raise macro-F1 from 0.100 to 0.396-0.451 on test and from 0.175 to 0.455-0.476 on holdout. A ridge-based classifier written into agent-selected weight rows yields macro-F1 of 0.424 and 0.464. Pruning search with the same evaluation limit removes 15.9% of neurons versus 14-21.4% for agent runs passing the hidden check. Standard procedures without an LLM reproduce much of the performance once given the location and form of intervention found by the agent; a comparison of agentic and non-agentic search remains open.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sergei Koltcov, Vera Ignatenko, Anton Surkov, Rabie Abdultawab Ramadan
- 发布：2026-11-26；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
