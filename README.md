Stock Price Prediction Tool

Requirements:
Python 3.8 or higher
pip

Install dependencies:
pip install -r requirements.txt

Place your CSV files in the stock_price_data_files directory, the format should be:

stock_price_data_files/

├── EXCHANGE_NAME1/

│   ├── FILE1.csv

│   ├── FILE2.csv

├── EXCHANGE_NAME2/

│   ├── FILE3.csv

│   ├── FILE4.csv
                  

How to run app: in root dirt, run the program with the following command:
python src/main.py

How to run tests, in root dir:
pytest
