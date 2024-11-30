import pytest
from src.prediction_api import predict_next_values

def test_predict_10_rows():
    """
    Test prediction with a dataset containing 10 stock details.
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
    # Expected results:
    # Prices = [16340.00, 16258.30, 16274.56, 16176.91, 16419.56, 16288.21, 16483.67, 16516.63, 16401.02, 16384.62]
    # n = 16384.62
    # n_plus_1 = 16483.67 (second-highest)
    # n_plus_2 = 16384.62 + (16483.67 - 16384.62) / 2 = 16434.145
    # n_plus_3 = 16434.145 + (16483.67 - 16434.145) / 4 = 16446.52625
    expected = [16483.67, 16434.145, 16446.52625]
    assert result == pytest.approx(expected, rel=1e-9)



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
    with pytest.raises(ValueError, match="Invalid data format. Expected each row to have at least three elements."):
        predict_next_values(SAMPLE_DATA)
