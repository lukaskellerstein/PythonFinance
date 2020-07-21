import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --------------------
# HELPER
def long_put(S, K, Price):
    return list(map(lambda x: max(K - x, 0) - Price, S))


# --------------------

# S = stock underlying
# K = strike price
# Price = premium paid for option
def short_put(S, K, Price):
    # Payoff a short put is just the inverse of the payoff of a long put
    P = long_put(S, K, Price)
    return [-1.0 * p for p in P]


def short_put_turning_point(K, Price):
    return K - Price


S = range(0, 200)  # Define some series of stock-prices
optionPrices = short_put(S, 100, 10)  # option price
turning_point = short_put_turning_point(100, 10)

# axes
plt.grid(True, which="both")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")

# plot
plt.plot(S, optionPrices)
plt.scatter(turning_point, 0)
plt.annotate(
    f"({turning_point},0)",  # this is the text
    (turning_point, 0),  # this is the point to label
    textcoords="offset points",  # how to position the text
    xytext=(0, 10),  # distance from text to points (x,y)
    ha="center",
)

plt.show()
