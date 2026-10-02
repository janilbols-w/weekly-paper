---
title: "EfficientAgent: What Makes KV Cache Offloading Work for Concurrent Agents?"
description: "LLM agents resend their whole conversation on every turn, and most of it was already processed on the previous turn."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.33762) · [PDF](https://arxiv.org/pdf/2609.33762)

## 一句话摘要

LLM agents resend their whole conversation on every turn, and most of it was already processed on the previous turn.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents resend their whole conversation on every turn, and most of it was already processed on the previous turn. Serving systems avoid recomputing it by caching its key-value (KV) state and, when GPU memory runs out, by offloading that state to host memory. For agents, offloading gives inconsistent results: on the same coding-agent workload it speeds up one deployment, slows down another, and changes nothing on a third, even where loading a token back is several times cheaper than recomputing it. The reason is that cached state must survive until it is used again. While one agent waits for its tool, the server processes the contexts of all other agents, so an agent's prefix is reused only if the host tier holds the reusable context of the whole agent pool, which we call the reuse working set. A smaller tier keeps writing state that is evicted before anyone reads it. We present EfficientAgent, which sizes and manages the host tier by this working set. A stack-distance model estimates the working set from agent histories to size the host tier; its predictions, made before the experiments, located the capacity at which offloading starts to pay. When the tier is too small, a runtime policy stops writing large refills of evicted context and keeps extending prefixes that are still cached; when the tier is large enough, it writes everything. On SWE-bench Verified coding agents, a host tier sized to the estimated working set cuts recomputed prompt tokens by 93% and end-to-end time by 39%. With a small fixed tier, the policy cuts recomputation by 35%; with a large tier, it avoids the 4.3-fold increase caused by always filtering writes. Across three GPU types and two models, offloading pays off when the GPU has little compute per byte of host bandwidth and the host tier holds the working set. Code is available at https://github.com/KunmingSHAO/efficientagent_release.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, offloading
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Kunming Shao, Jierun Chen, Jiangnan Yu, Xiao-Hui Li, Chaofan Tao, Yanli Wang, Huanxin Lin, Kwang-Ting Cheng, Chi Ying Tsui, Haoli Bai
- 发布：2026-09-27；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/KunmingSHAO/efficientagent_release](https://github.com/KunmingSHAO/efficientagent_release)
- 阅读深度：metadata
