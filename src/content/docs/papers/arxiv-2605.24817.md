---
title: "RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry"
description: "As Mixture-of-Experts (MoE) architectures are increasingly adopted for scaling Large Language Models (LLMs), safety auditing becomes necessary to verify whether these models produce or facilitate harmful behaviors during operation."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2605.24817) · [PDF](https://arxiv.org/pdf/2605.24817)

## 一句话摘要

As Mixture-of-Experts (MoE) architectures are increasingly adopted for scaling Large Language Models (LLMs), safety auditing becomes necessary to verify whether these models produce or facilitate harmful behaviors during operation.

## 为什么值得关注

待编辑增强。

## 摘要原文

As Mixture-of-Experts (MoE) architectures are increasingly adopted for scaling Large Language Models (LLMs), safety auditing becomes necessary to verify whether these models produce or facilitate harmful behaviors during operation. However, existing content-based auditing methods typically require access to user prompts, model internals, or outputs, potentially exposing sensitive user information and creating a tension between LLM safety and user privacy. On the other hand, we observe that, in MoE models, different inputs induce different sparse expert-routing patterns, which produce measurable footprints in low-level GPU execution telemetry. We refer to these hardware-observable signals induced by expert-routing decisions as expert routing telemetry; they are derived from GPU execution rather than from router logits or token-level routing assignments. Inspired by this observation, we propose RouteScan, a non-intrusive auditing framework for detecting harmful behaviors through such routing-induced GPU telemetry. Specifically, RouteScan utilizes the number of active GPU threads allocated to expert modules during the prefilling phase as a discriminative micro-architectural fingerprint, and builds a lightweight detection pipeline that isolates cross-domain invariant risk indicators for the precise identification of malicious prompts. Comprehensive evaluations on four open-source MoE LLMs with distinct routing designs demonstrate that RouteScan achieves strong generalization, with an AUROC exceeding 0.91 on unseen harmful domains. Moreover, privacy stress tests show that, although aggregated execution telemetry retains input-related attribute information, full prompts and exact sensitive fields cannot be reliably recovered under the evaluated attacks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bo Lv, Zhiheng Xu, KeDong Xiu, Ruyi Ding, Tianhang Zheng, Zhibo Wang, Kui Ren
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
