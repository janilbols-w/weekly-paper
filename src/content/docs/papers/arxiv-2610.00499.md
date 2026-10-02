---
title: "Denoising Surface: Modeling and Predicting Inference Cost for Diffusion LLM Serving"
description: "As diffusion large language models (dLLMs) become more capable, they are moving from research settings to real-world \\textit{serving}, where request management (such as scheduling and resource allocation) relies on accurate estimation of per-request inference cost."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.00499) · [PDF](https://arxiv.org/pdf/2610.00499)

## 一句话摘要

As diffusion large language models (dLLMs) become more capable, they are moving from research settings to real-world \textit{serving}, where request management (such as scheduling and resource allocation) relies on accurate estimation of per-request inference cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

As diffusion large language models (dLLMs) become more capable, they are moving from research settings to real-world \textit{serving}, where request management (such as scheduling and resource allocation) relies on accurate estimation of per-request inference cost. However, common cost proxies fall short for dLLMs: output length ignores that one forward pass can unmask multiple tokens, and denoising-step count ignores the \textit{heterogeneous} per-step costs. We observe that the block-autoregressive generation mechanism induces a two-dimensional execution structure over output blocks and within-block denoising steps, whereas these proxies collapse it into a scalar, discarding information essential for characterizing the cost. Motivated by this insight, we propose the Denoising Workload Surface (DWS), which preserves this two-dimensional block-step structure as a probability surface to weight the heterogeneous per-step costs. We then design a coarse-to-fine training scheme that enables a lightweight prompt-only predictor to accurately predict the complex DWS. This predictor runs efficiently even on a single CPU core, avoiding GPU contention with the serving model. Since DWS decouples request-dependent execution behavior from deployment-specific cost factors, the predictor transfers across hardware configurations without retraining. In \textit{real-world} serving experiments, DWS reduces cost-prediction error by up to $2.50\times$ over scalar-based predictors, while the DWS-guided shortest-job-first scheduler reduces end-to-end latency by up to $1.92\times$ for online chatbots.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haoyu Zheng, Fangcheng Fu, Binhang Yuan, Yongqiang Zhang, Liang Deng, Hao Wang, Yuanyuan Zhu, Xiao Yan, Jiawei Jiang
- 发布：2026-09-30；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
