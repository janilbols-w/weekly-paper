---
title: "CAST: Cost-Aware Speculative Trees from One-Pass Block Drafters"
description: "Speculative decoding accelerates large language model inference by drafting future tokens cheaply and verifying them with the target model in parallel."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.00321) · [PDF](https://arxiv.org/pdf/2610.00321)

## 一句话摘要

Speculative decoding accelerates large language model inference by drafting future tokens cheaply and verifying them with the target model in parallel.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model inference by drafting future tokens cheaply and verifying them with the target model in parallel. Block drafters score a whole block of future tokens in one forward pass, yet standard decoding verifies only the top-scoring chain and discards the other candidates. Because these candidates are already scored, verifying more of them adds target computation but no extra drafting. We introduce CAST (Cost-Aware Speculative Trees), which packs these candidates into a tree and verifies it in a single target pass, leaving the target model, drafter weights, and decoding rule untouched. To decide how wide the tree should be, CAST adds candidates while the expected gain from the next one outweighs the verification time it adds. The width therefore adapts to each deployment from a latency measurement, without sweeping over widths. We evaluate CAST across five domains on three GPU generations and two model families. At its predicted width, CAST is faster than the standard chain in all eight settings, by up to 43%. We also find that the best width depends strongly on the deployment. Where verification cost jumps at a kernel boundary, a 128-token tree is only 2% faster than the standard chain, whereas the tree at the predicted width is 20% faster. Furthermore, we prove that CAST leaves the target output distribution unchanged under both greedy and sampled decoding. Code is available at https://github.com/js-lee-AI/CAST.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jungseob Lee, Sugyeong Eo
- 发布：2026-09-29；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/js-lee-AI/CAST](https://github.com/js-lee-AI/CAST)
- 阅读深度：metadata
