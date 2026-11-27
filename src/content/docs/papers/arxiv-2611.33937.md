---
title: "InstructTTS-OPD: On-Policy Distillation for Multi-Objective Instruction-Following TTS"
description: "Instruction-following text-to-speech (Instruct-TTS) renders a target transcript in the manner described by a free-form natural-language instruction, and a good rendition must succeed on three fronts at once: following the instruction, pronouncing the transcript correctly, and sounding natural."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.33937) · [PDF](https://arxiv.org/pdf/2611.33937)

## 一句话摘要

Instruction-following text-to-speech (Instruct-TTS) renders a target transcript in the manner described by a free-form natural-language instruction, and a good rendition must succeed on three fronts at once: following the instruction, pronouncing the transcript correctly, and sounding natural.

## 为什么值得关注

待编辑增强。

## 摘要原文

Instruction-following text-to-speech (Instruct-TTS) renders a target transcript in the manner described by a free-form natural-language instruction, and a good rendition must succeed on three fronts at once: following the instruction, pronouncing the transcript correctly, and sounding natural. Reinforcement learning has become the standard way to post-train such generative models toward human preferences, and TTS systems increasingly adopt it. When the three objectives are optimized together under a single scalar reward, typically with group relative policy optimization (GRPO), training tends to be unstable: the objectives compete, and the shared update drifts toward whichever one is easiest to improve, producing a seesaw among them. We instead adapt on-policy distillation (OPD), which fuses several single-objective teachers by matching their velocity fields on the student's own rollouts. Realizing this for Instruct-TTS first calls for a sound reward on each axis, which we analyze carefully: a distilled Qwen-Omni proxy for the costly Gemini judge, dialect-free data for the WER reward, and DNSMOS in place of the language-biased UTMOS. We then train three single-objective teachers with GRPO and fuse them with OPD, routing each rollout to the instruction-following or WER teacher by its data domain and letting every rollout additionally follow the MOS teacher for quality. This lets instruction following and intelligibility improve together without a trade-off, but the quality target conflicts with instruction following, so following it additively reintroduces the seesaw. We therefore propose conflict-aware velocity fusion, which projects the quality target off the direction that opposes the primary objective before fusing, and show that it markedly reduces the instruction-following/quality trade-off. The fused model improves over scalar-reward GRPO on all three objectives at once.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haitao Li, Tian Tan, Yuguang Yang, Guanrou Yang, Wenhao Guan, Chenglin Li, Shan Yang, Xie Chen
- 发布：2026-11-26；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
