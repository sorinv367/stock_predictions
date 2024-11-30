def predict_next_values(data_points):
    """
    Predicts the next three stock prices based on the given dataset.

    Args:
        data_points (list): List of lists, where each sublist contains:
            [Stock-ID, Timestamp, stock price].

    Returns:
        list: List of three predicted prices.

    Raises:
        ValueError: If the input data is empty or does not contain prices.
    """
    if not data_points:
        raise ValueError("Insufficient data points for prediction.")
    
    if len(data_points) < 10:
        raise ValueError("Insufficient data for prediction.")
    
    # Extract the stock prices
    try:
        prices = [row[2] for row in data_points]
    except IndexError:
        raise ValueError("Invalid data format. Expected each row to have at least three elements.")



    # Perform predictions
    n = prices[-1]
    n_plus_1 = sorted(prices)[-2] if len(prices) > 1 else prices[0]
    n_plus_2 = n + (n_plus_1 - n) / 2
    n_plus_3 = n_plus_2 + (n_plus_1 - n_plus_2) / 4

    return [n_plus_1, n_plus_2, n_plus_3]
