---
title: "O\\'ido: Open-Vocabulary Speech Recognition on a $5 Microcontroller without a Neural Accelerator"
description: "Speech recognition on low-cost microcontrollers is, in practice, limited to keyword spotting or a fixed list of commands."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.13447) · [PDF](https://arxiv.org/pdf/2610.13447)

## 一句话摘要

Speech recognition on low-cost microcontrollers is, in practice, limited to keyword spotting or a fixed list of commands.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speech recognition on low-cost microcontrollers is, in practice, limited to keyword spotting or a fixed list of commands. We present O\'ido, an inference engine that runs open-vocabulary English speech recognition entirely on an ESP32-S3 (240 MHz dual-core Xtensa LX7, 512 KB of SRAM, 8 MB of PSRAM, 16 MB of flash, no neural accelerator). O\'ido executes a 13M-parameter Conformer-CTC model with int8 weights, per-frame dynamic int8 activations and int8 attention on the chip's SIMD instructions, with a schedule designed around flash and PSRAM bandwidth. On LibriSpeech test-clean/test-other the on-device arithmetic reaches 3.70%/8.23% word error rate (WER), within 0.12 points of full precision, and 3.33%/7.15% with an on-chip 1.3M-parameter language model; a transducer head gives 2.99%/6.67% and an int4 variant fits in 8.3 MB. This is 2.3-2.8x fewer errors than the vendor's recognizer on the same chip, and fewer than Whisper tiny.en and Moonshine tiny in full precision on a laptop, including in real noise and reverberation. Measured on a physical board, the firmware runs at 1.97x the duration of the audio on one core, with transcripts identical to an instruction-exact emulator: accurate, but not yet real time (a 4 s command is transcribed about 8.7 s after it ends). The two-core schedule gives wrong results on silicon and is disabled. A streaming variant shows partial text while the speaker talks and delivers the final text 4.1-11.1 s after clips of 3.6-10.6 s (7.2-22.4 s in utterance mode) at 4.86%/11.03% WER; a Spanish model makes 34-60% fewer errors than multilingual Whisper tiny. Code and models are released.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Daniel Varela S\'anchez, Guillermo Mart\'in-Coello Ju\'arez
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
