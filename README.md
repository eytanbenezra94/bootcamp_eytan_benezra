# Bootcamp Repository

## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.

## Class Materials Rules
- Each stage's handouts go in their own subfolder, named exactly as the course folder, e.g. `class_materials/stage01_problem-framing-and-scoping/`.
- Run lecture notebooks in place from that folder.
- Copy a homework starter into `homework/homeworkN/` before working on it.

## Project Folder Rules
- Keep project files organized and clearly named.
- The project folder structure is set up in Stage 02.

---

# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Portfolio Manager picking which sector to invest into usually just with a good feeling. I want just a simple monthly ranking based on momentum so they have real numbers instead.

## Stakeholder & User
PM makes the call. I'd run the signal and give them the ranking.

## Useful Answer & Decision
Predictive with ranked list of different sectors by momentum, updated monthly.


## Assumptions & Constraints
- need daily price data, no gaps
-  momentum probably doesn't stay more than a month 

## Known Unknowns / Risks
- regime changes could break the pattern
- sectors move together during a crash, ranking gets less useful

## Lifecycle Mapping
- define problem → Stage 01 → this README
- set up env → Stage 02 → repo, .env, requirements.txt
- write code → Stage 03 → src/utils.py
- pull data → Stage 04 → data/raw
- store results → Stage 05 → data/processed

## Repo Plan
Everything lives in project/, updated each stage.


## Data Storage (Stage 05)
Raw files live in `data/raw/` (CSV), processed files in `data/processed/` (Parquet).
Paths are env-driven via `DATA_DIR_RAW` / `DATA_DIR_PROCESSED` in `.env`, never hardcoded.

## Data Preprocessing (Stage 06)
Cleaning functions live in each homework's `src/cleaning.py`: median imputation for
sparse-but-usable columns, dropping columns above a missing-value threshold, and
min-max normalization. Applied to `data/raw/sample_data.csv`, saved to `data/processed/`.


## Exploratory Data Analysis (Stage 08)
Profiled numeric and categorical columns, checked distributions and time-series
behavior. Reusable `eda_summary()` helper lives in each homework's `src/eda.py`.