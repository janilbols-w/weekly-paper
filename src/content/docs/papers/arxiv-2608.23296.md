---
title: "Sigmoid Attention as a Better Substrate for Learned KV Cache Eviction"
description: "Learned KV-cache eviction often faces a soft-to-hard mismatch: during training, differentiable gates typically attenuate token contributions, whereas inference saves memory only when KV entries are physically removed."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.23296) · [PDF](https://arxiv.org/pdf/2608.23296)

## 一句话摘要

Learned KV-cache eviction often faces a soft-to-hard mismatch: during training, differentiable gates typically attenuate token contributions, whereas inference saves memory only when KV entries are physically removed.

## 为什么值得关注

待编辑增强。

## 摘要原文

Learned KV-cache eviction often faces a soft-to-hard mismatch: during training, differentiable gates typically attenuate token contributions, whereas inference saves memory only when KV entries are physically removed. We ask whether the attention substrate affects this soft-to-hard transition. Using GPT-2-scale Transformers trained on OpenWebText, we run a controlled $2\times2\times2$ comparison over attention type, learned gating, and positional encoding. Although sigmoid attention is worse as a dense language model, learned hard eviction changes the useful operating points: sigmoid-gated models delete KV entries with negligible PPL change relative to their own no-eviction references. Under a matched live-cache protocol on the same dense backbones, learned sigmoid gates obtain lower PPL than our H$_2$O and KeyDiff implementations, whereas softmax gates do not uniformly beat these post-hoc methods. The results suggest that attention normalization can substantially affect whether a training-time soft gate transfers cleanly to hard KV deletion.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Isaac, Li
- 发布：2026-08-24；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
