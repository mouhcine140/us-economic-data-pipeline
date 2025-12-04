import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")

def extract_retail_sales():
    path = os.path.join(RAW_DIR, "retail_sales_raw.csv")
    print(f"Loading retail sales from: {path}")
    return pd.read_csv(path)

def extract_cpi():
    path = os.path.join(RAW_DIR, "cpi_monthly.csv")
    print(f"Loading CPI data from: {path}")
    return pd.read_csv(path)
