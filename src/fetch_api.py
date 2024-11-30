import random
import pandas as pd


def fetch_10_consecutive_random_data_points(file_path):
    """
    Fetches 10 consecutive random data points from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row in the file.
              Returns an empty list if the file is empty or an error occurs.

    Raises:
        FileNotFoundError: If the file does not exist.
        Exception: For any unexpected errors during execution.
    """
    num_points=10
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print(f"File {file_path} is empty.")
            return []
        start_idx = random.randint(0, max(0, len(df) - num_points))
        return df.iloc[start_idx:start_idx + num_points].values.tolist()
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")
        raise e
    except Exception as e:
        print(f"Error fetching data points: {e}")
        return []
