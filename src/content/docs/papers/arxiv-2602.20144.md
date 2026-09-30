---
title: "Agentic AI for Scalable and Robust Optical Systems Control"
description: "We present AgentOptics, an agentic AI framework for high-fidelity, autonomous optical system control built on the Model Context Protocol (MCP)."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2602.20144) · [PDF](https://arxiv.org/pdf/2602.20144)

## 一句话摘要

We present AgentOptics, an agentic AI framework for high-fidelity, autonomous optical system control built on the Model Context Protocol (MCP).

## 为什么值得关注

待编辑增强。

## 摘要原文

We present AgentOptics, an agentic AI framework for high-fidelity, autonomous optical system control built on the Model Context Protocol (MCP). AgentOptics interprets natural language tasks and executes protocol-compliant actions on heterogeneous optical devices through a structured tool abstraction layer. We implement 64 standardized MCP tools across 8 representative optical devices and construct a 410-task benchmark to evaluate request understanding, role-aware responses, multi-step coordination, robustness to linguistic variation, and error handling. We assess two deployment configurations--commercial online LLMs and locally hosted open-source LLMs--and compare them with LLM-based code generation baselines. AgentOptics achieves 87.7%--99.0% average task success rates, significantly outperforming code-generation approaches, which reach up to 50% success. We further demonstrate broader applicability through five case studies extending beyond device-level control to system orchestration, monitoring, and closed-loop optimization. These include DWDM link provisioning and coordinated monitoring of coherent 400 GbE and analog radio-over-fiber (ARoF) channels; autonomous characterization and bias optimization of a wideband ARoF link carrying 5G fronthaul traffic; multi-span channel provisioning with launch power optimization; closed-loop fiber polarization stabilization; and distributed acoustic sensing (DAS)-based fiber monitoring with LLM-assisted event detection. These results establish AgentOptics as a scalable, robust paradigm for autonomous control and orchestration of heterogeneous optical systems.

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

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zehao Wang, Mingzhe Han, Wei Cheng, Yue-Kai Huang, Philip Ji, Denton Wu, Mahdi Safari, Flemming Holtorf, Kenaish AlQubaisi, Norbert M. Linke, Danyang Zhuo, Yiran Chen, Ting Wang, Dirk Englund, Tingjun Chen
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
