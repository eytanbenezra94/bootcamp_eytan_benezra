# Homework 6 — Data Preprocessing

## Cleaning Strategy
Functions are in `src/cleaning.py`. Columns with too many missing values get
dropped, the rest get filled with the median, then scaled to 0-1.