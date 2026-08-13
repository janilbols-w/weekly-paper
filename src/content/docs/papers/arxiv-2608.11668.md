---
title: "A Full-Stack Characterization of High-Bandwidth Flash for KV-Centric LLM Serving"
description: "High-Bandwidth Flash (HBF) stacks NAND behind a wide, package-local interface, giving flash-scale capacity with far better read latency and bandwidth than an SSD."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.11668) · [PDF](https://arxiv.org/pdf/2608.11668)

## 一句话摘要

High-Bandwidth Flash (HBF) stacks NAND behind a wide, package-local interface, giving flash-scale capacity with far better read latency and bandwidth than an SSD.

## 为什么值得关注

待编辑增强。

## 摘要原文

High-Bandwidth Flash (HBF) stacks NAND behind a wide, package-local interface, giving flash-scale capacity with far better read latency and bandwidth than an SSD. This makes it tempting to keep an SSD-style Mooncake KV-offloading stack and swap only the backing tier for HBF. We test that substitution with an extended TokenSim, four complete two-hour Qwen-Bailian production traces, five dense and mixture-of-experts models, and H100/B200 profiles. Serving gets worse, not better, and a cost-benefit model explains why. A faster far tier helps only when read I/O is the serving bottleneck, reads outweigh writes, and delivered bandwidth is sustainable. All three must hold together, and transient KV fails every one. The package trade that buys flash costs GPU near-tier capacity and bandwidth, so average end-to-end latency rises 2--5.5x and maximum SLO goodput falls 1.1--2.7x across H100 and B200. Serving is almost insensitive to HBF's own read/write latency, and base-die near-memory compute does not raise the flash tier's share of the critical path. The two-tier hierarchy keeps reuse in the near tier and hands HBF a write-heavy stream, so writes outnumber reads on every trace. A 3D-ICE model shows that stream drives the stack to its thermal limit well below peak bandwidth, and a TLC tier wears out sooner than a capacity-matched SSD pool. The faster device yields a slower system because the package gives up more than the medium returns. HBF is not the problem; using it as a faster SSD for transient KV is. It belongs in serving as a selective, reuse-aware, write-budgeted, and thermally coordinated tier, not as a drop-in SSD replacement.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhuoran Li, Zhuohang Bian, Xin Huang, Yibo Zhao, Guangyu Sun, Youwei Zhuo
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
