# Homework 5 — Data Storage

## Data Storage
Raw data is saved as CSV in `data/raw/`, processed data as Parquet in
`data/processed/`. Parquet keeps the column types and loads faster. Paths
come from `.env` instead of being hardcoded.