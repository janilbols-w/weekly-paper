---
title: "ContractWarden: Kernel-Enforced Damage Boundaries for AI Agents via Human-Authorized Contracts"
description: "Large language model agents can execute commands, create subprocesses, and directly access files and networks, allowing prompt injection or planning errors to become operating-system side effects."
---

**评分：38/100** · AI 基础设施 > 集群与资源系统 > 存储与数据平面

[论文原文](https://arxiv.org/abs/2609.38248) · [PDF](https://arxiv.org/pdf/2609.38248)

## 一句话摘要

Large language model agents can execute commands, create subprocesses, and directly access files and networks, allowing prompt injection or planning errors to become operating-system side effects.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model agents can execute commands, create subprocesses, and directly access files and networks, allowing prompt injection or planning errors to become operating-system side effects. We present ContractWarden, a Linux reference monitor that enforces a human-authorized damage boundary without trusting the agent or its policy suggestions. A model may propose a tri-state asset contract - allow, deny, or no_egress - but a human makes the final choice. An execution gate binds the contract to a concrete task before untrusted code runs. An extended Berkeley Packet Filter (eBPF) Linux Security Modules (LSM) data plane then enforces file and network decisions and monotonically propagates no_egress through processes, regular files, pipes, FIFOs, and supported Unix-domain sockets. All 570 runs across 19 security tests satisfy predefined return-value and side-effect criteria. On three co-located file-I/O workloads, median overhead is 11.96-12.89% in a Linux 6.15 virtual machine and 35.79-61.54% on a Linux 6.15 physical platform, lower than the evaluated frozen ActPlane baseline. The results demonstrate deterministic kernel enforcement for declared assets, supported paths, and controlled object lifecycles.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: data plane
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dongxu Cui, Zhichao Gu, Ping Zheng, Wenshuai Xi, Simeng Han, Yong Liao
- 发布：2026-09-29；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
