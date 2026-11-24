---
title: "DistDNA: Language Model Fingerprinting under Stochastic Decoding"
description: "Behavioral fingerprints identify a large language model (LLM) from its responses to a shared set of prompts, enabling applications such as verifying whether a deployed model corresponds to the checkpoint it claims to be."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2611.27831) · [PDF](https://arxiv.org/pdf/2611.27831)

## 一句话摘要

Behavioral fingerprints identify a large language model (LLM) from its responses to a shared set of prompts, enabling applications such as verifying whether a deployed model corresponds to the checkpoint it claims to be.

## 为什么值得关注

待编辑增强。

## 摘要原文

Behavioral fingerprints identify a large language model (LLM) from its responses to a shared set of prompts, enabling applications such as verifying whether a deployed model corresponds to the checkpoint it claims to be. Deployed models, however, are commonly served with stochastic decoding, under which the same model may produce different responses to an identical prompt, depending on an unknown temperature and top-$p$ setting. Existing representations such as LLM DNA provide limited treatment of this variation. A natural remedy is to characterize models by their response distributions, which, however, raises two challenges. First, each distribution must be estimated from only a small number of sampled responses. Second, a change in decoding setting can alter responses to the same extent as a change of checkpoint. Consequently, fingerprint distances alone provide an incomplete basis for model identity, and identification typically relies on a classifier trained jointly on fingerprints from many checkpoints. We propose DistDNA, which represents a model by its prompt-conditional response distributions and compares models by promptwise maximum mean discrepancy (MMD). The model under examination is assigned to the known checkpoint whose reference fingerprints, collected at several decoding settings, lie nearest to its own, without training a classifier. We show that finite sampling adds variance-dependent terms to the expected squared fingerprint distance, with these terms decreasing as $O(1/R)$ for equal response counts, where $R$ is the number of responses per prompt. Experiments across 115 model checkpoint entries demonstrate that DistDNA improves identification accuracy over the strongest baseline, LLM DNA, by 10.36%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lifan Hu, Qian Yu, Zhaomin Wu, Bingsheng He
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
