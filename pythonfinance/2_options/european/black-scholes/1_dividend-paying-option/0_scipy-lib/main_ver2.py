import numpy as np
import scipy.stats as si

# ---------------------------------------------
# EURO CALL or PUT
# ---------------------------------------------
def euro_vanilla_dividend(S, K, T, r, q, sigma, option="call"):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset
    # sigma: volatility of underlying asset

    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if option == "call":
        result = S * np.exp(-q * T) * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(
            -r * T
        ) * si.norm.cdf(d2, 0.0, 1.0)
    if option == "put":
        result = K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * np.exp(
            -q * T
        ) * si.norm.cdf(-d1, 0.0, 1.0)

    return result


resultCall = euro_vanilla_dividend(100, 95, 1, 0.05, 0.25, 0.3, option="call")
print(resultCall)

resultPut = euro_vanilla_dividend(100, 95, 1, 0.05, 0.25, 0.3, option="put")
print(resultPut)
