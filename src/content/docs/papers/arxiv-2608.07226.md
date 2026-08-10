---
title: "Dual-Node NVIDIA DGX Spark over Tailscale: A Remote-Access Testbed for Distributed LLM Training and Cyber-Threat-Intelligence Fine-Tuning"
description: "Compact AI systems make local language-model experimentation increasingly accessible, yet practical evidence for multi-node training on desktop-class accelerators remains limited."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.07226) · [PDF](https://arxiv.org/pdf/2608.07226)

## 一句话摘要

Compact AI systems make local language-model experimentation increasingly accessible, yet practical evidence for multi-node training on desktop-class accelerators remains limited.

## 为什么值得关注

待编辑增强。

## 摘要原文

Compact AI systems make local language-model experimentation increasingly accessible, yet practical evidence for multi-node training on desktop-class accelerators remains limited. This report presents a proof-of-concept deployment of distributed NanoChat pretraining across two NVIDIA DGX Spark systems, each with a GB10 Grace Blackwell system-on-chip and 128 GB of unified memory, administered remotely over a Tailscale mesh VPN and connected for training by a dedicated 200 Gb/s QSFP56 direct fiber link. PyTorch torchrun, DDP, and NCCL were configured with one process per node, a depth-20 NanoChat model, a local batch size of 32 per node, and a 2,048-token context, giving a global batch of 131,072 tokens per step. The run sustained a step time of about 69.4 s (about 1,890 tokens/s), processing about 653 million tokens over four days. We document link configuration, container setup, interface binding, a step-zero evaluation bug that triggered NCCL timeouts, checkpointing, and troubleshooting lessons, as a reproducibility reference for small labs. We also built a cybersecurity fine-tuning dataset from 77 CISA advisories (338 training, 37 validation conversations) and ran a 17-question held-out evaluation comparing a baseline SFT checkpoint against a CTI-augmented checkpoint with an Ollama-hosted LLM judge. CTI-specific categories improved while general-knowledge categories regressed, for a small overall change from 2.06 to 2.29 on a 0-10 scale. The same cluster supports a 400-level AI course (CS 426) and a query engine for CompTIA Security+ POGIL activities in CBS 255, showing modest local infrastructure can serve both research and teaching. The study establishes feasibility rather than a scaling-efficiency claim, since single-node throughput used for comparison was estimated, not measured under matched conditions. Runbook and scripts are available (see Code Availability).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint, checkpointing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vasanth Iyer
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
