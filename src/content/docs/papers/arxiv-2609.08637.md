---
title: "Navigating the digital spectrum: Assessing political bias, stability, and downstream fairness in Large Language Models"
description: "Large Language Models are increasingly deployed as information intermediaries, yet measuring their political behavior remains fragile because questionnaire results mix model dispositions with measurement artifacts and response-elicitation biases."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.08637) · [PDF](https://arxiv.org/pdf/2609.08637)

## 一句话摘要

Large Language Models are increasingly deployed as information intermediaries, yet measuring their political behavior remains fragile because questionnaire results mix model dispositions with measurement artifacts and response-elicitation biases.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models are increasingly deployed as information intermediaries, yet measuring their political behavior remains fragile because questionnaire results mix model dispositions with measurement artifacts and response-elicitation biases. We introduce a robust Political Compass Test evaluation framework that samples 300 configurations across an eight-dimensional perturbation space varying language, framing, instructions, answer format, option order, and persona wording. We evaluate eight Gemma 3 and Qwen 3 models across 14 languages and three quantization levels, obtaining design-averaged political coordinates with quantified uncertainty. Most models lean Libertarian-Left on average, but instruction phrasing, language, and answer format significantly affect recovered coordinates. Cross-lingual differences primarily reflect coordinate drift rather than distinct cultural reasoning. Reverse-engineering the test also exposes axis-weighting imbalances and the collapse of degenerate responses toward the center, so near-origin estimates for the smallest models can reflect weak signal rather than centrism. Free-text reasoning and chat-then-classify elicitation alter recovered coordinates, and larger models show clearer persona separation, with a specific failure of the Authoritarian-Left persona to move most models in the intended social direction. In downstream tasks, persona effects are modest relative to model size and target group for hate-speech detection, while base and centrist prompts give the highest agreement for topic-level sentiment. Political role prompting therefore has measurable but task- and dataset-specific downstream effects.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Luka Debevc, Nishan Chatterjee, Antoine Doucet, Senja Pollak, Matej Martinc
- 发布：2026-09-08；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
