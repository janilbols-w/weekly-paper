---
title: "Evaluating Inference Compute for Generative AI: A Framework for Enterprise Workloads"
description: "LLM deployment is shifting from single-turn completion to agentic trajectories in which a model plans, calls tools, reads results and reasons at test time before acting."
---

**评分：54/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2610.07094) · [PDF](https://arxiv.org/pdf/2610.07094)

## 一句话摘要

LLM deployment is shifting from single-turn completion to agentic trajectories in which a model plans, calls tools, reads results and reasons at test time before acting.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM deployment is shifting from single-turn completion to agentic trajectories in which a model plans, calls tools, reads results and reasons at test time before acting. This inverts the economics of inference hardware: chat serving amortises weight reads across large batches, whereas agent trajectories are sequentially dependent, run at effective batch one, and make per-token decode latency (TPOT) the dominant term in task completion time. Using a roofline analysis and a closed-form episode-latency model, we show why this regime favours accelerators that keep weights in on-die SRAM (Cerebras WSE-3/3T, Groq/NVIDIA LPU) or compiler-managed tiered memory (SambaNova SN40L/SN50), and why three vendor ecosystems converged in 2026 on disaggregated prefill/decode serving. We show that per-step reliability compounds exponentially in trajectory length-a 2% per-step failure rate erases a 2x decode advantage for a 20-step agent-so determinism and tail latency are first-order performance variables. We then propose a four-layer evaluation framework (silicon, serving system, agent episode, enterprise) with a metric set built on goodput at an agentic SLO and cost per successful episode, a six-axis benchmark protocol over six task families, a paired-bootstrap statistical design, an attestation protocol for vendor-run benchmarks, and TCO, availability and adoption-timing models with explicit break-even conditions. All performance figures are public and labelled by evidence class; we state seven falsifiable hypotheses and the experiments that test them, and argue that the most likely original result is that token-throughput rankings diverge from cost-per-successful-task rankings on long-horizon work.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo, tail latency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Abbas Raza Ali, Muhammad Ajmal Siddiqui, Moona Zahid
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
