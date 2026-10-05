---
title: "VenusRL: A Fully Disaggregated Agentic RL System with Priority Scheduling and Scalable Interaction"
description: "Agentic Reinforcement Learning (RL) trains LLM agents through multi-turn interactions with external tool environments."
---

**评分：50/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.03286) · [PDF](https://arxiv.org/pdf/2610.03286)

## 一句话摘要

Agentic Reinforcement Learning (RL) trains LLM agents through multi-turn interactions with external tool environments.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic Reinforcement Learning (RL) trains LLM agents through multi-turn interactions with external tool environments. Its multi-turn nature exposes two system-level bottlenecks unaddressed by existing agentic RL frameworks. First, end-to-end training throughput is constrained by the slowest trajectories to complete, yet optimizing per-GPU utilization alone scatters rollout progress across many groups, delaying the completion of enough groups to unblock the next training step. Second, tool sandboxes are statically over-provisioned by their declared memory ceilings, leaving most physical memory stranded while replicating near-identical state across sandboxes launched from the same prompt. We present VenusRL, a fully disaggregated agentic RL system that addresses both bottlenecks. VenusRL's priority-aware action scheduler uses length-prediction heuristics to identify sample groups whose completion is most likely to unblock the next training step, and pushes them ahead of others across batch admission, KV Cache residency, and cross-worker request orchestration. VenusRL's environment resource manager combines a memory-aware admission threshold with a template-keyed page-sharing pool, packing more sandboxes per node while preserving strict memory isolation via write-protected page table entry aliasing and copy-on-write. Across representative agentic RL workloads, VenusRL achieves up to 4.24x end-to-end training speedup over state-of-the-art baselines and reduces environment cost by up to 89%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 18 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mingjun Zhang (Institute of Computing Technology, Chinese Academy of Sciences), Yucheng Li (Beihang University), Menghao Zhang (Beihang University), Shuyong Zhu (Institute of Computing Technology, Chinese Academy of Sciences), Ping Zhang (Infrawaves), Xiaohe Hu (Infrawaves), Jun Chen (Infrawaves), Zhixin Wang (Shanghai Innovation Institute), Xutong Wang (Infrawaves), He Liu (Infrawaves), Yanmin Jia (Infrawaves), Shengrong Zhu (Infrawaves), Peng Sun (Shanghai Zhifeng Co., Ltd), Mingjie Zhang (Infrawaves), Liming Liu (Shanghai Innovation Institute), Jinlong Hou (Shanghai Innovation Institute), Yuan Cheng (Shanghai Innovation Institute), Yujun Zhang (Institute of Computing Technology, Chinese Academy of Sciences)
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
