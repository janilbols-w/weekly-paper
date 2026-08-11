---
title: "Length-MAX Tokenizer for Language Models"
description: "We introduce a new tokenizer for language models that minimizes the average tokens per character, thereby reducing the number of tokens needed to represent text during training and to generate text during inference."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2511.20849) · [PDF](https://arxiv.org/pdf/2511.20849)

## 一句话摘要

We introduce a new tokenizer for language models that minimizes the average tokens per character, thereby reducing the number of tokens needed to represent text during training and to generate text during inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce a new tokenizer for language models that minimizes the average tokens per character, thereby reducing the number of tokens needed to represent text during training and to generate text during inference. Our method, which we refer to as the Length-MAX tokenizer, obtains its vocabulary by casting a length-weighted objective maximization as a graph partitioning problem and developing a greedy approximation algorithm. On FineWeb and diverse domains, it yields 14--18\% fewer tokens than Byte Pair Encoding (BPE) across vocabulary sizes from 10K to 50K, and the reduction is 13.0\% when the size is 64K. Training GPT-2 models at 124M, 355M, and 1.3B parameters from scratch with five runs each shows 18.5\%, 17.2\%, and 18.5\% fewer steps, respectively, to reach a fixed validation loss, and 13.7\%, 12.7\%, and 13.7\% lower inference latency, together with a 16\% throughput gain at 124M, while consistently improving on downstream tasks including reducing LAMBADA perplexity by 11.7\% and enhancing HellaSwag accuracy by 4.3\%. Moreover, the Length-MAX tokenizer achieves 99.62\% vocabulary coverage and the out-of-vocabulary rate remains low at 0.12\% on test sets. These results demonstrate that optimizing for average token length, rather than frequency alone, offers an effective approach to more efficient language modeling without sacrificing -- and often improving -- downstream performance. The tokenizer is compatible with production systems and reduces embedding and KV-cache memory by 18\% at inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dong Dong, Weijie Su
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
