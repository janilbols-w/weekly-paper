---
title: "How Does Post-Training Shape LLM Value Preferences?"
description: "During post-training, large language models (LLMs) learn value preferences from corpora that may contain imbalanced proportions of opinions associated with different demographic groups."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.33371) · [PDF](https://arxiv.org/pdf/2610.33371)

## 一句话摘要

During post-training, large language models (LLMs) learn value preferences from corpora that may contain imbalanced proportions of opinions associated with different demographic groups.

## 为什么值得关注

待编辑增强。

## 摘要原文

During post-training, large language models (LLMs) learn value preferences from corpora that may contain imbalanced proportions of opinions associated with different demographic groups. Amplifying these imbalances may further underrepresent some groups' opinions. However, how opinion mixtures shape value preferences across post-training paths remains unclear. To answer this question, we conduct controlled experiments using post-training corpora with different opinion mixtures and five post-training paths based on SFT, DPO, and GRPO. We find that post-training amplifies opinion imbalances differently across post-training paths. Once value preferences are amplified, whether further post-training can remove them depends on both the post-training method and the opinion mixture in the corpus. More concerningly, a model's stability under interventions depends on whether further post-training changes its value preference. Moreover, these value preferences are transferred to student models even when distillation uses corpora with no explicit opinion questions. These findings suggest that both the opinion mixture in post-training corpora and the choice of post-training method should be considered when developing, evaluating, and reusing LLMs. Our code and data are available at https://github.com/ku-nlp/llm-value-preferences.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yang Liu, Shaoyang Xu, Masahiro Kaneko, Chengzhi Zhong, Wenxuan Zhang, Chenhui Chu
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ku-nlp/llm-value-preferences](https://github.com/ku-nlp/llm-value-preferences)
- 阅读深度：metadata
