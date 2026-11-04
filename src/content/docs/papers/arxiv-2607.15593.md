---
title: "Scaling LLM Agent Tool Access: The MCP Gateway"
description: "LLM agents increasingly rely on tool calling to complete tasks."
---

**评分：38/100** · AI 基础设施 > 集群与资源系统 > 存储与数据平面

[论文原文](https://arxiv.org/abs/2607.15593) · [PDF](https://arxiv.org/pdf/2607.15593)

## 一句话摘要

LLM agents increasingly rely on tool calling to complete tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents increasingly rely on tool calling to complete tasks. Model Context Protocol (MCP) standardizes tool calling between LLM agents and tool providers. It reduces integration cost and drives rapid growth in tool scale. In production deployments, tool access becomes difficult to scale. On the tool provider side, legacy services are not directly callable through MCP; the rapid protocol development creates ongoing compatibility cost. On the agent side, the number of mounted tools is limited by the LLM context window and inference overhead; mounting a large tool set increases token usage and inference latency and can reduce task success rate. Moreover, for stateful MCP backends with multiple replicas, preserving session affinity increases client-side complexity. We present a cloud-scale MCP Gateway system. It breaks the direct-connect model on the data plane and offloads legacy service integration, consolidating incompatible MCP variants, access control, tool recommendation, and session-aware routing at the gateway. The conversion module supports 315 OpenAPI services in the cloud and integrates MCP transport variants. Session-aware routing decouples the scalability of the gateway layer and the MCP service layer. The hybrid retrieval engine sustains $\sim$98\% Top-15 recall; it scales agent tool access to 3{,}000+ tools with improved tool selection accuracy. We also share the lessons learned from deploying the gateway system in production.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: data plane
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mingxin Li, Enge Song, Yueshang Zuo, Xiaodong Liu, Rong Wen, Qiang Fu, Gianni Antichi, Jian He, Jing Tie, Zhou Shao, Xiaobo Xue, Xiong Xiao, Luyao Zhong, Shaokai Zhang, Jiangu Zhao, Jianyuan Lu, Shize Zhang, Xiaoqing Sun, Changgang Zheng, Zihao Fan, Haonan Li, Tian Pan, Xiaomin Wu, Yang Song, Xing Li, Biao Lyu, Meng Li, Haipeng Dai, Guihai Chen, Shunmin Zhu
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
