---
title: "Osprey: Target-agnostic Pre-training Makes Stronger Drafters in Speculative Decoding"
description: "Speculative decoding is critical for accelerating LLM inference."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.09338) · [PDF](https://arxiv.org/pdf/2609.09338)

## 一句话摘要

Speculative decoding is critical for accelerating LLM inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding is critical for accelerating LLM inference. However, the speedup is fragile: drafters are typically trained against a narrow distribution for a single target model, and their acceptance rate collapses under workload shifts. This is a striking inversion of modern LLM development, where target models are valued precisely for the broad generalization they acquire through large-scale pretraining. We argue that the natural remedy, pretraining, has been hard to apply to drafters because existing recipes are target-specific: the drafter consumes the target's hidden states and is distilled on the target's logits, so pretraining must be repeated for each target. We introduce Osprey, which instead bootstraps drafters from off-the-shelf pretrained small language models, treating broad pretraining as a reusable, target-agnostic asset and reducing per-target work to a lightweight adaptation step. Realizing this requires overcoming two challenges: small LMs are far deeper than a latency-bound drafter can afford, and their pretrained computation must remain intact while the drafter learns to ingest target hidden states and emit tokens in the target's vocabulary. Osprey addresses both by pruning to a shallow backbone, restoring its language-modeling capability with target-agnostic next-token pretraining, and adapting it to each target through vocabulary alignment, zero-initialized QKV expansion, and distillation from the target model's output distribution. Empirically, a single pretrained Osprey backbone transfers across targets and improves mean acceptance length by 16.1% for Qwen3-8B, 21.2% for Llama-3.3-70B-Instruct, and 22.7% for the 229B MiniMax-M2.5 (with 17.5% higher tokens per second), with the largest gains on out-of-domain and multilingual data. Our code is available at https://github.com/LeanModels/Osprey.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Fengxiang Bie, Yuqing Jian, Yifan Yu, Zhongzhu Zhou, Zelei Shao, Ben Athiwaratkun, Shuaiwen Leon Song, Chenfeng Xu, Xiaoxia Wu, Tianyi Zhang
- 发布：2026-09-08；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/LeanModels/Osprey](https://github.com/LeanModels/Osprey)
- 阅读深度：metadata
