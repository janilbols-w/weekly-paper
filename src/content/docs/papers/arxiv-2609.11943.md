---
title: "PinDCO: Whole-Page Aware Dynamic Creative Optimization at Scale"
description: "Recent advances in generative AI have substantially accelerated the creation of high-quality ad creatives, dramatically expanding the number of candidate variants per campaign."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度

[论文原文](https://arxiv.org/abs/2609.11943) · [PDF](https://arxiv.org/pdf/2609.11943)

## 一句话摘要

Recent advances in generative AI have substantially accelerated the creation of high-quality ad creatives, dramatically expanding the number of candidate variants per campaign.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in generative AI have substantially accelerated the creation of high-quality ad creatives, dramatically expanding the number of candidate variants per campaign. This shift increases the need for scalable dynamic creative optimization (DCO) systems that can match creatives to the most relevant audiences under stringent latency and cost constraints. We present PinDCO, a production DCO system for ad creative retrieval and selection on Pinterest, a billion-scale visual discovery platform. PinDCO is built around a Creative Component Fusion Network (CCFN) that performs dynamic creative scoring by modeling each creative component (e.g., image, title, layout) with a dedicated tower, using component-specific hyperparameters to account for differing modeling complexity. The component representations are fused to predict a creative-level score conditioned on the ad-level prediction, and we improve training data quality via an exploration-exploitation strategy. To account for Pinterest's waterfall grid layout, where a creative's rendered size affects nearby content and session-level engagement, we introduce a Pixel-aware Adjustment Module(PAM) that adjusts scores based on creative size to encourage efficient screen real-estate utilization and better whole-page outcomes. To support the large volume of creative candidates, we further employ a lightweight pre-selection model for early pruning, and optimize serving efficiency through caching and dynamic batching. Extensive offline analyses and online A/B experiments demonstrate the effectiveness of PinDCO, yielding a +3.09% lift in ad Click-Through Rate(CTR) with positive whole-page metrics. With the strong performance, we launched PinDCO in the Pinterest Ads platform.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: dynamic batching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yu Hao, Yuchun Li, Peimeng Sui, Meilin Liu, Tianyuan Cui, Hao Li, Zicong Zhou, Akanksha Baid
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
