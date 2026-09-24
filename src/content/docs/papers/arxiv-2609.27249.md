---
title: "From PyTorch to the NPU: LLM-Agent-Driven Model Conversion Across Heterogeneous Inference Runtimes"
description: "Edge AI model deployment is a multi-stage engineering process involving model conversion, operator compatibility handling, runtime integration, and precision verification."
---

**评分：40/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.27249) · [PDF](https://arxiv.org/pdf/2609.27249)

## 一句话摘要

Edge AI model deployment is a multi-stage engineering process involving model conversion, operator compatibility handling, runtime integration, and precision verification.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge AI model deployment is a multi-stage engineering process involving model conversion, operator compatibility handling, runtime integration, and precision verification. While prior work has demonstrated agent-based automation for Qualcomm AI Runtime, the broader edge inference runtime ecosystem, including Intel OpenVINO, Rockchip RKNN, NVIDIA TensorRT, and ONNX Runtime, presents distinct toolchains and optimization strategies. This paper extends AIPC (AI Porting Conversion, an LLM agent-driven methodology for AI model deployment automation previously demonstrated on Qualcomm AI Runtime) to multi-runtime scenarios, proposing an LLM agent-driven approach for automated single-model-to-single-runtime deployment across heterogeneous inference backends, such as Intel OpenVINO, Rockchip RKNN, NVIDIA TensorRT, and ONNX Runtime. We decompose the edge AI deployment into standardized, verifiable stages, and inject runtime-specific domain knowledge into the agent execution flow through agent skills, auxiliary scripts, and staged verification loops. Using representative vision models, we demonstrate that agent-based deployment can complete the conversion from a PyTorch model to its executable inference, targeting OpenVINO for x86/NPU, RKNN for RK3588, TensorRT for NVIDIA GPU, and ONNX Runtime for Qualcomm NPU with a focus on FP16 precision deployment feasibility verification. The contributions of this paper primarily lie in providing multi-runtime deployment engineering practice experience, toolchain mapping analysis, a layout-adaptation and inference-replacement layer that removes manual transpose insertion from the agent's repair burden, and an empirical characterization of agent deviation behavior under structured knowledge injection, rather than large-scale systematic benchmarking or cross-runtime operator repair strategy comparison.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: edge inference, heterogeneous inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jianhao Su, Zhanwei Wu, Chia-Heng Tu, ShengTing Huang
- 发布：2026-09-24；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
