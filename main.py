import statsmodels.api as m
import numpy as np
import matplotlib.pyplot as plt


# For repeatability
np.random.seed(1)

# Create historical market prices
market_prices = np.random.normal(loc=.07/220, scale=.01, size=90)
plt.plot(market_prices)
plt.show()
print(f"Mean of daily price change = {np.mean(market_prices)}")
print(f"220 * mean = {220 *np.mean(market_prices)}")

# Create historical index prices
index_names = [f"idx{n}" for n in range(11,34)]
index_profiles = dict()
for name in index_names:

    start_price = 32 # make random
    beta = 0.8 # make random

    index_profiles[name] = [start_price, beta]



# Create 5 funds with list of indices
funds = dict()
funds['Fund1'] = ["idx11", "idx12", "idx13"]
funds['Fund2'] = ["idx21", "idx22", "idx23"]
funds['Fund3'] = ["idx31", "idx32", "idx33"]


