import pandas as pd
import random


def fetch_10_consecutive_random_data_points(file_path):
    num_points=10
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print(f"File {file_path} is empty.")
            return []
        start_idx = random.randint(0, max(0, len(df) - num_points))
        return df.iloc[start_idx:start_idx + num_points].to_dict('records')
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")
        raise e
    except Exception as e:
        print(f"Error fetching data points: {e}")
        return []