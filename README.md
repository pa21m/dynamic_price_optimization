# Dynamic Price Optimisation (Two-Stage Pipeline)

A two-stage, data-driven dynamic pricing pipeline that combines **competitive positioning** with **demand elasticity modelling** to produce guarded, actionable price recommendations.

## What’s inside

- Notebook workflow: competitor analysis → elasticity estimation → guarded optimisation → test candidate shortlist
- Setup instructions
- Optional dataset sanity-check helper (`src/quickcheck.py`)

## Repo structure

```
.
├── notebooks/
│   └── dynamic_price_optimization.ipynb
├── data/
│   └── raw/                 # put Competition_Data.csv here (git-ignored)
├── outputs/                 # notebook exports (git-ignored)
├── src/
│   └── quickcheck.py
├── reports/
│   └── figures/
├── DATA.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Data

Download the dataset using the link inside the tutorial and place it here:

```
data/raw/Competition_Data.csv
```

(See `DATA.md`.)

Optional quick check:

```bash
python -m src.quickcheck --data data/raw/Competition_Data.csv
```

## Run

Open:

- `notebooks/dynamic_price_optimization.ipynb`

Outputs (CSVs) will be saved to:

- `outputs/`

## Portfolio write-up (problem → approach → result)

**Problem:** Pricing decisions must balance competitiveness with revenue impact. Static rules can miss opportunities, especially when demand sensitivity varies across products.

**Approach:** Stage 1 analyses competitor price gaps and runs simple scenario tests. Stage 2 estimates price elasticity using a log–log regression with fixed effects and applies guardrails (e.g., price-change limits and competitor bands) to generate realistic item-level recommendations.

**Result:** A reproducible workflow that produces controlled price changes and a shortlist of low-risk test candidates for real-world experimentation (A/B testing).

---

## Credits & References

- **Tutorial reference (includes dataset download link):**  
  https://amanxai.com/2024/07/22/price-optimization-using-python/
