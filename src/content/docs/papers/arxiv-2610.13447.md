---
title: "O\\'ido: Real-Time Open-Vocabulary Speech Recognition on a $5 Microcontroller without a Neural Accelerator"
description: "Speech recognition on low-cost microcontrollers is, in practice, limited to keyword spotting or a fixed list of commands."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.13447) · [PDF](https://arxiv.org/pdf/2610.13447)

## 一句话摘要

Speech recognition on low-cost microcontrollers is, in practice, limited to keyword spotting or a fixed list of commands.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speech recognition on low-cost microcontrollers is, in practice, limited to keyword spotting or a fixed list of commands. We present O\'ido, an inference engine and a family of models that run open-vocabulary English speech recognition entirely on an ESP32-S3 (240 MHz Xtensa LX7, 8 MB of PSRAM, 16 MB of flash, no neural accelerator) faster than real time on one core. Version 1 of this work ran a 13 M-parameter Conformer-CTC at 1.97x the duration of the audio. We measured on the board that the bound was memory traffic and per-frame cost, not arithmetic: external memory reads at 89 MB/s (PSRAM) and 32 MB/s (flash), and a streaming recognizer re-reads every weight for every chunk. Version 2 combines a model built for that memory system (80 ms frame stacking, a 64-channel front end, 12 or 16 blocks, int4 weights that mostly fit in PSRAM, fine-tuned from the version 1 model) with engine changes that overlap the weight stream with compute (an asynchronous data-cache preload), keep work buffers in SRAM and make the decoder cheap. On a physical board the streaming real-time factor falls from 1.77 to 0.54 (variant B) and 0.72 (variant A), the final text appears 259 ms (B) or 431 ms (A) after the end of speech with audio fed at real-time speed, and the host build and the firmware produce identical transcripts. Variant A reaches 7.1%/16.4% word error rate on LibriSpeech test-clean/test-other in streaming mode with 0.64 s chunks and the on-chip language model (4.6%/10.7% with full context). Code, models and the raw board measurements are released.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Daniel Varela S\'anchez, Guillermo Mart\'in-Coello Ju\'arez
- 发布：2026-10-12；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
