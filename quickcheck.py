"""Quick sanity checks for the pricing dataset.

Usage:
  python -m src.quickcheck --data data/raw/Competition_Data.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True)
    args = parser.parse_args()

    df = pd.read_csv(Path(args.data))
    print("Shape:", df.shape)
    print("\nColumns:", list(df.columns))

    required = ["Fiscal_Week_ID", "Item_ID", "Store_ID", "Item_Price", "Competition_Price", "Item_Quantity"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        print("\nMissing required columns:", missing)
    else:
        print("\nRequired columns present ✅")

    print("\nMissing values (top 15):")
    print(df.isna().sum().sort_values(ascending=False).head(15))

    print("\nHead:")
    print(df.head(5).to_string(index=False))


if __name__ == "__main__":
    main()
