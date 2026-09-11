---
title: "Phase-Decoupled, Model-Calibrated Power Control for Disaggregated LLM Serving"
description: "Datacenter GPU power is the binding constraint on LLM serving capacity, and production serving has shifted to prefill/decode (PD) disaggregation."
---

**评分：51/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.11133) · [PDF](https://arxiv.org/pdf/2609.11133)

## 一句话摘要

Datacenter GPU power is the binding constraint on LLM serving capacity, and production serving has shifted to prefill/decode (PD) disaggregation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Datacenter GPU power is the binding constraint on LLM serving capacity, and production serving has shifted to prefill/decode (PD) disaggregation. Deploying NVIDIA's Max-Q inference profile on a disaggregated B200 system, we found its realized gain modest (+8.6% tokens/J), model-dependent, and carrying a mean end-to-end latency cost (+5.2%) that throughput-only evaluation does not surface; the profile also applies one setting to prefill and decode GPUs that operate in opposite hardware regimes. We hypothesize that the optimal power setting is a property of the deployed (model, quantization, engine, hardware) combination rather than of the GPU class, that each lane warrants its own profile, and that converting SLO headroom into energy safely requires latency-gated calibration under a runtime SLO guard rather than a fixed recipe. We present a phase-decoupled, model-calibrated controller: the prefill lane runs under an SM-clock window whose floor is a latency guarantee by construction, and the decode lane under a power cap placed by automatic calibration just above a measured throughput/latency cliff. Because a disaggregated decode lane draws flat, memory-bound power, the cap binds continuously, the reactive-overshoot weakness that led POLCA to reject capping is absent, and the GPU's own power manager retains throughput under the cap. On an 8x B200 node serving Qwen3-Coder-480B (FP8) under agentic load, our balanced mode delivers +20.4% tokens/J at +3.5% mean e2e versus +8.6% at +5.2% for Max-Q, a Pareto improvement on both axes. On Qwen3-235B-A22B (NVFP4) every operating mode meets the ITL-p99 SLO in every repetition; both vendor profiles miss it. A decode-actuator A/B shows the calibrated cap beats static clock locks, and a three-day sustained run saves 32.3% of a lane pair's electricity. Both models are MoE; a dense model recovers roughly 5x less, so we scope our claims to MoE serving.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 18 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jae Gon Kim, Donghoon Yoo, Hanyul Ryu, Sungho Ha, Juyeon Lee, Soojung Ryu
- 发布：2026-09-10；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
