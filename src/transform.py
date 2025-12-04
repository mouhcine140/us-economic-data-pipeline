import pandas as pd

def preprocess_sales(df):
    df = df.copy()
    df["date"] = pd.to_datetime(df["observation_date"])
    df.rename(columns={"RSXFS": "retail_sales"}, inplace=True)
    return df[["date", "retail_sales"]]

def preprocess_cpi(df):
    df = df.copy()
    df["date"] = pd.to_datetime(df["observation_date"])
    df.rename(columns={"CPIAUCSL": "cpi"}, inplace=True)
    return df[["date", "cpi"]]

def merge_and_adjust(sales_df, cpi_df):
    sales = preprocess_sales(sales_df)
    cpi = preprocess_cpi(cpi_df)

    merged = pd.merge(sales, cpi, on="date", how="inner")
    
    # Adjust for inflation
    merged["real_retail_sales"] = merged["retail_sales"] / merged["cpi"] * 100

    # Compute YoY growth (12 months difference)
    merged["yoy_growth_pct"] = merged["real_retail_sales"].pct_change(periods=12) * 100

    return merged
