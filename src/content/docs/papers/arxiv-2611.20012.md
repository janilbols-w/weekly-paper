---
title: "Offline-First Quantized AI: Design and Evaluation of an On-Device Maternal-Health Assistant for Low-Connectivity Environments"
description: "Offline language models could extend access to maternal-health information where internet connectivity is unreliable, but deployment requires both clinically appropriate responses and feasible local execution."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.20012) · [PDF](https://arxiv.org/pdf/2611.20012)

## 一句话摘要

Offline language models could extend access to maternal-health information where internet connectivity is unreliable, but deployment requires both clinically appropriate responses and feasible local execution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Offline language models could extend access to maternal-health information where internet connectivity is unreliable, but deployment requires both clinically appropriate responses and feasible local execution. This study presents an offline Android assistant integrating ready-made quantized language models, a clinically validated local knowledge package, conversational context, and model-initiated local retrieval. Gemma 4 E2B and Qwen3.5 0.8B were compared across 45 conversations and 312 turns per configuration, including a dedicated offline agentic benchmark. Gemma achieved higher response-quality, context-retention, and safety scores; Qwen offered faster generation and lower memory use. Clinician assessment of 150 Gemma responses across nine clinical domains yielded a mean quality score of 3.80/4, with 147 responses meeting the acceptance criterion. A paired RAG-on/off experiment evaluated 74 questions: retrieval improved 11 responses, left 56 neutral, produced four adverse response changes, and left three pairs unassessable. RAG-on had descriptively higher mean usefulness, safety, correctness, and actionability in the conditional 70-pair subset excluding the four flagged pairs from both conditions. Physical-device testing demonstrated offline responses on a 6 GB Android handset, with a 14.3 s median latency, alongside successful reconnection synchronization in the integrated application. Together, the findings document clinical response quality and practical performance of the integrated offline maternal-health assistant.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Okenla AbdulQahhar Abimbola, Maurice Abraham John, Adepoju Jeremiah Moyondafoluwa, Omolaiye Samuel, Oko-Oba Sandra Chioma, Owoo Oluwamayowa Emmanuel, Thanni Adewuyi, Lily Aimas-Love, Benson Eniola, Abdulquddus Ajibade, Sylvia Essessien, Anyanwu Princess Emmanuella, Adereni Abiodun
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
