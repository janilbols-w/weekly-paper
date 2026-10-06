---
title: "From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model Agents"
description: "Activation probes can predict safety-relevant properties of language models with high area under the receiver-operating-characteristic curve (AUROC), but deployed agent monitors make thresholded alarm decisions under tight false-alarm budgets."
---

**评分：38/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2610.04575) · [PDF](https://arxiv.org/pdf/2610.04575)

## 一句话摘要

Activation probes can predict safety-relevant properties of language models with high area under the receiver-operating-characteristic curve (AUROC), but deployed agent monitors make thresholded alarm decisions under tight false-alarm budgets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Activation probes can predict safety-relevant properties of language models with high area under the receiver-operating-characteristic curve (AUROC), but deployed agent monitors make thresholded alarm decisions under tight false-alarm budgets. These are different estimands. We introduce an Operational Validity Contract that fixes a monitor's target, observability, identity, timing, intervention unit, comparator, calibration, and cost. We formalize risk at the semantic request or trajectory level: when one task contains repeated alarm opportunities, row-level AUROC and false positive rate do not identify semantic-unit any-alarm risk. A confidence-certified threshold also requires enough independent negative units, a tie-safe rule, and transport to deployment. Across Models Under Pressure, LASR refusal prediction, immutable AgentDojo, and a prospectively protocol-frozen ST-WebAgentBench replication, joint activation-observable monitors reach AUROC 0.957 and 0.935 on the first two benchmarks, yet their locked 5%/10% detection rates are only .642/.742 and .719/.782, respectively. On AgentDojo, the secondary mean-activation rollout monitor reaches AUROC 0.922 but detects none of 38 positive semantic cases at the locked 5% operating point; thresholds intended for 10% false alarms realize 18.7-20.0% on test. Because the test misses its prospectively frozen 40-positive support gate, we label it support-insufficient. On ST-WebAgentBench, activation reaches AUROC .874, but 23 independent calibration negatives cannot identify even a 10% controller; the locked policy abstains rather than reporting its mechanical zero FPR as a success. An exploratory counterexample also lowers full AUROC while improving realized 10% utility. The fail-closed compiler caps MUP and LASR at restricted predictive value and AgentDojo and ST-Web at representation accessibility; no setting reaches alarm-policy validity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xueping Gao
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
