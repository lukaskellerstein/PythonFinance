import numpy as np
import scipy.stats as si

# ---------------------------------------------
# EURO CALL or PUT
# ---------------------------------------------
def euro_vanilla(S, K, T, r, sigma, option="call"):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # sigma: volatility of underlying asset

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if option == "call":
        result = S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(
            d2, 0.0, 1.0
        )
    if option == "put":
        result = K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(
            -d1, 0.0, 1.0
        )

    return result


resultCall = euro_vanilla(100, 50, 1, 0.05, 0.25, option="call")
print(resultCall)

resultPut = euro_vanilla(100, 50, 1, 0.05, 0.25, option="put")
print(resultPut)
