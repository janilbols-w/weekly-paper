---
title: "Delta Tokenizer: Reference-Identical Tokenization of Session Deltas and Segment-Parallelism for Long Prompts on Multicore CPUs"
description: "An agent that drives an LLM sends the model the same conversation again and again, and each turn adds only a little text at the end."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.19801v1) · [PDF](https://arxiv.org/pdf/2610.19801v1)

## 一句话摘要

An agent that drives an LLM sends the model the same conversation again and again, and each turn adds only a little text at the end.

## 为什么值得关注

待编辑增强。

## 摘要原文

An agent that drives an LLM sends the model the same conversation again and again, and each turn adds only a little text at the end. Inference engines reuse the KV cache of the shared prefix, so only the new tokens pass through the model. However, tokenization has no such shortcut. The CPU front end of the serving engine converts every request back into token IDs from its first character, which lengthens the time to first token (TTFT) and consumes CPU on every turn. We present Delta Tokenizer, a CPU tokenization front end that tokenizes only the delta between a request and the previous request of the same session. It retains the earlier token sequence, encodes again only the appended text and the short tail whose tokens the append could affect, and joins the two only at a position the tokenizer's splitting rules themselves cannot move, which keeps the result exact. For long requests with no state to reuse, it cuts the text where practical tokenizers already keep neighboring pieces independent, encodes the pieces on several cores at once, and concatenates the outputs into the reference encoding, exactly. A shared CPU pool schedules these chunks together with the short incremental updates, so an update runs between two chunks rather than behind an entire long job. The incremental path shortens the tokenization of a session turn by roughly 40x relative to the Hugging Face reference tokenizer, and on 16 cores the chunk-parallel path encodes a four-million-character request 8.2x faster than a serial encode and 1.6-2.1x faster than LoPT. Inside SGLang, Delta Tokenizer reduces the median TTFT through the chat interface by 59% at 100K tokens and brings the P99 TTFT of agent sessions down 9.5x under load and 23x when long requests tie up the front end. Every output we checked matches the reference, among them 41.8 billion documents encoded by its fast encoder.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 8 |
| reproducibility | 9 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Zhenyu Zhang, Zhichao Cao
- 发布：2026-10-14；更新：2026-10-14
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/asu-idi/toktier](https://github.com/asu-idi/toktier)
- 阅读深度：metadata
