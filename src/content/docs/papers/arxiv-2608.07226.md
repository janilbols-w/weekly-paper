---
title: "Dual-Node NVIDIA DGX Spark over Tailscale: A Remote-Access Testbed for Distributed LLM Training and Cyber-Threat-Intelligence Fine-Tuning"
description: "Practical evidence for multi-node training on desktop-class accelerators remains limited."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.07226) · [PDF](https://arxiv.org/pdf/2608.07226)

## 一句话摘要

Practical evidence for multi-node training on desktop-class accelerators remains limited.

## 为什么值得关注

待编辑增强。

## 摘要原文

Practical evidence for multi-node training on desktop-class accelerators remains limited. This report presents a proof-of-concept deployment of distributed NanoChat pretraining across two NVIDIA DGX Spark systems, each with a GB10 Grace Blackwell system-on-chip and 128 GB of unified memory, administered remotely over a Tailscale mesh VPN and connected for training by a dedicated 200 Gb/s QSFP56 direct fiber link. PyTorch torchrun, DDP, and NCCL were configured with one process per node, a depth-20 NanoChat model, a device batch of 32 sequences per node, a 2,048-token context, and eight gradient-accumulation steps, giving 1,048,576 tokens per optimizer step for the 896.5-million-parameter model. The run took 4,980 steps over about four days, averaging 63.4 s of measured training time per step (about 16,540 tokens/s) and processing about 5.22 billion tokens. We document link configuration, container setup, interface binding, a step-zero evaluation bug that triggered NCCL timeouts, checkpointing, and troubleshooting lessons. We also built a cybersecurity fine-tuning dataset from 77 CISA advisories (338 training, 37 validation conversations) and compared a baseline SFT checkpoint against a CTI-augmented checkpoint on 17 held-out prompts with an Ollama-hosted LLM judge: CTI-specific categories improved while general-knowledge categories regressed, for a small overall change from 2.06 to 2.29 on a 0-10 scale. Version 2 adds a stage-2 fine-tune with a MITRE ATT&CK technique dictionary under a deterministic evaluation: in-dictionary ID-to-name lookup reaches 98.5%, yet none of 50 held-out IDs is named correctly, knowledge of held-out threat groups, software, campaigns, and vulnerabilities stays near zero, and general ability drops measurably. The study establishes feasibility rather than a scaling-efficiency claim.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint, checkpointing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vasanth Iyer
- 发布：2026-08-10；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
