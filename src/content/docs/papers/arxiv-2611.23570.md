---
title: "Safe to Omit, Worth Omitting? Keeping the Answer and Cutting Latency When an LLM Agent Skips Another's Message"
description: "In multi-agent systems, a receiver agent often waits for a helper agent's message (text or its latent KV cache), which can improve performance but adds latency."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.23570) · [PDF](https://arxiv.org/pdf/2611.23570)

## 一句话摘要

In multi-agent systems, a receiver agent often waits for a helper agent's message (text or its latent KV cache), which can improve performance but adds latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

In multi-agent systems, a receiver agent often waits for a helper agent's message (text or its latent KV cache), which can improve performance but adds latency. We study when a receiver agent can skip the message safely (the final answer rarely changes) and beneficially (the time saved exceeds the cost of deciding). Our mechanism reads the receiver agent's confidence without the message and uses a finite-sample test to certify a threshold at which, with high probability, at most 5% of skipped answers change; if none passes, the system keeps communicating. We test it on OpenBookQA, ARC-Challenge, and MMLU-Pro with three Qwen model pairs, on cross-family agents, and on SQuAD and GSM8K. Four insights emerge. First, oracle headroom is weak evidence that messages help: control inputs without answer-specific content, matched to change answers as often as real messages, reproduce a median 76% of the oracle's gain. Second, whether a message can be skipped depends on how often and how predictably it alters the answer, not on its accuracy; every certified KV-cache path is less accurate than the receiver agent alone. Third, where text messages help, skipping keeps most of their gain: on unseen questions in the four such settings, the policies skip 59 to 80% and keep an estimated 76 to 95% of the gain. In two prospective tests with all rules fixed in advance, our mechanism skips a three-agent system's verifier on 39.9% of sealed questions, keeping 12.55 of its 12.80-point gain, and a 32B helper on 68.4% of held-out questions, keeping its whole gain. Fourth, safety does not determine efficiency: at batch size one, skipping text saves hundreds of milliseconds per query and skipping KV cache far less. Certification extends to SQuAD but not to GSM8K. In eleven tests on unseen questions, every certified policy we could test kept its change rate's 95% upper bound below 5% under our answer parsers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xinyang Li, Chih-Hsuan Yang, Xiaolong Ma, Anjir Ahmed Chowdhury, Vikram Vasudevan, Rajeev Thakur, Feng Yan
- 发布：2026-11-17；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Piedpiperrr/safe-to-omit](https://github.com/Piedpiperrr/safe-to-omit)
- 阅读深度：metadata
