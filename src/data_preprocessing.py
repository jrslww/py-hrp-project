## Import necessary libraries
import pandas as pd
import pandas_datareader as pdr
import datetime


## Function to fetch stock data from Yahoo Finance
def fetch_stock_data(symbols, start_date, end_date):
    stock_data = pdr.get_data_yahoo(symbols, start=start_date, end=end_date)
    return stock_data["Adj Close"]


## Function to calculate percentage returns from the stock prices
def calculate_returns(stock_prices):
    return stock_prices.pct_change().dropna()


## Main function to preprocess the data
def preprocess_data(symbols, start_date, end_date):
    # Fetch stock data
    stock_prices = fetch_stock_data(symbols, start_date, end_date)

    # Calculate returns
    returns = calculate_returns(stock_prices)

    return returns


if __name__ == "__main__":
    ## Define stock symbols, start date, and end date for testing
    symbols = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    start_date = datetime.datetime(2017, 1, 1)
    end_date = datetime.datetime(2021, 12, 31)

    ## Preprocess the data and print the first few rows
    returns = preprocess_data(symbols, start_date, end_date)
    print(returns.head())
