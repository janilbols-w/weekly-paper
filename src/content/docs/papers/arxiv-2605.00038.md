---
title: "Lottery BP: Unlocking Quantum Error Decoding at Scale"
description: "During a QEC cycle, quantum error decoding stands on the critical path."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2605.00038) · [PDF](https://arxiv.org/pdf/2605.00038)

## 一句话摘要

During a QEC cycle, quantum error decoding stands on the critical path.

## 为什么值得关注

待编辑增强。

## 摘要原文

During a QEC cycle, quantum error decoding stands on the critical path. To enable fault tolerance on millions of qubits in real time, scalable decoding is necessary, which motivates this paper. Existing decoding algorithms (decoders), such as clustering, matching, belief propagation (BP), and neural networks, suffer from one or more of inaccuracy, costliness, and incompatibility, upon a broad set of quantum error correction codes, such as surface code and bivariate bicycle code. Therefore, there exists a gap between existing decoders and an ideal decoder that is accurate, fast, general, and scalable simultaneously. To move closer to the goal above, this paper contributes in three aspects, including decoder algorithm, decoder architecture, and decoding simulator. First, we propose Lottery BP, a lightweight decoder that introduces guided randomness to break the symmetric deadlock caused by quantum degeneracy during decoding. Lottery BP improves the decoding accuracy over BP by up to 6 orders. Second, we design a PolyQec architecture that implements Lottery BP as a local decoder and ordered statistics decoding (OSD) as a global decoder, exemplifying a hierarchical decoder architecture. PolyQec is configurable for surface code and X/Z check. Since Lottery BP boosts the local decoding accuracy, PolyQec invokes the costly global OSD decoder less frequently over BP+OSD to enhance the scalability, e.g., up to 4 orders of magnitude less for surface codes. Third, we develop Syndrilla, a modular PyTorch-based decoding simulator that enables fair, extensible decoder evaluation with unified accuracy and performance metrics. On GPUs, Syndrilla runs 1 order of magnitude faster than CUDAQX.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fault tolerance
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yanzhang Zhu, Chen-Yu Peng, Yun Hao Chen, Yeong-Luh Ueng, Di Wu
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
