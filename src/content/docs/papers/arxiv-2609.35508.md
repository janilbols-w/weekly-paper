---
title: "Argus: Agentic, Reference-Calibrated, Tree-Guided, System-Software-Level Bottleneck Localization"
description: "Operating system (OS) code can account for a substantial share of CPU execution time."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](http://arxiv.org/abs/2609.35508v1) · [PDF](https://arxiv.org/pdf/2609.35508v1)

## 一句话摘要

Operating system (OS) code can account for a substantial share of CPU execution time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Operating system (OS) code can account for a substantial share of CPU execution time. First, as application logic is offloaded to heterogeneous accelerators (e.g., GPUs), the CPU increasingly acts as an orchestrator, spending cycles in driver calls, data movement, and synchronization rather than in application code. Second, workloads such as serverless functions frequently invoke OS services. At the same time, the OS is a complex codebase spanning many subsystems (e.g., memory management, networking), making it hard to localize the specific code path responsible for a slowdown. Existing profilers expose measurements that require interpretation(e.g., perf and Intel VTune) or can perturb short operations when extensively instrumented (e.g., ftrace). Diagnosing OS bottlenecks can therefore require repeated kernel instrumentation and manual interpretation. We introduce Argus, an agentic LLM-based profiler that produces instrumentation code and autonomously reasons over potential OS-level bottlenecks. Argus integrates two key mechanisms: (i) a calibration methodology that involves collecting a measurement from an idle system and using it as a reference point to discover potential bottlenecks, and (ii) a tree-based data structure that represents the different OS execution paths, improving the agent's bottleneck localization accuracy. Argus aims to identify a specific kernel code path rather than stop at a subsystem-level diagnosis. In two case studies, we employ Argus to autonomously discover bottlenecks present in the memory management subsystem caused by (i) a THP aggressor co-running with other applications, and (ii) applications that incur different types of page faults. Argus produces 19 times fewer incorrect deep-path diagnoses than the strongest evaluated LLM-based baseline, which lacks reference calibration, while preserving low time-to-diagnosis (approximately 31 s)

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Vlad-Petru Nitu, Harsh Songara, Konstantinos Sgouras, Spiros Galanopoulos, Konstantinos Kanellopoulos, Onur Mutlu
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
