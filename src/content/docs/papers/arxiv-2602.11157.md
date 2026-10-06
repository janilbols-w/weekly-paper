---
title: "Response-Based Knowledge Distillation for Multilingual Jailbreak Prevention Unwittingly Compromises Safety"
description: "Large language models (LLMs) are increasingly deployed worldwide, yet their safety alignment remains predominantly English-centric."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.11157) · [PDF](https://arxiv.org/pdf/2602.11157)

## 一句话摘要

Large language models (LLMs) are increasingly deployed worldwide, yet their safety alignment remains predominantly English-centric.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are increasingly deployed worldwide, yet their safety alignment remains predominantly English-centric. This allows for vulnerabilities in non-English contexts, especially with low-resource languages. We introduce a novel application of knowledge distillation (KD) in the context of multilingual jailbreak prevention, examining its efficacy. We distill the refusal behaviors of a proprietary teacher model (OpenAI o1-mini) with Low-Rank Adaptation (LoRA) into three open-source student models: Meta-Llama-3-8B-Instruct, Gemma-2-2B-IT, and Qwen3-8B, using ~28,000 multilingual jailbreak prompts from XSafety via black-box response-based, parameter-efficient fine-tuning (PEFT). Evaluation on the MultiJail benchmark reveals a counterintuitive behavior: standard fine-tuning on the teacher's ``safe'' refusal data inadvertently increases Jailbreak Success Rate (JSR) for all student models, up to 16.6 percentage points. Our experiments reveal a divergent generalization to unseen languages during distillation, with varying outcomes depending on the base model. By removing a primary source of safety degradation, nuanced `boundary' refusals, we mitigate or even reverse safety declines in student models, although reductions in reasoning performance (GSM8K) persist. Overall, our exploratory study highlights the challenges and potential of KD as a technique for multilingual safety alignment, offering a foundation for future research in this direction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Max Zhang, Derek Liu, Kai Zhang, Joshua Franco, Haihao Liu
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
