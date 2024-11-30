import pytest
from src.prediction_api import predict_next_values
from datetime import datetime, timedelta

def test_predict_normal_dataset():
    """
    Test prediction with a normal dataset containing stock details.
    """
    SAMPLE_DATA = [
        ["FLTR", "01-09-2023", 16340.00],
        ["FLTR", "02-09-2023", 16258.30],
        ["FLTR", "03-09-2023", 16274.56],
        ["FLTR", "04-09-2023", 16176.91],
        ["FLTR", "05-09-2023", 16419.56],
        ["FLTR", "06-09-2023", 16288.21],
        ["FLTR", "07-09-2023", 16483.67],
        ["FLTR", "08-09-2023", 16516.63],
        ["FLTR", "09-09-2023", 16401.02],
        ["FLTR", "10-09-2023", 16384.62],
    ]

    result = predict_next_values(SAMPLE_DATA)

    stock_id = "FLTR"
    last_timestamp = datetime.strptime("10-09-2023", "%d-%m-%Y")
    expected_timestamps = [
        (last_timestamp + timedelta(days=i)).strftime("%d-%m-%Y")
        for i in range(1, 4)
    ]

    expected_prices = [16483.67, 16434.15, 16446.53]

    # Check Stock-ID and Timestamp
    for i, row in enumerate(result):
        assert row[0] == stock_id
        assert row[1] == expected_timestamps[i]

    # Check prices
    for actual_price, expected_price in zip([row[2] for row in result], expected_prices):
        assert actual_price == pytest.approx(expected_price, rel=1e-2)

def test_predict_empty_dataset():
    """
    Test prediction with an empty dataset, expecting a ValueError.
    """
    SAMPLE_DATA = []
    with pytest.raises(ValueError, match="Insufficient data points for prediction."):
        predict_next_values(SAMPLE_DATA)


def test_predict_invalid_dataset_format():
    """
    Test prediction with a dataset missing required elements, expecting a ValueError.
    """
    SAMPLE_DATA = [
        ["FLTR", "01-09-2023"],
        ["FLTR", "02-09-2023"],
        ["FLTR", "03-09-2023"],
        ["FLTR", "04-09-2023"],
        ["FLTR", "05-09-2023"],
        ["FLTR", "06-09-2023"],
        ["FLTR", "07-09-2023"],
        ["FLTR", "08-09-2023"],
        ["FLTR", "09-09-2023"],
        ["FLTR", "10-09-2023"],
    ]
    with pytest.raises(ValueError, match="Invalid data format"):
        predict_next_values(SAMPLE_DATA)
