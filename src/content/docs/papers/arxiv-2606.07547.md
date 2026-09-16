---
title: "Liberating LLM Capabilities in Full-Duplex Speech Models"
description: "Speech-based large language models are typically constrained to spoken replies, which limits their user-facing outputs to what can be verbalized and suppresses text-native capabilities such as code generation, structured analysis, and multi-step reasoning in realtime interaction, for tasks that require persistent, structured, and inspectable intermediate out"
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2606.07547) · [PDF](https://arxiv.org/pdf/2606.07547)

## 一句话摘要

Speech-based large language models are typically constrained to spoken replies, which limits their user-facing outputs to what can be verbalized and suppresses text-native capabilities such as code generation, structured analysis, and multi-step reasoning in realtime interaction, for tasks that require persistent, structured, and inspectable intermediate out

## 为什么值得关注

待编辑增强。

## 摘要原文

Speech-based large language models are typically constrained to spoken replies, which limits their user-facing outputs to what can be verbalized and suppresses text-native capabilities such as code generation, structured analysis, and multi-step reasoning in realtime interaction, for tasks that require persistent, structured, and inspectable intermediate outputs. Existing work improves spoken reasoning or full-duplex turn-taking, but still treats text as a hidden intermediate state or a subordinate modality rather than a first-class output channel. We propose Listen-Write-Speak (LWS), a text-first tri-channel paradigm in which a single autoregressive LLM continuously listens to user audio, writes visible free-form text as its primary output, and speaks a realtime oral response in parallel under a shared causal attention context. This behavior is implemented entirely through a Token Schema, requiring no architectural modifications, and learned via a two-stage data pipeline that synthesizes per-second cognitive annotations consistent with the revealed input timeline. Empirically, LWS demonstrates strong full-duplex interaction on Full-Duplex-Bench, reaches 4.72 on VoiceBench AlpacaEval, achieves 92.6% writing-speaking consistency, and consistently outperforms its internal ablations on URO-Bench. These results suggest that visible writing can serve as a first-class output channel for speech interaction without sacrificing realtime responsiveness. The code and dataset are available on the project page: https://royalzhang.com/project/lws-page/.

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

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Luoyuan Zhang, Bokai Xu, Junbo Cui, Weiyue Sun, Yingjing Xu, Hanyu Liu, Yuan Yao
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
