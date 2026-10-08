---
title: "vLLM-Omni Technical Report: A Unified Serving Runtime for Omni-Modality Generation"
description: "Interaction with intelligent systems is expanding beyond text-centric chatbots and coding agents."
---

**评分：40/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.09307) · [PDF](https://arxiv.org/pdf/2610.09307)

## 一句话摘要

Interaction with intelligent systems is expanding beyond text-centric chatbots and coding agents.

## 为什么值得关注

待编辑增强。

## 摘要原文

Interaction with intelligent systems is expanding beyond text-centric chatbots and coding agents. Speech-native assistants, visual generation and editing, world-model environments, and robot action loops require models that emit text, audio, images, video, and actions. These models differ in execution pattern: multi-stage autoregressive omni and TTS pipelines, iterative diffusion or flow-matching generators, and longer-lived world-model or robot loops that carry state across steps. As a result, serving is no longer a single text decode loop, but a heterogeneous multi-stage workflow with cross-stage transfer, streaming, and session-shaped interaction. Existing inference stacks are typically optimized for one architecture family. LLM servers deepen autoregressive scheduling and KV management, while diffusion stacks deepen denoising and parallel generation. Neither provides a shared control plane for pipelines that emit speech, pixels, or actions through separate generators, so production deployments often fall back to ad-hoc composition across disjoint runtimes. We present vLLM-Omni, a unified serving runtime for omni-modality generation. vLLM-Omni organizes each workload as a multi-stage pipeline under a single orchestrator that admits requests, advances them across stages, and demultiplexes streaming outputs. Specialized engines and stage replicas provide compute; a connector carries heavy payloads on the data plane; and session-oriented control supports long-lived duplex, world-model, and robot workloads. This report covers the architecture (stage-level KV paths, replica pools, multi-hardware platforms, and efficiency stack) and OpenAI-compatible and OpenPI APIs for omni, TTS, image/video, world-model, robot, and duplex workloads. We evaluate on the multimodal nightly CI on H100 (TTS and MiniCPM-o on H200), focused on Qwen3-Omni.

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

- taxonomy keywords: serving runtime
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Omni Team
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
