## Import necessary libraries
import matplotlib.pyplot as plt

## Function to plot portfolio weights
def plot_portfolio_weights(weights):
    plt.figure(figsize=(12, 6))
    plt.bar(weights.index, weights)
    plt.xlabel('Stocks')
    plt.ylabel('Portfolio Weight')
    plt.title('Hierarchical Risk Parity Portfolio Weights')
    plt.show()

if __name__ == "__main__":
    ## Example weights for testing
    example_weights = {'AAPL': 0.25, 'MSFT': 0.25, 'GOOGL': 0.25, 'AMZN': 0.25}
    example_weights_series = pd.Series(example_weights)

    ## Plot the example weights
    plot_portfolio_weights(example_weights_series)
