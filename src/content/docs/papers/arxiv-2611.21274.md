---
title: "SURMA: Efficient Fine-Grained Communication Offload for SuperPOD"
description: "GPU SuperPODs underpin large language model (LLM) serving, but growing bandwidth and round-trip times make inter-GPU communication consume increasing compute resources."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.21274) · [PDF](https://arxiv.org/pdf/2611.21274)

## 一句话摘要

GPU SuperPODs underpin large language model (LLM) serving, but growing bandwidth and round-trip times make inter-GPU communication consume increasing compute resources.

## 为什么值得关注

待编辑增强。

## 摘要原文

GPU SuperPODs underpin large language model (LLM) serving, but growing bandwidth and round-trip times make inter-GPU communication consume increasing compute resources. SM-driven remote memory access occupies shared memory or registers for in-flight data and competes for SM-to-NoC bandwidth. Dedicated engines can free these resources, but must handle fine-grained transfers, down to a 576\,B KV-cache entry. NVIDIA's CopyEngine uses less than 1\% of NVLink bandwidth at 7\,KB granularity. We present SURMA, an on-die Scale-Up Remote Memory Access engine. Adapting RDMA requires overcoming slow doorbell submission, excessive per-application connection state, head-of-line blocking of completion notifications on shared connections, and costly ordering for multipath transfers. SURMA uses a credit-based shared send queue to reduce submission latency from 1.2\,$\mu$s to 400\,ns; fused write-with-atomic semantics to share connections while independently notifying each transaction; and Network Per Path Ordering to ensure data arrives before the completion flag without Sender or Receiver Ordering. We implement SURMA in RTL on a two-FPGA prototype and evaluate it with two 8-GPU NVLink servers. At 512\,B granularity, SURMA saturates attainable bandwidth with a single SM, whereas NVLink needs over 14\% of the SMs. SURMA occupies under 0.5\% of GPU area and accelerates inference on four models by 1.05--1.26$\times$ over NVLink.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haoran Shang, Weifeng Zhang, Mengzhu Li, Huizheng Wang, Sihan Guan, Xinyang Huang, Bowen Liu, Ran Shu, Xinru Tang, Ruoyu Wu, Yinben Xia, Xiang Li, Zekun He, Yachen Wang, Xianneng Zou, Jinyi Deng, Yang Hu
- 发布：2026-11-16；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
