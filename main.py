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
fund_profiles = dict()
fund_profiles['Fund1'] = (32.61, ["idx11", "idx12", "idx13"])
fund_profiles['Fund2'] = (17.08, ["idx21", "idx22", "idx23"])
fund_profiles['Fund3'] = (98.39, ["idx31", "idx32", "idx33"])


#############################################
#    HISTORICAL FUND PRICES
#############################################
fund_prices = dict()
for name in fund_names:

    start_price = fund_profiles[name][0]
    best_index = fund_profiles[name][1][0]
    fund_prices[name] = start_price + start_price * market_changes * beta





# Create 5 funds with list of indices



