import pytest
import pandas as pd
from src.fetch_api import fetch_10_consecutive_random_data_points

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

@pytest.fixture
def create_test_csv(tmp_path):
    """
    Creates a temporary CSV file with sample data for testing.
    """
    file_path = tmp_path / "test_stock_data.csv"
    df = pd.DataFrame(SAMPLE_DATA)
    df.to_csv(file_path, index=False)
    return file_path


def test_fetch_10_rows(create_test_csv):
    """
    Test if the function fetches exactly 10 rows when data is sufficient.
    """
    file_path = create_test_csv
    result = fetch_10_consecutive_random_data_points(file_path)
    assert len(result) == 10
    assert isinstance(result, list)
    assert all(len(row) == 3 for row in result)

def test_empty_file(tmp_path):
    """
    Test if the function handles empty files gracefully.
    """
    file_path = tmp_path / "test_empty.csv"
    file_path.touch()

    result = fetch_10_consecutive_random_data_points(file_path)
    assert result == []

def test_missing_file():
    """
    Test if the function raises a FileNotFoundError for a missing file.
    """
    with pytest.raises(FileNotFoundError):
        fetch_10_consecutive_random_data_points("non_existent_file.csv")

def test_invalid_file_format(tmp_path):
    """
    Test if the function handles invalid file formats gracefully.
    """
    file_path = tmp_path / "test_invalid.csv"
    with open(file_path, "w") as f:
        f.write("Invalid content")

    result = fetch_10_consecutive_random_data_points(file_path)
    assert result == []
