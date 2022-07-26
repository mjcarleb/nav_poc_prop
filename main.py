import statsmodels.api as m
import numpy as np
import matplotlib.pyplot as plt

# For repeatability
np.random.seed(1)

#############################################
#    HISTORICAL MARKET PRICES
#############################################
market_changes = np.random.normal(loc=.07/220, scale=.01, size=90)
#plt.plot(market_changes)
#plt.show()
print(f"Mean of daily price change = {np.mean(market_changes)}")
print(f"220 * mean = {220 *np.mean(market_changes)}")

#############################################
#    INDEX PROFILES
#############################################
index_names = [f"idx{n}" for n in range(11,34)]
index_profiles = dict()
for name in index_names:

    start_price = np.random.uniform(low=10, high=110)
    beta = np.random.uniform(low=-1, high=1)
    index_profiles[name] = [start_price, beta]

#############################################
#    HISTORICAL INDEX PRICES
#############################################

index_prices = dict()
for name in index_names:

    start_price = index_profiles[name][0]
    beta = index_profiles[name][1]
    index_prices[name] = start_price + start_price * market_changes * beta

# Create 5 funds with list of indices
funds = dict()
funds['Fund1'] = ["idx11", "idx12", "idx13"]
funds['Fund2'] = ["idx21", "idx22", "idx23"]
funds['Fund3'] = ["idx31", "idx32", "idx33"]


