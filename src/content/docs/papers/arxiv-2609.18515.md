---
title: "Beyond Routine Compliance: Cunning Data Cultivates Safety Vigilance in Large Language Models"
description: "Safety alignment teaches large language models (LLMs) to recognize harmful requests and reject risky instructions."
---

**评分：39/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2609.18515) · [PDF](https://arxiv.org/pdf/2609.18515)

## 一句话摘要

Safety alignment teaches large language models (LLMs) to recognize harmful requests and reject risky instructions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Safety alignment teaches large language models (LLMs) to recognize harmful requests and reject risky instructions. Yet aligned models can fail when harmful intent is concealed within seemingly benign contexts. Robust safety therefore requires both knowledge of safety boundaries and \textbf{vigilance}: the ability to detect unusual premises, misleading reasoning, and latent risks beneath surface-level semantics. Vigilance requires models to scrutinize a request's underlying intent and assumptions before acting. To cultivate this capability, we introduce \textbf{cunning questions}, which are not necessarily safety-related but contain misleading premises, atypical reasoning, or subtle inconsistencies. We hypothesize that learning to look beyond such reasoning traps can transfer to safety-critical scenarios. Experiments show that Cunning training improves robustness to out-of-distribution jailbreak attacks and strengthens subsequent safety fine-tuning. Furthermore, augmenting an existing state-of-the-art safety alignment pipeline with Cunning establishes a new state of the art across our evaluated settings, reducing mean ASR across nine backbone--benchmark combinations from 17.40\% to 15.05\%. Trace analysis after matched safety fine-tuning suggests that safety judgments are more likely to govern responses before harmful planning begins. A conditional theoretical analysis further characterizes when invariance learned from cunning data can transfer to safety-related inputs. These findings suggest that cunning data can strengthen model vigilance and complement conventional safety alignment.

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

- taxonomy keywords: trace analysis
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Youjia Wang, Lin Xu, Yang Sun, Yuxiao Lu, Chengfang Fang, Jie Shi
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
