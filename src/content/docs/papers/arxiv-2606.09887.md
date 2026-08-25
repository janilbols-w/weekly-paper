---
title: "SocraticPO: Policy Optimization via Interactive Guidance"
description: "Reinforcement learning (RL) for large language models usually supervises reasoning with scalar outcome rewards, such as binary correctness."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.09887) · [PDF](https://arxiv.org/pdf/2606.09887)

## 一句话摘要

Reinforcement learning (RL) for large language models usually supervises reasoning with scalar outcome rewards, such as binary correctness.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning (RL) for large language models usually supervises reasoning with scalar outcome rewards, such as binary correctness. Such rewards provide an optimization direction but rarely explain how a model should revise its mistaken reasoning, which can encourage shortcut learning and brittle policies. We propose \textbf{SocraticPO} (Socratic Policy Optimization), a policy-optimization framework that augments RL rollouts with Socratic-style natural-language guidance. During rollout, the student first answers independently; if the answer is incorrect, a teacher diagnoses the attempt and provides concise corrective guidance, after which the student continues under the expanded context. Crucially, this guidance is paired with reward decay: correct answers obtained after teacher intervention only receive decayed rewards, preventing the policy from treating teacher help as a free path to reward. Since SocraticPO only modifies the rollout process while leaving the standard expected-reward objective intact, it can be plugged into existing policy-gradient backends such as Reinforce++. Moreover, because the teacher provides only text-level guidance, SocraticPO can leverage stronger black-box teacher models without requiring access to logits or distribution matching. On undergraduate-level scientific reasoning benchmarks from SciKnowEval, SocraticPO improves over strong RL and self-distillation baselines. Ablations show that both targeted guidance and reward decay are necessary, with reward decay mitigating reliance on assisted correction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
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

- 作者：Zirui Liu, Tingyue Pan, Jie Ouyang, Qi Liu, Xianquan Wang, Jiayu Liu, Qingchuan Li, Jing Sha, Zhenya Huang, Shijin Wang, Enhong Chen
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
