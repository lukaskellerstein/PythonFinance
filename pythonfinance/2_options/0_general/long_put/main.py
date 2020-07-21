import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# S = stock underlying
# K = strike price
# Price = premium paid for option
def long_put(S, K, Price):
    # Long Put Payoff = max(Strike Price - Stock Price, 0)
    # # If we are long a call, we would only elect to call if the current stock price is less than
    # the strike price on our option
    P = list(map(lambda x: max(K - x, 0) - Price, S))
    return P


def long_put_turning_point(K, Price):
    return K - Price


S = range(0, 200)  # Define some series of stock-prices
optionPrices = long_put(S, 100, 10)  # option price
turning_point = long_put_turning_point(100, 10)


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
