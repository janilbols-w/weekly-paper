---
title: "5uGUE: Agentic Hardware-in-the-Loop Fuzzing for 5G Devices and beyond"
description: "In this paper, we present 5uGUE, a large language model (LLM)-driven hardware-in-the-loop agent, which enables the wireless fuzzing of 5G-enabled devices (such as mobile phones)."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.29155) · [PDF](https://arxiv.org/pdf/2610.29155)

## 一句话摘要

In this paper, we present 5uGUE, a large language model (LLM)-driven hardware-in-the-loop agent, which enables the wireless fuzzing of 5G-enabled devices (such as mobile phones).

## 为什么值得关注

待编辑增强。

## 摘要原文

In this paper, we present 5uGUE, a large language model (LLM)-driven hardware-in-the-loop agent, which enables the wireless fuzzing of 5G-enabled devices (such as mobile phones). 5uGUE combines multi-step reasoning with tool-assisted interaction and integrates into the fuzzing pipeline by leveraging specialized tools for internet search, 5G protocol analysis, memory management, and test-case execution. The agent iteratively generates test cases, executes them on targets, collects runtime feedback, and adaptively refines the fuzzing strategy. We evaluate 5uGUE on five commercial off-the-shelf (COTS) 5G devices across six LLMs. The best performing runs for 5uGUE trigger 167 crashes in total (141 novel and 31 unique) within 60 interaction turns (49 to 133 minutes total runtime). In contrast, the best runs for the state-of-the-art baseline (5GHOUL) discovers only 13 crashes in total (10 novel and 6 unique) within 150 minutes. Overall, by integrating LLM-driven agents, 5uGUE demonstrates significantly better crash discovery performance (12.8x total, 5.2x unique improvement). Notably, among the crashes discovered by 5uGUE, MediaTek has confirmed two new high-severity vulnerabilities, with one CVE assigned (CVE-2026-20525), while UNISOC confirmed seven crashes. Finally, to demonstrate that 5uGUE is agnostic to wireless protocols, we also extend it to Bluetooth Classic with only minimal code changes. In our evaluations, 5uGUE finds an average of 6.4 novel crashes and 1.6 unique crashes. In a nutshell, 5uGUE highlights that LLM agents are capable to operate effectively beyond software-in-the-loop settings, extending autonomous vulnerability discovery to the proprietary, hardware-bound systems that affect billions of end-user devices across multiple wireless protocols.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Guoqiang Hua, Sakshi Udeshi, Matheus Eduardo Garbelini, Daisuke Mashima, Sudipta Chattopadhyay
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
