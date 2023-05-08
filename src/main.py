## Import necessary libraries
import datetime
import matplotlib.pyplot as plt

## Import functions from data_preprocessing and hrp modules
from data_preprocessing import preprocess_data
from hrp import get_hrp_portfolio_weights

## Function to plot portfolio weights
def plot_portfolio_weights(weights):
    plt.figure(figsize=(12, 6))
    plt.bar(weights.index, weights)
    plt.xlabel('Stocks')
    plt.ylabel('Portfolio Weight')
    plt.title('Hierarchical Risk Parity Portfolio Weights')
    plt.show()

## Main function to run the script
def main():
    # Define stock symbols, start date, and end date
    symbols = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    start_date = datetime.datetime(2017, 1, 1)
    end_date = datetime.datetime(2021, 12, 31)

    # Preprocess the data
    returns = preprocess_data(symbols, start_date, end_date)

    # Calculate HRP weights
    hrp_weights = get_hrp_portfolio_weights(returns)

    # Print and plot the weights
    print(hrp_weights)
    plot_portfolio_weights(hrp_weights)

if __name__ == "__main__":
    main()
