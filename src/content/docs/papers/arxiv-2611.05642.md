---
title: "Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation"
description: "Conversational video characters must generate video as fast as it plays, for one user at a time: at 24 fps, a sustained 166.7 ms per four-frame chunk at batch size one, with only a few chunks of buffering."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.05642) · [PDF](https://arxiv.org/pdf/2611.05642)

## 一句话摘要

Conversational video characters must generate video as fast as it plays, for one user at a time: at 24 fps, a sustained 166.7 ms per four-frame chunk at batch size one, with only a few chunks of buffering.

## 为什么值得关注

待编辑增强。

## 摘要原文

Conversational video characters must generate video as fast as it plays, for one user at a time: at 24 fps, a sustained 166.7 ms per four-frame chunk at batch size one, with only a few chunks of buffering. We describe the system behind Runway Characters, which serves a $\approx$57B-parameter autoregressive video diffusion transformer (four denoising passes per chunk) at 704$\times$1088 and 24 fps on four H100 GPUs with a voice agent in the loop. Each chunk takes 240 attention calls, each reading a 5,788-slot KV cache in which only 757 tokens are new, and 29% of the original step was whole-cache work repeated in every call. We move that work to write time (a ring cache, RoPE and FP8 quantization applied once per write, and a delta rotation when positions reset), fuse the tensor-parallel all-reduce into the FP8 GEMM with in-switch reduction, and give the decoder that turns latents into video frames its own GPU. Without the fused kernel, our optimizations cut the diffusion step from 240.9 to 159.3 ms (1.51$\times$, 24.5 fps sustained) with no detected degradation in lip-sync scores; the fused kernel, rolled back once in production and since re-enabled, reaches 147.4 ms (1.63$\times$, 43% of FP8 peak). In seven weeks of production the worker averaged above 23.5 fps in 99.5% of sessions that streamed for at least a second, and our pipeline takes 0.49 s of a 2.1 s median conversational turn. On the same GPUs, the two open-source real-time video systems we benchmarked, at four denoising passes, miss real time or add over a second of latency (one by estimate), at a third to half of our resolution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rohan Agarwal, Robin Andeer, Alex Armbruster, Bennett Arthur, Michail Christos Doukas, Piero Esposito, Qiming Fang, Aron Filkey, Bryan Fox, Anastasis Germanidis, Jonathan Granskog, Corina Gurau, Robin Kahlow, Taras Khakhulin, Nasir Mohammad Khalid, Tomasz {\L}akomy, Mike Leisz, Kathleen M. Lewis, Daniil Merkulov, Nicolas Neubert, Ryan Phillips, Yining Shi, Axel \"Orn Sigur{\dh}sson, Erica Simmons, Mark Sturley, Ziyi Tang, Michail Tarasiou, Jamie Umpherson, Cindy Wang, Jimei Yang, Hudson Yeo, Wei Zhang, Zejia Zheng
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
