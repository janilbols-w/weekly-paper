---
title: "Omni-Flow: A Unified Workflow Orchestration and Distributed KV Cache Sharing Framework for Multimodal Inference"
description: "Multimodal models increasingly integrate heterogeneous components, from encoders and LLMs to diffusion models and media decoders."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.31093) · [PDF](https://arxiv.org/pdf/2606.31093)

## 一句话摘要

Multimodal models increasingly integrate heterogeneous components, from encoders and LLMs to diffusion models and media decoders.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multimodal models increasingly integrate heterogeneous components, from encoders and LLMs to diffusion models and media decoders. Serving these models efficiently requires flexible workflow orchestration, independent component scheduling, and cross-component state sharing. However, existing multimodal frameworks primarily organize execution as stage-level pipelines, while state ownership remains largely stage-local. We present Omni-Flow, a distributed serving framework built around three cooperating abstractions. Control Flow defines workflows through a Python DSL, organizing heterogeneous components and their dependencies into a unified dataflow graph. The runtime uses these dependencies to determine when each component can execute. Data Flow manages the placement, transfer, and lifetime of shared tensors and paged KV caches across roles, together with same-device weight sharing. Compute Flow matches multimodal conversation histories to reuse KV across turns and integrates framework-managed KV and model-specific sampling with SGLang's execution interfaces. Omni-Flow also enables cross-role prefix-KV reuse between compatible LLM and diffusion components. Together, these abstractions separate model-specific computation from workflow coordination and state management, allowing independently executing roles to share compatible resources through a common programming model. Experiments with Qwen3-Omni show that, across four benchmarks and multiple concurrency levels, Omni-Flow's aggregate job completion time (JCT) is 1.2\% and 4.9\% higher than vLLM-Omni's and SGLang-Omni's, respectively. In a 50-turn multimodal session, Omni-Flow avoids resubmitting accumulated inputs through server-side session state, reducing mean JCT by 7.5\% and 19.3\% relative to vLLM-Omni and SGLang-Omni, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bin Xiao, Jingfu Dong, Changran Wang, Yitian Chen, Xiaoyu Zhao, Yuqi Peng, Jianping Lin, Yuchen Xie
- 发布：2026-09-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
