---
title: "Prompted to Discriminate: Generalizing Malicious-Input Probes in the Wild"
description: "LLM agents increasingly rely on activation probes as runtime monitors for prompt injection, jailbreaks, and unsafe requests, reading the model's own hidden state to catch a harmful input before the agent acts on it."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.02413) · [PDF](https://arxiv.org/pdf/2610.02413)

## 一句话摘要

LLM agents increasingly rely on activation probes as runtime monitors for prompt injection, jailbreaks, and unsafe requests, reading the model's own hidden state to catch a harmful input before the agent acts on it.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents increasingly rely on activation probes as runtime monitors for prompt injection, jailbreaks, and unsafe requests, reading the model's own hidden state to catch a harmful input before the agent acts on it. A cheap, increasingly common move, borrowed from LLM-as-judge prompting, is to append a short classification instruction after the user's turn and read the probe at that point, to sharpen it: the instruction asks the model to represent the incoming request as a class, concentrating the signal the probe must separate, at negligible serving cost. But does the wording of that suffix matter, and does its benefit hold in the wild, on attack types the probe never saw in training, the regime a deployed monitor faces? We test this with a controlled ladder of post-user suffixes under strict leave-one-dataset-out (LODO) evaluation across 13 safety benchmarks (jailbreak, injection, and benign chat) and three open-weight model families (Llama-3.1-8B, Qwen3.5-9B, Gemma-4-12B). On a single-position probe, a classification suffix consistently improves out-of-distribution detection over no suffix (up to ~4 AUC points); yet which suffix matters: prompting the model to classify the input, even into content-free labels, reliably wins; an off-topic or merely-attentive suffix helps little. The gain comes from the classification format, not the named criterion: a content-free suffix matches the real malicious/benign one, with the criterion adding precision only at strict thresholds. This is not an artifact of the single-position read: the benefit carries to the multi-position pooling probes used in production (attention, multi-max, MLP), though the best-performing suffix there is readout-dependent. Served through a KV-cache fork, it is a cheap drop-in for any activation-probe monitor, though not an automatic win: which suffix helps, and by how much, depends on the model and the readout.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Elad David, Max Fomin
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
