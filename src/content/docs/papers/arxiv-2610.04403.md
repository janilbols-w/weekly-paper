---
title: "Saying, Not Knowing: Aggressively GGUF-Quantized Small Language Models Still Write Rare Words They Can No Longer Define"
description: "Post-training quantization to the GGUF format's mixed-precision K-quants is commonly how open-weight language models reach consumer hardware, yet its effect on fine-grained lexical competence is uncharacterized."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.04403) · [PDF](https://arxiv.org/pdf/2610.04403)

## 一句话摘要

Post-training quantization to the GGUF format's mixed-precision K-quants is commonly how open-weight language models reach consumer hardware, yet its effect on fine-grained lexical competence is uncharacterized.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization to the GGUF format's mixed-precision K-quants is commonly how open-weight language models reach consumer hardware, yet its effect on fine-grained lexical competence is uncharacterized. We audit 27 quantized artifacts across 13 families and four architecture backbones, 0.35B-14B parameters, evaluated down their published ladder to Q2_K (about 2.6 bits per weight), on 429 frequency-validated rare English words under two probes: surface inclusion of a prompt-supplied word and its one-sentence definition, scored by a tiered multi-synonym matcher, its error measured by a blind LLM-judge census of every definition, with human verification. Three regimes emerge at Q2: total collapse into unusable builds, severe semantic dissociation in sub-2B models, and mostly robust preservation above about 3B. In every sub-2B artifact, definitions fall 20-67% below the artifact's baseline, typically several times the inclusion loss. Two controls separate rarity from task difficulty: within the rare set, loss rises with rarity in six of seven sub-2B artifacts, and on a 100-word common-word set rare words lose more than common words in all eight, significantly in six. Tokenizer vocabulary size does not predict the damage (Spearman rho=0.12); parameter count dominates (rho=0.72), confirmed within five of six same-tokenizer families. Q4_K_M remains lexically clean at >=1B. The damage is frequency-graded, provider-dependent, and not calibrated by WikiText-2 perplexity: across nine artifact-matched ladders, near-identical Q2 penalties (44.7%/47.6%) separate an artifact keeping its definitions (3.6%) from one losing them (43.6%). Aggressively quantized small models can keep generating fluent text while no longer knowing what it means, risking hardware-constrained deployments in domains where semantics carries consequences. Validation must be per artifact.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Saurabh Kumar Singh, Yogeshwar Singh Dadwhal, Malhar Vedak
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
