---
title: "OmniHarness: Harnessing Generalizable Visual Generation via Symbolic Policy Learning"
description: "Unified multimodal large language models (MLLMs) and multi-agent systems have advanced visual generation."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2609.16057) · [PDF](https://arxiv.org/pdf/2609.16057)

## 一句话摘要

Unified multimodal large language models (MLLMs) and multi-agent systems have advanced visual generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Unified multimodal large language models (MLLMs) and multi-agent systems have advanced visual generation. However, three limitations remain. (1) Existing methods often distill task-specific experience with limited generalizability. (2) Reflection is often deferred until task completion. (3) Knowledge is often acquired only in response to downstream task demands. To address these limitations, we introduce OmniHarness, a framework for generalizable visual generation via symbolic policy learning. OmniHarness abstracts verified executions into symbolic policies for visual generation task families, capturing shared procedures and applicability conditions while removing instance-specific inputs. The harness instantiates, adapts, and composes these policies for new tasks. Intermediate verification guides refinement and failure recovery during execution. Through self-directed inquiry, OmniHarness autonomously generates and executes practice tasks near its capability limits before downstream objectives are specified. Execution feedback continually refines the policies while model parameters remain fixed. Experiments across six benchmarks, three MLLM backbones, and three visual agent frameworks demonstrate strong performance and continual capability expansion. On ComfyBench's Creative tasks, OmniHarness achieves a 95.0% resolve rate, exceeding the strongest baseline by 27.5 percentage points. Frozen policy snapshots improve existing visual agent systems through plug-and-play reuse.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: failure recovery
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xu Xu (Beihang University), Jinxiu Liu (The Chinese University of Hong Kong), Zhangbo Qiao (Beihang University), Jiaxing Lu (Beihang University), Xiangyu Zhang (Beihang University), Yubin Gu (National University of Singapore), Fangwei Ning (Beihang University), Yan Shi (Beihang University)
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
