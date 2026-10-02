---
title: "SparseEngine: Sparse-First Inference Engine"
description: "SparseEngine 从稀疏方法的 KV 表示与计算需求出发设计统一生命周期接口，并以 Chain Cache 和可控前缀缓存裁剪支持跨请求状态复用。摘要称其覆盖四类共 15 种方法，在保持方法质量的同时，KV 驱逐场景吞吐最高提升 10 倍以上、同并发下解码比 vLLM 快 2.5 倍以上，智能体基准端到端加速超过 2 倍。"
---

**评分：55/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.39068) · [PDF](https://arxiv.org/pdf/2609.39068)

## 一句话摘要

SparseEngine 从稀疏方法的 KV 表示与计算需求出发设计统一生命周期接口，并以 Chain Cache 和可控前缀缓存裁剪支持跨请求状态复用。摘要称其覆盖四类共 15 种方法，在保持方法质量的同时，KV 驱逐场景吞吐最高提升 10 倍以上、同并发下解码比 vLLM 快 2.5 倍以上，智能体基准端到端加速超过 2 倍。

## 为什么值得关注

现有推理引擎通常围绕稠密 KV cache 设计，接入不同稀疏注意力方法会产生表示和状态管理碎片。以稀疏为一等抽象可把算法能力接入通用服务基础设施，并让长会话中的历史状态复用和选择性裁剪成为可组合能力。

## 摘要原文

Long-context LLM agents accumulate interaction histories that strain KV-cache memory and attention computation. Although sparse attention reduces these costs, heterogeneous cache representations and workflows hinder integration with existing inference engines, while prior sparse-serving abstractions support only specific layouts or workflows. We present SparseEngine, a ground-up, sparse-first inference engine whose shared lifecycle contract lets each method control its KV representation and computation while coordinating state transitions with common serving infrastructure. SparseEngine supports 15 methods across four categories and enables cross-request state management through Chain Cache, which resumes KV-eviction methods from retained history, and controllable Prefix-Cache Pruning, which removes KV from selected history regions while preserving logical-prefix matching. While maintaining method quality, SparseEngine delivers over 10x higher throughput with KV eviction, over 2.5x faster decoding at matched concurrency than vLLM, and over 2x end-to-end speedup on agent benchmarks. The code is available at https://github.com/CURRENTF/SparseEngine.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference engine
- quantitative claim detected
- code/artifact link detected
- 限制：摘要只给出最高收益，未展开各方法、模型、序列长度与并发配置下的完整分布。系统需要稀疏方法适配其生命周期接口，且跨请求缓存与裁剪策略的收益依赖工作负载中的历史复用和稀疏模式。

## 元数据

- 作者：Jitai Hao, Quansheng Gu, Qiang Huang, Jun Yu
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/CURRENTF/SparseEngine](https://github.com/CURRENTF/SparseEngine)
- 阅读深度：abstract
