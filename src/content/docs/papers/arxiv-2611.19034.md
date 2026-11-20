---
title: "Refinement vs. Replanning: Inference Compute Allocation in Robot Policies"
description: "A frozen chunked robot policy can spend deployment-time inference compute in two coupled ways: more work within each policy call to refine a predicted action chunk, or more frequent policy calls to replan from fresh observations."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](http://arxiv.org/abs/2611.19034v1) · [PDF](https://arxiv.org/pdf/2611.19034v1)

## 一句话摘要

A frozen chunked robot policy can spend deployment-time inference compute in two coupled ways: more work within each policy call to refine a predicted action chunk, or more frequent policy calls to replan from fresh observations.

## 为什么值得关注

待编辑增强。

## 摘要原文

A frozen chunked robot policy can spend deployment-time inference compute in two coupled ways: more work within each policy call to refine a predicted action chunk, or more frequent policy calls to replan from fresh observations. We study this allocation without updating model weights. Our evaluation procedure reports success with both nominal compute rate and complete attempt cost, selects comparisons on discovery tasks, and tests prespecified comparisons on held-out tasks. Comparisons added after inspecting the held-out results only summarize observed patterns. We demonstrate the procedure with one frozen SmolVLA checkpoint in synchronous LIBERO simulation, using denoising count as the refinement control and fixing chunk length at K=50. Arithmetic and latency characterize cost differently: at d=10, 82.1% of counted arithmetic is independent of denoising, whereas a descriptive affine fit to fixed-input host time assigns 17.7% to its intercept. At h=2, d=2 succeeds on 139/160 attempts versus 122/160 for d=5 (+10.6 percentage points; task-conditional 95% interval: +4.4 to +16.9), while using 5.9% less arithmetic per control step. Executing h=5 rather than h=2 at d=2 yields 138/160 versus 139/160 successes and 60.7% lower arithmetic per attempt; equivalence is not established. The case study shows why deployment adaptation must evaluate generation effort and feedback frequency jointly; it does not define a universal setting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Alba Maria Tellez Fernandez
- 发布：2026-11-14；更新：2026-11-14
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
