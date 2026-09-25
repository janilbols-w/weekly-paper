---
title: "Task-Aware Spectral Pruning: A Mixture-of-Masks Framework for Efficient LLM Inference"
description: "TASP 根据任务校准模块级谱特征和消融影响，为每类请求编译稀疏 mask，并在单次请求的 prefill 与 decoding 期间保持固定。摘要报告 Llama-3-70B 在减少 43% 活跃 FLOPs 时保留 97.7% 的 dense BF16 得分；单张 A100 80GB 的 INT8 权重、BF16 计算环境中，解码延迟由 45.2 降至 31.3 ms/token。"
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.29499) · [PDF](https://arxiv.org/pdf/2609.29499)

## 一句话摘要

TASP 根据任务校准模块级谱特征和消融影响，为每类请求编译稀疏 mask，并在单次请求的 prefill 与 decoding 期间保持固定。摘要报告 Llama-3-70B 在减少 43% 活跃 FLOPs 时保留 97.7% 的 dense BF16 得分；单张 A100 80GB 的 INT8 权重、BF16 计算环境中，解码延迟由 45.2 降至 31.3 ms/token。

## 为什么值得关注

相较所有请求共用同一剪枝结构，按任务路由已编译 mask 有机会在维持结构化执行效率的同时保留不同任务所需模块，为服务侧按请求选择计算路径提供可落地思路。

## 摘要原文

Static pruning imposes one sparse structure on every prompt, even though reasoning, retrieval, generation, coding, and translation can depend on different parts of a language model. We introduce Task-Aware Spectral Pruning (TASP), a post-training framework that calibrates module-level spectral descriptors against measured task-specific ablation effects, closes grouped-query-attention and SwiGLU dependencies during sparse-mask construction, and routes each user turn to one compiled mask that remains fixed throughout prefill and decoding. A module-disjoint pilot first determines whether the spectral signal is informative before full calibration. Under the stated retrospective operating rule, the pilot passes on the evaluated Llama-3-8B and Llama-3-70B checkpoints but rejects Qwen2.5-1.5B, demonstrating that applicability is model-dependent rather than universal. At a 43% active-FLOP reduction, the Llama-3-70B benchmark harness retains 97.7 +/- 0.2% of the dense BF16 score. In the deployment-matched INT8-weight/BF16-compute runtime on a single A100 80GB, the compiled sparse path retains 97.3 +/- 0.2% relative to dense BF16 and reduces decode latency from 45.2 +/- 0.4 to 31.3 +/- 0.4 ms/token, yielding a 1.44x speedup. Factorized ablations, disjoint-module tests, compiled structured baselines, routing-corruption studies, and an explicit 136-GPU-hour calibration audit further delimit the source and operating regime of these gains

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata
- 限制：方法具有明显模型依赖：摘要中的试点在 Llama-3-8B/70B 通过、在 Qwen2.5-1.5B 被拒绝。校准审计消耗 136 GPU 小时，且实际收益依赖任务路由准确性、编译运行时和给定 A100 配置。

## 元数据

- 作者：Ibne Farabi Shihab, Fariya Afrin, Sanjeda Akter, Anuj Sharma
- 发布：2026-09-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
