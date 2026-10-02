---
title: "On-Device Commercial Intent Retrieval Under Size, Latency, and Privacy Constraints: A 3 MiB Retrieval System with Typed Egress Boundaries"
description: "We study commercial intent inference that runs entirely on the user's device, under three constraints frozen before the work began: the downloaded payload under 3 MiB, Tier-0 inference under 20 ms at p95, and no raw text, content embedding, or stable identifier leaving the device."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.00170) · [PDF](https://arxiv.org/pdf/2610.00170)

## 一句话摘要

We study commercial intent inference that runs entirely on the user's device, under three constraints frozen before the work began: the downloaded payload under 3 MiB, Tier-0 inference under 20 ms at p95, and no raw text, content embedding, or stable identifier leaving the device.

## 为什么值得关注

待编辑增强。

## 摘要原文

We study commercial intent inference that runs entirely on the user's device, under three constraints frozen before the work began: the downloaded payload under 3 MiB, Tier-0 inference under 20 ms at p95, and no raw text, content embedding, or stable identifier leaving the device. Under them we build a retrieval path over a 6,020-leaf commercial taxonomy: a static embedding table distilled from a Korean sentence transformer, quantized to 4 bits, no inference runtime. Our main result is where that constraint costs accuracy. On real Korean commerce text labelled by others (22,900 AI-Hub shopping reviews), mid-category top-5 on real product names is 75.0% against an 18.4% permutation baseline, but splits on one observable: a query containing some leaf name as a substring scores 83.5%, one containing none 45.2%. A generic 196.6x larger teacher seemed to localize the gap (+20.1 pp without an anchor, +0.1 with). That null was two effects cancelling: the same teacher fine-tuned on the student's own contrastive pairs reaches 0.8586 and beats the pure-encoder student by +10.6 pp with an anchor and +20.9 pp without. The cost is not uniform, but it is not free anywhere; where the anchor is absent, task adaptation buys the teacher nothing, so what the constrained encoder lacks there is capacity. The expensive regime is detectable on-device from the ranker's own score margin: declining the least confident fifth lifts the rest to 0.8296. A second axis we first reported, a manufacturer model code, does not survive source-category fixed effects (-4.0 pp, p=0.51); the anchor does (+13.0 pp). Payload is 2,942,652 bytes, all three library links measured. Tier-0 p95 is 4.431 and 3.670 ms on two iPhones (A14, A16) and 5.080 ms on a budget Android tablet (Snapdragon 695), all slower than three server CPUs on the same code. Taxonomy supervision is mostly synthetic Korean utterances.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hyojung Han
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
