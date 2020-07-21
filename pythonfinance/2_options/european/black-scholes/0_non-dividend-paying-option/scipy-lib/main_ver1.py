import numpy as np
import scipy.stats as si

# ---------------------------------------------
# EURO CALL
# ---------------------------------------------
def euro_vanilla_call(S, K, T, r, sigma):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # sigma: volatility of underlying asset

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    call = S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(
        d2, 0.0, 1.0
    )

    return call


resultCall = euro_vanilla_call(100, 50, 1, 0.05, 0.25)
print(resultCall)

# ---------------------------------------------
# EURO PUT
# ---------------------------------------------
def euro_vanilla_put(S, K, T, r, sigma):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # sigma: volatility of underlying asset

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    put = K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(
        -d1, 0.0, 1.0
    )

    return put


resultPut = euro_vanilla_put(100, 50, 1, 0.05, 0.25)
print(resultPut)