import numpy as np
import scipy.stats as si

# ---------------------------------------------
# EURO CALL
# ---------------------------------------------
def black_scholes_call_div(S, K, T, r, q, sigma):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset
    # sigma: volatility of underlying asset

    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    call = S * np.exp(-q * T) * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(
        -r * T
    ) * si.norm.cdf(d2, 0.0, 1.0)

    return call


resultCall = black_scholes_call_div(100, 95, 1, 0.05, 0.3, 0.25)
print(resultCall)

# ---------------------------------------------
# EURO PUT
# ---------------------------------------------
def black_scholes_put_div(S, K, T, r, q, sigma):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset
    # sigma: volatility of underlying asset

    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    put = K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * np.exp(
        -q * T
    ) * si.norm.cdf(-d1, 0.0, 1.0)

    return put


resultPut = black_scholes_put_div(100, 95, 1, 0.05, 0.3, 0.25)
print(resultPut)
