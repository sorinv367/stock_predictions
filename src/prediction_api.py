from datetime import datetime, timedelta

def predict_next_values(data_points):
    """
    Predicts the next three stock price rows based on the given dataset.

    Args:
        data_points (list): List of lists, where each sublist contains:
            [Stock-ID, Timestamp, Stock Price].

    Returns:
        list: List of three predicted rows in the format [Stock-ID, Timestamp, Stock Price].

    Raises:
        ValueError: If the input data is empty or does not contain prices.
    """
    if not data_points:
        raise ValueError("Insufficient data points for prediction.")

    # Extract the last row's stock ID, timestamp, and stock prices
    try:
        stock_id = data_points[-1][0]
        last_timestamp = datetime.strptime(data_points[-1][1], "%d-%m-%Y")
        prices = [row[2] for row in data_points]
    except (IndexError, ValueError) as e:
        raise ValueError("Invalid data format") from e

    if len(prices) < 1:
        raise ValueError("Insufficient price data for prediction.")


    # Calculate predictions
    n = prices[-1]
    n_plus_1 = sorted(prices)[-2] if len(prices) > 1 else prices[0]
    n_plus_2 = n + (n_plus_1 - n) / 2
    n_plus_3 = n_plus_2 + (n_plus_1 - n_plus_2) / 4

    # Round predictions to 2 decimal places
    n_plus_1 = round(n_plus_1, 2)
    n_plus_2 = round(n_plus_2, 2)
    n_plus_3 = round(n_plus_3, 2)

    # Generate timestamps for the next 3 days
    next_timestamps = [(last_timestamp + timedelta(days=i)).strftime("%d-%m-%Y")
                        for i in range(1, 4)]

    # Return the predictions in the required format
    return [
        [stock_id, next_timestamps[0], n_plus_1],
        [stock_id, next_timestamps[1], n_plus_2],
        [stock_id, next_timestamps[2], n_plus_3],
    ]
