# Cycle Replacement Pipeline

This repository demonstrates a **cycle replacement analysis pipeline**
using **auto-generated fake data**.

1) No real customer data  
2) Safe for GitHub  
3) Reproducible  
4) Easy to understand  

---

## How it works

1. Generate fake data (units, customers, callbacks)
2. Run a simple pipeline that reads the data
3. Produce a summary output

---

## Quick start

```bash
pip install -r requirements.txt
python scripts/generate_fake_data.py
python -m cycle_replacement.run
