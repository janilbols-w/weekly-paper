---
title: "Mitigating Agentic Deception via Evaluation-Side Partially Observable Games"
description: "As large language models become more capable agents, they can exhibit deceptive behaviors, cheating human for higher rewards while appearing helpful."
---

**评分：45/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2611.12835) · [PDF](https://arxiv.org/pdf/2611.12835)

## 一句话摘要

As large language models become more capable agents, they can exhibit deceptive behaviors, cheating human for higher rewards while appearing helpful.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language models become more capable agents, they can exhibit deceptive behaviors, cheating human for higher rewards while appearing helpful. We attribute this failure to evaluation-side partial observability, where models are evaluated mainly from final outcome, without checking the faithfulness of underlying reasoning, tool use, and environmental effects. Prior mitigations address this partial observability by predefined evaluator latent belief space or one-shot monitoring, which do not extend to free-form language space and vulnerable to stronger deceptions that evade simple monitoring. In this work, we formulate deception mitigation as an Evaluation-Side Partially Observable Extensive Form Game (e-PoG), a max-min framework in which an agent maximizes reward, a monitor minimizes the agent's payoff by exposing deception from the full interaction trajectory, and a fixed verifier validates the monitor's claims and converts them into penalties. We define the solution concept as a Subgame-Perfect Oversight Equilibrium (SPOE) between agent and monitor, and prove its existence in finite games. With a perfect verifier, every SPOE is faithful; with an imperfect verifier, the guarantee persists if verifier errors do not reverse the ranking of monitor actions. To achieve faithful SPOE, we derive a two-timescale policy gradient algorithm and enhance the pipeline empirically with NLI verification and deterministic checks. Experiments with Gemma3-4B-IT and Qwen3-4B/8B on Agentic Role-Playing, SearchQA, and WebShop show that e-PoG mitigates multiple emergent deception modes, outperforming the strongest baselines by 26.0% in deception mitigation and by up to 39.8% in task success. These gains persist under weak-to-strong supervision. Code is available at https://github.com/Toyoid/deceptive-agent.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Hanxiao Li, Shutong Liu, Yongjia Ma, Jiaming Ji, Juntao Dai, Shuning Zhang, Kejian Shi, Kai Chen, Pu Feng, Yuqing Ma, Qi Dou, Yaodong Yang, Xianglong Liu, Simin Li
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Toyoid/deceptive-agent](https://github.com/Toyoid/deceptive-agent)
- 阅读深度：metadata
