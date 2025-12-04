import os

def save_processed(df, output_path):
    """
    Save processed DataFrame to CSV.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
