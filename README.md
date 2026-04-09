# Cycle Replacement Pipeline

This repository contains a **clean, reproducible Python pipeline** for
cycle replacement proposal generation.

## What this project does
- Loads unit, customer, callback, and cycle data
- Identifies cycle replacement targets
- Calculates proposal schedule and cost
- Outputs structured datasets for quotation and reporting

## Data safety
- No real customer data is stored
- All data in `sample_data/` is **falsified**
- Real data paths are configured via `config.yaml` (not committed)

## How to use (high level)
1. Copy `config/config.example.yaml` → `config/config.yaml`
2. Replace paths with your own data
3. Run `python -m cycle_replacement.run`

This structure is designed for **GitHub readers** and **internal handover**.
