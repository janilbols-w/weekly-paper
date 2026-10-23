---
title: "Low-Latency MoE Inference in Space Data Centers: A Wireless-Power-Transfer Perspective"
description: "Space data centers (SpaceDCs) are emerging as platforms for large language models (LLMs), supported by continuous solar-energy harvesting and high-speed interconnections."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2610.30923) · [PDF](https://arxiv.org/pdf/2610.30923)

## 一句话摘要

Space data centers (SpaceDCs) are emerging as platforms for large language models (LLMs), supported by continuous solar-energy harvesting and high-speed interconnections.

## 为什么值得关注

待编辑增强。

## 摘要原文

Space data centers (SpaceDCs) are emerging as platforms for large language models (LLMs), supported by continuous solar-energy harvesting and high-speed interconnections. The mixture-of-experts (MoE) architecture supports distributed LLM inference by deploying experts across satellites. However, skewed expert activation creates uneven computation power demands despite uniform solar-power supply at the dawn-dusk sun-synchronous orbit (SSO). Consequently, active experts remain power-constrained while harvested power at idle experts is underused. These reduce inference efficiency and increase latency. To address this supply-demand mismatch, we propose the SpaceWPT framework, which uses inter-satellite laser-based wireless power transfer (WPT) to redistribute harvested power. The key design challenge is to balance the computation demands of power-donating and power-receiving satellites under WPT losses: transferring more power accelerates computation at the receiver but leaves less power for the donor. After deriving design principles that simplify WPT control, we characterize the resulting latency tradeoff through a tractable surrogate of average inference latency. Minimizing the surrogate yields a novel two-sided water-filling strategy that determines whether each active expert donates, retains, or receives power according to the water level and its WPT link efficiency. Simulations with Mixtral-8x7B and Phi-3.5-MoE show up to 29.25% lower inference latency than without WPT, with larger gains under more compact formations and higher transfer efficiencies.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: moe inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haotian Zheng, Zhanwei Wang, Kaibin Huang
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
