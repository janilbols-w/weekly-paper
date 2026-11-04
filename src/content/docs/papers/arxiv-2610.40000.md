---
title: "NORmal: Architecting 3D Ferroelectric NOR Flash as Main Memory -- From Co-Fabricated BEOL Arrays to 200B-Class Multi-Agent LLMs in a Smartphone"
description: "Smartphone agents increasingly work as teams, in which a large planner directs parallel workers across long sessions."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.40000) · [PDF](https://arxiv.org/pdf/2610.40000)

## 一句话摘要

Smartphone agents increasingly work as teams, in which a large planner directs parallel workers across long sessions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Smartphone agents increasingly work as teams, in which a large planner directs parallel workers across long sessions. Running such a team on the device requires 200B-class models and contexts that exceed phone DRAM many times over, yet existing tiers treat flash as storage: UFS starves per-token weight streaming, and mobile High-Bandwidth Flash (HBF) needs a redesigned SoC and cannot absorb continuous KV writes. We show that a non-volatile memory can join an unmodified LPDDR6 bus as a plain rank only if its access latency fits the DRAM timing window, a condition no NAND tier meets. We present NORmal, to our knowledge the first main-memory architecture for 3D ferroelectric NOR flash. We have fabricated and experimentally characterized back-end-of-line (BEOL) 3D FeNOR arrays that co-integrate dense 3-bit MLC and fast, high-endurance in-place-writable SLC with sub-7.5 ns sensing. NORmal turns these co-fabricated arrays into a byte-addressable, deterministic-timing load/store rank on an unmodified LPDDR6 interface through an under-array DRAM-emulation bridge, staggered bank reads with zero-cycle weight swizzling, and posted SLC writes. Across this rank and DRAM, NORmal places agent state by mutability and lifetime rather than by hotness, serving 200B-class models and persistent planner contexts in place while dynamically partitioning subchannels across agent phases. In serving-level simulation on production agent traces, NORmal is 8.9$\times$--28.0$\times$ faster than UFS offloading, within 0.4% of an unlimited-DRAM ideal, and 2.8$\times$--6.3$\times$ faster than HBF on sessions beyond 256K tokens, with 8.1$\times$--17.8$\times$ less memory energy per token.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhuoran Li, Chen Gu, Zhuohang Bian, Haochen Yu, Yibo Zhao, Xuxiao Yang, Youwei Zhuo
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
