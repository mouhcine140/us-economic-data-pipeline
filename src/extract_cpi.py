import pandas as pd

def extract_cpi():
    print("Loading local CPI data...")
    df = pd.read_csv("../data/raw/cpi_raw.csv")
    df["date"] = pd.to_datetime(df["date"])
    print(f"   → {len(df)} monthly records loaded")
    return df
