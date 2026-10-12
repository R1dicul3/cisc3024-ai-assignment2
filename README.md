# CISC3024 Pattern Recognition — AI Assignment #2

**Bayes-PFL: Bayesian Prompt Flow Learning for Zero-Shot Anomaly Detection**

This repository contains the complete, AI-produced work for AI Assignment #2 of CISC3024 (Pattern Recognition).
The assignment required finding a *recent* classification/recognition algorithm based on **probability / Bayes theory**
with a computer-vision application, and implementing it entirely with an AI agent (no hand-written code).

- **Chosen algorithm**: Bayes-PFL (CVPR 2025, arXiv:2503.10080) — models the CLIP *prompt space as a learnable probability
  distribution* (variational inference + normalizing flows) and samples diverse prompts for zero-shot anomaly detection.
- **Report**: [REPORT.md](REPORT.md) (English, with the 6 required sections).
- **Evidence trail**: [PROMPTS.md](PROMPTS.md) (how the AI found and implemented the algorithm).
- **Candidate search**: [CANDIDATES.md](CANDIDATES.md) (the full filtered shortlist).

## Layout

- `Bayes-PFL/` — the adapted official pipeline (ViT-B-16 backbone, 8 GB-friendly; see REPORT.md §3.3 for all changes).
- `tools/` — AI-written helper scripts (candidate search, data prep, smoke tests, launch scripts).
- `REPORT.md`, `PROMPTS.md`, `CANDIDATES.md`, `REQUIREMENTS.md` — documentation.

## Reproducing

Environment: Python 3.13, PyTorch 2.11 + CUDA, an 8 GB NVIDIA GPU. Data and weights are **not** committed.

1. Download OpenAI `ViT-B-16.pt` into `Bayes-PFL/pretrained_weight/`.
2. Download VisA (`VisA_20220922.tar`, ~1.93 GB) and run `tools/prep_visa.py` to standardize it.
3. `tools/run_train.ps1` trains on 7 auxiliary VisA categories; then `test.py` evaluates on 5 held-out categories.

## Note on the zero-shot protocol

The paper trains on one dataset and tests on another. Since only VisA is freely downloadable, this work uses a
**within-VisA zero-shot split**: train on 7 auxiliary categories, evaluate on 5 **held-out, unseen** categories
(pcb1–pcb4, pipe_fryum). See REPORT.md §3.3.

## Credit

Bayes-PFL: Zhen Qu et al., CVPR 2025 — <https://github.com/xiaozhen228/Bayes-PFL>
