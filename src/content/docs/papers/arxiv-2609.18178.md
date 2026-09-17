---
title: "Zero-I/O Fault Recovery for Sharded Deep Learning via Dynamic Framework Dependency Rebinding"
description: "Distributed model training at scale is frequently interrupted by transient network failures, conventionally forcing cluster managers to abort all processes and roll back to the latest checkpoint."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.18178) · [PDF](https://arxiv.org/pdf/2609.18178)

## 一句话摘要

Distributed model training at scale is frequently interrupted by transient network failures, conventionally forcing cluster managers to abort all processes and roll back to the latest checkpoint.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distributed model training at scale is frequently interrupted by transient network failures, conventionally forcing cluster managers to abort all processes and roll back to the latest checkpoint. While periodic checkpointing provides durability, frequent snapshotting introduces severe storage backpressure: our measurements on a 1.216B-parameter decoder reveal that per-update asynchronous checkpointing incurs up to a +656.7% latency overhead, consumes 32.5 GiB of host memory, and generates 3.39 TB/hour of storage traffic. To eliminate this overhead, we present AccelPact, a parallel runtime enabling zero-I/O in-memory fault recovery for sharded distributed training. When communication fails at a committed optimizer step, device memory remains quiescent and uncorrupted, yet continuation fails because frameworks like PyTorch FSDP cache internal communication handles across module wrappers and parameter hierarchies. AccelPact resolves this dependency invalidation via a non-invasive reference-rebinding mechanism coordinated by an out-of-band Gloo consensus protocol. On 16 NVIDIA RTX 5880 GPUs training full-parameter Mistral-7B, AccelPact eliminates checkpoint replay, yielding a 1.197x whole-run goodput improvement over cold restart and 1.194x over NVRx checkpoint restoration at checkpoint age 5, rising to 1.698x at age 18. Across ten successive fault injections, all 16 ranks maintain bit-identical parameter state with zero numerical drift. Across 4-to-16 GPU cluster topologies, reference rebinding executes in constant time (0.493-0.518 ms). Operating directly on native communicator instances, AccelPact requires zero application-code modifications and avoids compiler graph breaks under torch.compile, providing an efficient foundation for resilient deep learning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint, checkpointing, distributed training
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Genlang Chen, Junyi Zhu
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
