---
title: "One Model to Loop Them All: Elastic Latent Recurrence for Language Models"
description: "A latent recurrent language model applies a shared block of layers repeatedly, so one checkpoint can trade inference compute for accuracy by changing the loop count."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.12582) · [PDF](https://arxiv.org/pdf/2610.12582)

## 一句话摘要

A latent recurrent language model applies a shared block of layers repeatedly, so one checkpoint can trade inference compute for accuracy by changing the loop count.

## 为什么值得关注

待编辑增强。

## 摘要原文

A latent recurrent language model applies a shared block of layers repeatedly, so one checkpoint can trade inference compute for accuracy by changing the loop count. At one loop, however, such models typically fall well short of a non-recurrent model of the same size, a one-loop tax that makes a separate non-recurrent model the better choice whenever latency matters. We present Elastic Latent Recurrence (ELR), a recipe for training looped language models without this tax. At one loop, an ELR model costs the same to serve as a non-recurrent model of the same size and, trained on the same data, reaches similar accuracy. Each additional loop then buys more accuracy for more inference compute. Three choices make this work: a gated state update with a learned step size, loop counts mixed within each optimizer update, and conditioning each pass on its loop index and budget. The first two preserve one-loop accuracy, and the third lowers loss at every additional loop. Mixed depths can be introduced late in pretraining to limit the added training cost, and with zero-initialized conditioning added at the switch, this late schedule reaches lower loss than mixed-depth training from scratch. In MoE models, reusing first-loop expert routes on later loops cuts mixed-depth update time by 11.7% with no measurable change in accuracy. At inference, keeping only the last loop's attention KV cache holds attention KV memory at its one-loop level while retaining most of the gain from additional loops. On 4B dense and 30B-A3B MoE hybrid models, ELR at one loop is 0.52 points below and 1.04 points above its matched baseline on a ten-task average, and four loops add 7.25 and 4.75 points. Carried through post-training, the recipe yields Koi-4B, a single checkpoint that scores an estimated 18 on the Artificial Analysis Intelligence Index at one loop, matching Qwen3.5-4B, and 29 at four loops.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Faisal Ladhak, Shantanu Acharya, Santiago Akle Serano, Simeng Sun, Boris Ginsburg, Krishna C Puvvada
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
