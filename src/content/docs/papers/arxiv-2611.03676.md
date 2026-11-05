---
title: "A local orchestration harness for molecular design with foundation models"
description: "Molecular design requires coordinated generation, property prediction and iterative editing, with each decision linked to the correct chemical structure and supporting evidence."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2611.03676) · [PDF](https://arxiv.org/pdf/2611.03676)

## 一句话摘要

Molecular design requires coordinated generation, property prediction and iterative editing, with each decision linked to the correct chemical structure and supporting evidence.

## 为什么值得关注

待编辑增强。

## 摘要原文

Molecular design requires coordinated generation, property prediction and iterative editing, with each decision linked to the correct chemical structure and supporting evidence. Integrating these capabilities in practice presents three major challenges: retaining local control of molecular data, connecting specialized models across tasks and verifying that proposed changes satisfy chemical constraints. Here we present MolCrew, a locally deployable system that coordinates four separately trained molecular specialists with a language-model orchestrator and RDKit calculations. The specialists generate structures from descriptions, describe molecular structures, predict biological endpoints and propose edits towards specified goals. Separate model weights allow each capability to be evaluated and updated independently within the workflow. RDKit calculations check structural validity, quantify descriptor changes and assess specified structural constraints, while returned observations guide further tool calls. We evaluated low-rank adaptation of the orchestrator for tool-use decisions and failure recovery while leaving specialist weights unchanged. On 3,300 ChEBI-20 test examples, MolCrew achieved 96.4% exact structure recovery, compared with 38.7% for published Atomas-large results. Across eight MoleculeNet datasets evaluated using scaffold splits, mean area under the receiver operating characteristic curve was 0.851, compared with 0.770 for published Atomas results. In a recorded evaluation using the unadapted orchestrator, 1,554 of 1,699 requests (91.5%) passed every predefined workflow check. By preserving inspectable links between molecular proposals, model outputs and chemical calculations, MolCrew provides a modular framework for computational candidate assessment and refinement under local data control.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: failure recovery
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sakib Mostafa, Md Atik Ahamed, James Zou, Lei Xing, Md Tauhidul Islam
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
