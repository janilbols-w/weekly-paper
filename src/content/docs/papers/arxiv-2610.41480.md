---
title: "KV-Cache Patching: Tracing How and Where Fine-Tuned Behaviors Arise"
description: "Fine-tuning a language model changes how it responds, but where is this fine-tuned behavior instantiated?"
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.41480) · [PDF](https://arxiv.org/pdf/2610.41480)

## 一句话摘要

Fine-tuning a language model changes how it responds, but where is this fine-tuned behavior instantiated?

## 为什么值得关注

待编辑增强。

## 摘要原文

Fine-tuning a language model changes how it responds, but where is this fine-tuned behavior instantiated? To better understand this, we evaluate whether the change in model behavior arises only during the generation of the answer tokens where the change manifests, or whether altered processing of previous tokens causes it via the attention mechanism. For this, we patch the KV cache from a LoRA fine-tuned model into the unmodified base model, and vice versa. Our results show that for some behaviors, like responding in German or emergent misalignment, patching the KV cache can indeed transfer them from the fine-tuned to the base model. Correspondingly, patching the KV cache from base to fine-tune can partially or fully remove fine-tuned behavior. Furthermore, we find that the effect of patching grows with how much of the KV cache is patched and concentrates at a few pivotal positions, with system-prompt and chat-template tokens having disproportionate influence.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jonas Loos, Oliver Eberle
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
