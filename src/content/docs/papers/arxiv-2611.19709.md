---
title: "Cache or Denoise Less? Residual Reuse in a Flow-Matching World Action Model"
description: "Flow-matching robot policies generate each action chunk through repeated network evaluations, one per denoising step."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](http://arxiv.org/abs/2611.19709v1) · [PDF](https://arxiv.org/pdf/2611.19709v1)

## 一句话摘要

Flow-matching robot policies generate each action chunk through repeated network evaluations, one per denoising step.

## 为什么值得关注

待编辑增强。

## 摘要原文

Flow-matching robot policies generate each action chunk through repeated network evaluations, one per denoising step. Cross-cycle caches such as C$^3$ache reuse computation from earlier replanning calls, but whether they beat simply taking fewer steps is unclear. We compare the two in Fast-WAM, a 6B-parameter world action model, on LIBERO-Goal. Two uncached steps keep the success of ten: on all 500 initial states they are non-inferior within two percentage points, for one checkpoint and noise seed. Under PyTorch's default compile mode, they also cut a replanning call on an RTX A6000 from 202 to 92 ms. This leaves little room for caching. A cache that keeps two fresh steps cannot be faster than two uncached steps: every call still encodes the images, runs the video expert and computes those two steps. Caching the first of two steps, refreshed every fourth call, saves at most 11--14% of a call by our cost model. Cached policies are also fragile. Their losses tracked the share of the flow path the cached steps cover: under Fast-WAM's current time shift, C$^3$ache's eight cached steps cover 80% of the path instead of 44%, and the cached policy succeeds on 63% of states against 95% uncached. Resampling the noise on every call cost caches covering 60% or more of the path 14--40 points. These results argue for fewer-step baselines and for testing reuse under the deployed sampler and noise settings. We release our evaluation harness, logs and a checklist.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Abhinav Gupta, Nissan Pow
- 发布：2026-11-15；更新：2026-11-15
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/gabhinav001/cache-or-denoise-less](https://github.com/gabhinav001/cache-or-denoise-less)
- 阅读深度：metadata
