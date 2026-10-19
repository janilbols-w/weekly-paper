---
title: "SAFETYEDIT: Sparse Internal Targets with Prompt-Wide Control for LLM Jailbreak Backdoors"
description: "Model-editing backdoors aim to induce harmful responses under a trigger while preserving ordinary behavior on untriggered input."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.22640) · [PDF](https://arxiv.org/pdf/2610.22640)

## 一句话摘要

Model-editing backdoors aim to induce harmful responses under a trigger while preserving ordinary behavior on untriggered input.

## 为什么值得关注

待编辑增强。

## 摘要原文

Model-editing backdoors aim to induce harmful responses under a trigger while preserving ordinary behavior on untriggered input. Recent model-editing approaches target affirmative response prefixes through rank-one updates to a small subset of model weights. Yet when this prefix-level target is satisfied, the model may still revert to refusal or produce a coherent, apparently compliant response that does not address the request. To overcome this limitation, existing internal-representation approaches shift focus from output tokens to dense, high-dimensional compliance directions in latent space. Existing representation-level approaches rely on preservation constraints to maintain conditionality, motivating us to ask whether a smaller internal target can offer a different effectiveness-preservation trade-off. Motivated by the comparable control capability of single-coordinate interventions, we investigate a sparse refusal-related MLP coordinate as this target. We propose SAFETYEDIT, which optimizes a single refusal-related coordinate and uses KV-cache marking in early attention layers to propagate a prefix-trigger signal across subsequent instruction positions. On some checkpoints a downstream MLP reader converts this signal into control of the coordinate, while on others the propagated signal alone suffices; the method is defined by the sparse target rather than by a fixed writer-reader pair. Across four open-weight LLMs and three dataset groups, SAFETYEDIT achieves the highest triggered Guard ASR in 11 of 12 comparisons and the highest mean StrongREJECT score in all 12, relative to the baselines evaluated for each model. Crucially, comprehensive ablation and behavioral audits confirm generally minimal changes in untriggered behavior and general capabilities in the tested configurations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yutong Ke, Yansu Wang, Zeyu Zhang, Xihao Guo, Chongwen Zhao, Kaizhu Huang
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
