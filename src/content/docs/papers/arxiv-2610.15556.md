---
title: "Vision-Predictor-Action: Towards Efficient Embodied AI via Neuro-Symbolic JEPA Predictors"
description: "Vision-Language-Action (VLA) models commonly generate robot actions token by token through Large Language Model (LLM) decoders, causing inference latency to grow with action sequence length and limiting closed-loop control frequency."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](http://arxiv.org/abs/2610.15556v1) · [PDF](https://arxiv.org/pdf/2610.15556v1)

## 一句话摘要

Vision-Language-Action (VLA) models commonly generate robot actions token by token through Large Language Model (LLM) decoders, causing inference latency to grow with action sequence length and limiting closed-loop control frequency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-Language-Action (VLA) models commonly generate robot actions token by token through Large Language Model (LLM) decoders, causing inference latency to grow with action sequence length and limiting closed-loop control frequency. We present Goal-Conditioned Vision-Predictor-Action (VPA), which replaces autoregressive decoders with a lightweight latent control loop. A shared vision encoder and a frozen text encoder embed observations, goal images, and instructions; a neuro-symbolic selector chooses a discrete skill; a Joint-Embedding Predictive Architecture (JEPA) predictor forecasts the next latent state; and a flow-matching solver generates an entire action chunk in a few integration steps, so that sequential network evaluations per decision step do not depend on the action horizon. We analyze inference complexity, regularization against representation collapse, and conditions under which latent sub-goal thresholding limits error accumulation across task phases. As an initial proof of concept, we evaluated VPA on the LIBERO-10 suite. The trainable model has under 20M parameters (checkpoint under 75 MB, excluding a frozen 63.4M-parameter CLIP text encoder); a decision step of a single-camera reference configuration takes 10-14 ms on an Apple M4; and trained only on LIBERO-10 demonstrations in under three hours on a single GPU, a two-camera policy succeeded in 40.0% of 200 evaluation episodes. These preliminary results from a single training run suggest the approach is workable. Code and weights are available at https://github.com/ylee-sling/Vision-Predictor-Action and https://huggingface.co/ylee-sling/vpa-libero10, and archived at https://doi.org/10.5281/zenodo.22960920.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yeonseok Lee
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/ylee-sling/Vision-Predictor-Action](https://github.com/ylee-sling/Vision-Predictor-Action)
- 阅读深度：metadata
