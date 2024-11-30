import os
import pandas as pd
from fetch_api import fetch_10_consecutive_random_data_points
from prediction_api import predict_next_values


def process_stock_files(exchanges_directory: str):
    """
    Processes stock files within a given directory.

    Args:
        exchange_dir (str): Path to the folder containing stock files.
    """
    exchanges_dirs = [os.path.join(exchanges_directory,f)
                        for f in os.listdir(exchanges_directory)
                            if os.path.isdir(os.path.join(exchanges_directory,f))]

    if not exchanges_dirs:
        print(f"No directory found in {exchanges_directory}")
        return

    for exchange_dir in exchanges_dirs:
        for exchange_csv_file_name in os.listdir(exchange_dir):
            if exchange_csv_file_name.endswith(".csv"):
                full_path = os.path.join(exchange_dir, exchange_csv_file_name)
                stock_data = fetch_10_consecutive_random_data_points(full_path)
                if not stock_data:
                    print(f"Skipping {exchange_csv_file_name} due to missing data.")
                    continue

                predictions = predict_next_values(stock_data)
                if predictions:
                    write_predictions_to_file(full_path, stock_data, predictions)
                else:
                    print(f"Could not generate predictions for {exchange_csv_file_name}.")
                    continue

def write_predictions_to_file(file_path, original_data, predictions):
    """
    Writes the original stock data and predictions to an output CSV file.

    Args:
        file_path (str): Path to the input file being processed.
        original_data (list): Original data points as a list of lists.
        predictions (list): Predicted data points as a list of lists.

    Returns:
        None
    """
    print(predictions)
    try:
        combined_data = original_data + predictions
        df = pd.DataFrame(combined_data)

        # Write the data to a CSV file
        file_path_without_extension, _ = os.path.splitext(file_path)
        output_file = file_path_without_extension + "_expected.csv"
        df.to_csv(output_file, index=False, header=False)
        print(f"Predictions written to {output_file}")

    except Exception as e:
        print(f"Error writing predictions to file: {e}")


if __name__ == "__main__":
    DATA_DIR = "stock_price_data_files"
    process_stock_files(DATA_DIR)
