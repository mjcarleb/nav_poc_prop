import statsmodels.api as m
import numpy as np
import matplotlib.pyplot as plt

# For repeatability
np.random.seed(1)

#############################################
#    HISTORICAL MARKET PRICE CHANGES
#############################################
market_changes = np.random.normal(loc=.07/220, scale=.01, size=90)
print(f"Mean of daily price change = {np.mean(market_changes)}")
print(f"220 * mean = {220 *np.mean(market_changes)}")


#############################################
#    INDEX PROFILES
#############################################
index_names = [f"idx{n}" for n in range(11,34)]
index_betas = dict()
for name in index_names:

    #start_price = np.random.uniform(low=10, high=110)
    beta = np.random.uniform(low=-1, high=1)
    index_betas[name] = beta


#############################################
#    HISTORICAL INDEX PRICE CHANGES
#############################################
index_changes = dict()
for name in index_names:

    beta = index_betas[name]
    index_changes[name] = market_changes * beta


#############################################
#    FUND PROFILES
#############################################
fund_names = ["Fund1", "Fund2", "Fund3"]
fund_indices = dict()
fund_indices['Fund1'] = ["idx11", "idx12", "idx13"]
fund_indices['Fund2'] = ["idx21", "idx22", "idx23"]
fund_indices['Fund3'] = ["idx31", "idx32", "idx33"]


#############################################
#    HISTORICAL FUND PRICE CHANGES
#############################################
fund_changes = dict()
for name in fund_names:

    best_index = fund_indices[name][0]
    fund_changes[name] = index_changes[best_index] + np.noraml.random(loc=0, scale=.0001)
