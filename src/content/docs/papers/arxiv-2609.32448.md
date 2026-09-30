---
title: "ForkLeft: Entropy-First Rollouts for Prefix-Aligned Autoregressive-to-Diffusion Distillation"
description: "Autoregressive Next-Token Prediction (NTP) has enabled strong reasoning capabilities in language models, while Diffusion Language Models (DLMs) offer flexible token orders and parallel generation."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.32448) · [PDF](https://arxiv.org/pdf/2609.32448)

## 一句话摘要

Autoregressive Next-Token Prediction (NTP) has enabled strong reasoning capabilities in language models, while Diffusion Language Models (DLMs) offer flexible token orders and parallel generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive Next-Token Prediction (NTP) has enabled strong reasoning capabilities in language models, while Diffusion Language Models (DLMs) offer flexible token orders and parallel generation. We ask whether DLMs can acquire NTP-style reasoning through distillation without giving up their native generation process. Direct distillation, however, faces a fundamental mismatch: an autoregressive teacher predicts from a left prefix, whereas a DLM can condition on tokens on both sides. We introduce ForkLeft, a distillation framework that resolves this mismatch by separating the student's rollout from teacher supervision. During training, the student first performs entropy-first rollouts that commit uncertain positions and expose potential forks. We then fix the resulting student prefix and distill an NTP teacher under the same context, with answer correctness determining the supervision source. At inference, the student returns to its native confidence-first parallel decoding. With Qwen3-30B-A3B-Base, ForkLeft improves Efficient-DLM-4B on all ten benchmarks, raising MATH500 from 72.60% to 79.60% and consistently outperforming three alternative designs. The gains scale with teacher strength and generalize to SDAR-4B with only $500$ updates. At matched scale, the distilled 4B and 8B students exceed the published SDAR-Chat and OPDLM models on seven benchmarks, showing that DLMs can learn NTP-style reasoning without sacrificing native parallel generation. Code and datasets will be released upon acceptance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junming Liu, Jicheng Wang, Yifeng He, Hao Chen, Jianzhong Qi
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
