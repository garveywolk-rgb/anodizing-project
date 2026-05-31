# Anodizing Project — Master Workspace

Everything for my self-directed anodized-aluminum study lives here: code, data, images,
notebook, documents, and final outputs. One home, one structure, so nothing gets lost
between now and November.

**Garvey Wolk — B.S. Materials Science & Engineering, Drexel University**

---

## The one-sentence thesis

> Anodizing parameters (voltage, time, electrolyte temperature, surface prep) control the
> structure of the aluminum-oxide layer, and that structure determines the properties I can
> measure: thickness, color uptake, hardness, and wettability.

## Folder map

```
anodizing-project/
├── 00_admin/          Project plan, checklist, shopping list, budget tracker
├── 01_docs/           The full project document, write-up drafts, references I write
├── 02_lab-notebook/   Dated session logs — the most important folder for interviews
├── 03_data/
│   ├── raw/           Untouched data as collected (per-session CSVs, ImageJ exports)
│   └── processed/     The cleaned master dataset + anything derived from raw
├── 04_images/
│   ├── coupons/       Standardized photos of each finished coupon
│   ├── contact-angle/ Side-on droplet photos for wettability
│   ├── wear/          Before/after abrasion photos
│   ├── failures/      Botched coupons — keep these, they're interview gold
│   └── figures/       Generated plots for the report and poster
├── 05_code/
│   ├── analysis/      Python: 720-rule calc, plotting, stats
│   ├── imagej/        ImageJ macros + notes for repeatable measurement
│   └── utils/         Small helpers (file naming, data validation)
├── 06_outputs/
│   ├── report/        The polished technical write-up
│   └── poster/        The one-page figure sheet / mini-poster
└── 07_references/     Papers, datasheets, saved web sources I rely on
```

## How to work in here (the rules I set for myself)

1. **Raw data is sacred.** Once a file lands in `03_data/raw/`, I never edit it. All cleaning
   happens in code and writes to `03_data/processed/`. This means I can always re-run analysis
   from scratch and trust it.
2. **One naming convention, everywhere.** See `00_admin/CONVENTIONS.md`. Every coupon photo,
   data row, and notebook entry uses the same coupon ID (e.g. `B2-1`).
3. **Log the session before I forget it.** Fill in the notebook entry the same day, including
   what went wrong. Future-me at an interview depends on present-me being honest here.
4. **Code reads from `03_data/`, writes figures to `04_images/figures/`.** Nothing hardcoded
   to my desktop; paths stay relative so the repo is portable.

## Quick start each session

- Before a run: open `02_lab-notebook/`, copy the template, fill in the plan.
- Compute targets: `python 05_code/analysis/anodizing_720.py`.
- After measuring: add rows to `03_data/processed/measurements.csv`, drop photos in `04_images/`.
- To make plots: `python 05_code/analysis/plot_results.py`.

## GitHub

This whole folder is the repo. The parts that go public are the code, the processed dataset,
the figures, and the docs. Large raw image dumps and scratch files are kept local via
`.gitignore`. See `00_admin/GITHUB.md` for the push workflow.
