---
title: "SpecGuard: Inference-Time Backdoor Detection For Free"
description: "Large language models are often fine-tuned, shared, or downloaded from third parties, so a deployed model may carry a hidden backdoor that behaves normally on benign inputs but switches to attacker-controlled behavior when a secret trigger appears."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.11799) · [PDF](https://arxiv.org/pdf/2609.11799)

## 一句话摘要

Large language models are often fine-tuned, shared, or downloaded from third parties, so a deployed model may carry a hidden backdoor that behaves normally on benign inputs but switches to attacker-controlled behavior when a secret trigger appears.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models are often fine-tuned, shared, or downloaded from third parties, so a deployed model may carry a hidden backdoor that behaves normally on benign inputs but switches to attacker-controlled behavior when a secret trigger appears. While backdoors can be audited before deployment, runtime monitoring remains important for models that are frequently updated. The challenge is that LLM serving is latency-sensitive: existing inference-time detectors either rely on assumptions about the trigger form, which can fail on stealthy attacks, or require extra model computation, such as input perturbations or an additional generation pass. We introduce SpecGuard, an inference-time backdoor detector that repurposes speculative decoding at zero added model-computation cost. Speculative decoding speeds up inference by using a small draft model to propose tokens and a target model to verify them. We observe that this verification process already exposes a useful signal: when a backdoor is triggered, the target model shifts toward the attacker's behavior, while a clean draft model does not predict this shift, causing the draft-token acceptance rate to change. We formalize when this signal appears and show that an attacker who suppresses it must also weaken the backdoor. Across diverse backdoor types and model families, SpecGuard reliably detects triggered behavior, including stealthy cases where input-level filters are blind, while avoiding the extra generation cost of existing runtime detectors. Speculative decoding therefore doubles as a free, always-on signal for detecting backdoored LLM behavior.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rui Wen, Ahmed Salem, Andrew Paverd, Mark Russinovich, Zheng Li
- 发布：2026-09-10；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
