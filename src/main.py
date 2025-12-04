import os
import pandas as pd
import matplotlib.pyplot as plt
from extract import extract_retail_sales, extract_cpi
from transform import merge_and_adjust
from load import save_processed  # <-- CORRECTION

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

print("\nU.S. Economic Data Pipeline – Mouhcine Riany © 2025\n")

print("Loading local data...")
print("Loading retail sales from:", os.path.join(RAW_DIR, "retail_sales_raw.csv"))
print("Loading CPI data from:", os.path.join(RAW_DIR, "cpi_monthly.csv"))

sales = extract_retail_sales()
cpi = extract_cpi()

merged = merge_and_adjust(sales, cpi)

# Save output CSV
output_path = os.path.join(PROCESSED_DIR, "merged_inflation_adjusted.csv")
save_processed(merged, output_path)  # <-- CORRECTION
print("Processed CSV saved to:", output_path)

# Drop NA for plotting
df = merged.dropna(subset=["yoy_growth_pct"])

# Plot YoY inflation-adjusted retail sales
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["yoy_growth_pct"])
plt.xlabel("Date")
plt.ylabel("YoY Growth (%)")
plt.title("Year-over-Year Real Retail Sales Growth in the U.S.")
plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(PROCESSED_DIR, "yoy_growth_plot.png"))
print("Plot saved to:", os.path.join(PROCESSED_DIR, "yoy_growth_plot.png"))
