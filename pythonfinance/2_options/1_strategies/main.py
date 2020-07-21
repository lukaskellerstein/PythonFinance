import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------
# -----------------------------------------------------------
# BASIC strategies
# -----------------------------------------------------------
# -----------------------------------------------------------

# S = stock underlying
# K = strike price
# Price = premium paid for option
def long_call(S, K, Price):
    # Long Call Payoff = max(Stock Price - Strike Price, 0)
    # If we are long a call, we would only elect to call if the current stock price is greater than
    # the strike price on our option
    P = list(map(lambda x: max(x - K, 0) - Price, S))
    return P


def long_put(S, K, Price):
    # Long Put Payoff = max(Strike Price - Stock Price, 0)
    # If we are long a call, we would only elect to call if the current stock price is less than
    # the strike price on our option
    P = list(map(lambda x: max(K - x, 0) - Price, S))
    return P


def short_call(S, K, Price):
    # Payoff a shortcall is just the inverse of the payoff of a long call
    P = long_call(S, K, Price)
    return [-1.0 * p for p in P]


def short_put(S, K, Price):
    # Payoff a short put is just the inverse of the payoff of a long put
    P = long_put(S, K, Price)
    return [-1.0 * p for p in P]


# -----------------------------------------------------------
# -----------------------------------------------------------
# ADVANCED strategies
# -----------------------------------------------------------
# -----------------------------------------------------------


def bull_spread(S, E1, E2, Price1, Price2):

    P_1 = long_call(S, E1, Price1)
    P_2 = short_call(S, E2, Price2)
    return [x + y for x, y in zip(P_1, P_2)]


def bear_spread(S, E1, E2, Price1, Price2):

    P = bull_spread(S, E1, E2, Price1, Price2)
    return [-1.0 * p + 1.0 for p in P]


def straddle(S, E, Price1, Price2):

    P_1 = long_call(S, E, Price1)
    P_2 = long_put(S, E, Price2)
    return [x + y for x, y in zip(P_1, P_2)]


def risk_reversal(S, E1, E2, Price1, Price2):

    P_1 = long_call(S, E1, Price1)
    P_2 = short_put(S, E2, Price2)
    return [x + y for x, y in zip(P_1, P_2)]


def strangle(S, E1, E2, Price1, Price2):

    P_1 = long_call(S, E1, Price1)
    P_2 = long_put(S, E2, Price2)
    return [x + y for x, y in zip(P_1, P_2)]


def butterfly_spread(S, E1, E2, E3, Price1, Price2, Price3):

    P_1 = long_call(S, E1, Price1)
    P_2 = long_call(S, E3, Price3)
    P_3 = short_call(S, E2, Price2)
    P_3 = [2 * p for p in P_3]
    return [x + y + z for x, y, z in zip(P_1, P_2, P_3)]


def strip(S, E1, Price1, Price2):

    P_1 = long_call(S, E1, Price1)
    P_2 = long_put(S, E1, Price2)
    P_2 = [2 * p for p in P_2]
    return [x + y for x, y in zip(P_1, P_2)]


# -----------------------------------------------------------
# -----------------------------------------------------------
# PLOT
# -----------------------------------------------------------
# -----------------------------------------------------------
S = [t / 5 for t in range(0, 1000)]  # Define some series of stock-prices

fig, ax = plt.subplots(nrows=3, ncols=2, sharex=True, sharey=True, figsize=(30, 25))
fig.suptitle(
    "Payoff Functions for Long/Short Put/Calls", fontsize=20, fontweight="bold"
)
fig.text(
    0.5, 0.08, "Stock/Underlying Price ($)", ha="center", fontsize=18, fontweight="bold"
)
fig.text(
    0.08,
    0.5,
    "Option Payoff ($)",
    va="center",
    rotation="vertical",
    fontsize=18,
    fontweight="bold",
)

plt.subplot(321)
P = butterfly_spread(S, 100, 125, 150, 10, 5, 5)
P_1 = long_call(S, 100, 10)
P_2 = long_call(S, 150, 5)
P_3 = short_call(S, 125, 5)
P_3 = [2 * p for p in P_3]
plt.plot(S, P_1, "r")
plt.plot(S, P_2, "r--")
plt.plot(S, P_3, "b--")
plt.plot(S, P)
plt.legend(["Long Call", "Long Call", "Short Call", "Butterfly Spread"])
plt.title("Butterfly Spread")

plt.subplot(322)
P1 = bull_spread(S, 50, 100, 15, 10)
long_c = long_call(S, 50, 15)
short_c = short_call(S, 100, 10)

plt.plot(S, P1)
plt.plot(S, long_c, "r--")
plt.plot(S, short_c, "b--")

plt.legend(["Bull Spread", "Long Call", "Short Call"])
plt.title("Bull Spread")

plt.subplot(323)
P = straddle(S, 100, 10, 10)
P_longcall = long_call(S, 100, 10)
P_longput = long_put(S, 100, 10)
plt.plot(S, P)
plt.plot(S, P_longcall, "r--")
plt.plot(S, P_longput, "b--")
plt.legend(["Straddle", "Long Call", "Long Put"])
plt.title("Straddle")

plt.subplot(324)
P = risk_reversal(S, 100, 75, 10, 10)
P_longcall = long_call(S, 100, 10)
P_shortput = short_put(S, 75, 10)
plt.plot(S, P, "g")
plt.plot(S, P_longcall, "b--")
plt.plot(S, P_shortput, "r--")
plt.legend(["Risk Reversal", "Long Call", "Short Put"])
plt.title("Risk-Reversal")

plt.subplot(325)
P = strangle(S, 100, 75, 10, 10)
P_longcall = long_call(S, 100, 10)
P_longput = long_put(S, 75, 10)
plt.plot(S, P, "g")
plt.plot(S, P_longcall, "b--")
plt.plot(S, P_longput, "r--")
plt.legend(["Strangle", "Long Short", "Long Put"])
plt.title("Strangle")

plt.subplot(326)
P_1 = long_call(S, 100, 10)
P_2 = long_put(S, 100, 10)
P_2 = [2 * p for p in P_2]
P = strip(S, 100, 10, 10)
plt.plot(S, P, "g")
plt.plot(S, P_1, "r--")
plt.plot(S, P_2, "b--")
plt.plot([100, 100], [-50, 50], "black")
plt.legend(["Strip", "Long Call", "Long Put"])
plt.annotate(
    "Strike Price",
    xy=(100, -50),
    xytext=(125, -30),
    arrowprops=dict(facecolor="black", shrink=0.01),
)
plt.title("Strip")

plt.show()
