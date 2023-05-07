## Import necessary libraries
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, leaves_list
from scipy.spatial.distance import pdist, squareform
from sklearn.preprocessing import MinMaxScaler


## Function to calculate the inverse-variance portfolio weights
def get_inverse_variance_weights(cov_matrix):
    ivp = 1 / np.diag(cov_matrix)
    weights = ivp / ivp.sum()
    return pd.Series(weights, index=cov_matrix.index)


## Function to sort the covariance matrix using a hierarchical tree
def sort_cov_matrix(cov_matrix, method="single"):
    dists = pdist(cov_matrix)
    linkage_matrix = linkage(dists, method=method)
    sorted_idx = leaves_list(linkage_matrix)
    return cov_matrix.iloc[sorted_idx, sorted_idx]


## Function to compute HRP weights recursively
def compute_hrp_weights(cov_matrix, method="single"):
    if len(cov_matrix) == 1:
        return pd.Series(1, index=cov_matrix.index)

    sorted_cov_matrix = sort_cov_matrix(cov_matrix, method)

    left_idx = sorted_cov_matrix.index[0:len(cov_matrix) // 2]
    right_idx = sorted_cov_matrix.index[len(cov_matrix) // 2:]

    left_cov = sorted_cov_matrix.loc[left_idx, left_idx]
    right_cov = sorted_cov_matrix.loc[right_idx, right_idx]

    left_weights = compute_hrp_weights(left_cov)
    right_weights = compute_hrp_weights(right_cov)

    total_weights = pd.concat([left_weights, right_weights], axis=0)

    left_variance = np.dot(left_weights.T, np.dot(left_cov, left_weights))
    right_variance = np.dot(right_weights.T, np.dot(right_cov, right_weights))

    alpha = 1 - left_variance / (left_variance + right_variance)

    hrp_weights = total_weights * np.append(alpha, 1 - alpha)
    return hrp_weights


## Function to calculate HRP portfolio weights
def get_hrp_portfolio_weights(returns, method="single"):
    cov_matrix = returns.cov()
    hrp_weights = compute_hrp_weights(cov_matrix, method)
    return hrp_weights


if __name__ == "__main__":
    ## Create some sample data for testing
    np.random.seed(42)
    num_assets = 5
    num_data_points = 1000
    returns = pd.DataFrame(np.random.normal(size=(num_data_points, num_assets)), columns=list('ABCDE'))

    ## Calculate HRP weights
    hrp_weights = get_hrp_portfolio_weights(returns)
    print(hrp_weights)
