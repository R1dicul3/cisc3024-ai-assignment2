# Evidence trail — AI-driven workflow (Assignment #2)

This file logs the actual sequence of AI decisions/actions that produced this assignment.
It is evidence for report sections 1 ("how AI found the algorithm") and 3 ("how AI implemented it").
No code was written by the human author.

## Phase 1 — Algorithm search (evidence for §1)
1. Read the assignment PDF (AIassign2.pdf): needs a *recent probability/Bayes-based classification/recognition algorithm* for CV/PR, done entirely by AI.
2. Queried arXiv official API (not search snippets) with e.g.
   - cat:cs.CV AND abs:"Bayesian" AND abs:"classification"
   - abs:"variational" AND abs:"posterior" AND cat:cs.CV
   sorted by submission date.
3. Queried GitHub API to verify each candidate has real, maintained public code.
4. Filtered with 5 hard criteria (Bayes-core / recent / CV-recognition / public code / 8GB-feasible).
5. Selected **Bayes-PFL** (CVPR 2025, arXiv:2503.10080, github.com/xiaozhen228/Bayes-PFL).
   Rejected: H²EDL (Dirichlet overlap w/ Assign#1), Bella (no repo), Bayesian Flow Networks (2023, stale), RDC (ICML 2024, oldest), app-only papers (Bayes not the contribution).

## Phase 2 — Environment & data
6. Confirmed local stack: Python 3.13.5, torch 2.11.0+cu128, RTX 4060 8GB, CUDA available.
7. Downloaded VisA (1.93 GB) + OpenAI ViT-B-16 weights (350 MB). (MVTec skipped: requires registration.)
8. Reproduced the repo's data pipeline (make_VAND + metaSolver) to build the standardized VisA set + meta_visa.json.
9. Fixed pandas 2.x integer-positional indexing (data[n] -> data.iloc[n]) in the dataset script.

## Phase 3 — Adaptation to 8 GB (evidence for §3)
10. Re-targeted backbone: ViT-L-14-336 -> ViT-B-16; image_size 518 -> 224; features_list [6,12,18,24] -> [3,6,9,12].
11. Budget: batch 32 -> 8; epochs 30 -> 6.
12. Within-VisA zero-shot protocol: train 7 aux categories, validate/test 5 held-out unseen categories (pcb1-4, pipe_fryum).
13. Removed dead imports: imgaug (unused DRAEM path), open_clip_local (unused/commented).
14. Added --product_list to test.py for held-out-only evaluation.
15. Smoke-tested full forward+backward in BOTH train and test modes before the long run (model 13.08 M params, gradients verified).

## Phase 4 — Training & evaluation
16. Trained on 7 auxiliary VisA categories (1,210 images, batch 8, 6 epochs, ~8 min/epoch on 8GB).
    val pixel-AP on held-out: 0.0885 -> 0.1146 -> 0.1172 (loss_cls 0.706 -> 0.650, KL 51.9 -> 38.5).
17. Final test on the 5 held-out categories (checkpoint epoch 6, MC sample_num=10):
    pixel AUROC 92.94% (macro-mean), image AUROC 64.80%.
    per-category image/pixel AUROC: pcb1 43.5/96.2, pcb2 55.0/90.5, pcb3 47.4/89.1, pcb4 82.1/93.4, pipe_fryum 96.1/95.6.

## Phase 5 — Report & delivery
18. Wrote the English report (REPORT.md) with the 6 required sections.
19. Published code to GitHub: https://github.com/R1dicul3/cisc3024-ai-assignment2 (created via gh CLI, authenticated as R1dicul3).

---
*Key commands / scripts (all AI-generated): tools/find_candidates.py (arXiv+GitHub search), tools/prep_visa.py (data), tools/smoke_forward.py (correctness smoke), tools/run_train.ps1 (training).*
