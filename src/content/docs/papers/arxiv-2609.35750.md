---
title: "KV-streams for Efficient Compaction in Agentic Reinforcement Learning"
description: "Scaling the horizon of agentic LLMs is bottlenecked by the need to fit ever longer context traces in GPU memory."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.35750) · [PDF](https://arxiv.org/pdf/2609.35750)

## 一句话摘要

Scaling the horizon of agentic LLMs is bottlenecked by the need to fit ever longer context traces in GPU memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Scaling the horizon of agentic LLMs is bottlenecked by the need to fit ever longer context traces in GPU memory. Context compaction has been the most popular mechanism to alleviate this issue, keeping GPU memory constant for a given trace. Unfortunately, most compaction strategies rely on prefilling the LLM context many times over, hindering training throughput. To alleviate this bottleneck and enable efficient trainable compaction, we propose KV-streams, a plug-and-play strategy compatible with any compaction strategy that substantially increases throughput while showing no evidence of hindering performance. KV-streams enable scalable compaction by streaming the KV cache forward rather than flushing it after each compaction. We show that KV-streams enable three different compaction strategies, achieving a 2.6 to 5x wall-clock speedup in training. Beyond efficiency, we find that the streamed KV cache can act as a recurrent state, carrying forward information that has long since disappeared from the context. Specifically, in a controlled setting we show that, contrary to prior work, RL alone is all that is needed for this behavior to emerge. Overall, we show KV-streams to be an efficient and lightweight plug-and-play addition to any post-training pipeline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Emiliano Penaloza, Dane Malenfant, Dheeraj Vattikonda, Roger Creus Castanyer, Siddarth Venkatraman, Abhay Puri, Jonathan Light, Matthew James Sargent, Augustine N. Mavor-Parker, Massimo Caccia, Lucas Caccia, Glen Berseth, Esmeralda S. Whitammer, Alessandro Sordoni, Minseon Kim, Marc-Alexandre C\^ot\'e, Laurent Charlin, Guillaume Lajoie
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
