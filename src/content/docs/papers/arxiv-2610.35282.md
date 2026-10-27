---
title: "Satellite Intelligence: Distributed Training, Collaborative Inference,and LLM Adaptation in LEO Constellation"
description: "The proliferation of orbital sensing data and the real-time demands of emerging global services are pushing low Earth orbit (LEO) satellite networks from bent-pipe relays toward intelligent onboard processing."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.35282) · [PDF](https://arxiv.org/pdf/2610.35282)

## 一句话摘要

The proliferation of orbital sensing data and the real-time demands of emerging global services are pushing low Earth orbit (LEO) satellite networks from bent-pipe relays toward intelligent onboard processing.

## 为什么值得关注

待编辑增强。

## 摘要原文

The proliferation of orbital sensing data and the real-time demands of emerging global services are pushing low Earth orbit (LEO) satellite networks from bent-pipe relays toward intelligent onboard processing. This shift confronts a fundamental tension, where modern artificial intelligence (AI) training paradigms require intensive computation, abundant memory, and stable connectivity, all of which are scarce under the dynamic topologies, intermittent links, and severe size, weight, and power (SWaP) constraints of satellite networks. Addressing this tension demands rethinking AI workflows, from training and inference to the emerging deployment of large language models (LLMs), under a constraint-aware design philosophy. To the best of our knowledge, this paper provides the first survey that jointly covers all three, whereas prior surveys examine these aspects in isolation. We begin by identifying the deployment challenge of satellite intelligence (SI) and deriving design principles for SI. We then examine three advancing paradigms: i) distributed training, where federated learning (FL) and split learning (SL) enable satellite-ground co-training under resource limitations; ii) collaborative inference, which exploits single-satellite, multi-satellite, and satellite-ground architectures to meet real-time service demands; and iii) on-orbit LLM adaptation and serving, which tackles the frontier challenge of deploying LLMs under severe orbital constraints and resource-aware serving. Finally, we identify open challenges and future directions. By bridging the AI and satellite networks, this paper provides a research roadmap for the implementation of space-native AI technologies.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zheng Lin, Zhanwei Wang, Yuxin Zhang, Yafei Wang, Ons Aouedi, Zihan Fang, Jinfeng Xu, Jing Yang, Vu Nguyen Ha, Yuanwei Liu, Mohamed-Slim Alouini, Symeon Chatzinotas
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
