import sympy as sy
from sympy.stats import Normal, cdf
from sympy import init_printing

# ---------------------------------------------
# EURO CALL
# ---------------------------------------------
def black_scholes_call_div_sym(S, K, T, r, q, sigma):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset
    # sigma: volatility of underlying asset

    N = Normal("x", 0.0, 1.0)

    d1 = (sy.ln(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))
    d2 = (sy.ln(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))

    call = S * sy.exp(-q * T) * cdf(N)(d1) - K * sy.exp(-r * T) * cdf(N)(d2)

    return call


resultCall = black_scholes_call_div_sym(100, 95, 1, 0.05, 0.3, 0.25)
print(resultCall)

# ---------------------------------------------
# EURO PUT
# ---------------------------------------------
def black_scholes_call_put_sym(S, K, T, r, q, sigma):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset
    # sigma: volatility of underlying asset

    N = Normal("x", 0.0, 1.0)

    d1 = (sy.ln(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))
    d2 = (sy.ln(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))

    put = K * sy.exp(-r * T) * cdf(N)(-d2) - S * sy.exp(-q * T) * cdf(N)(-d1)

    return put


resultPut = black_scholes_call_put_sym(100, 95, 1, 0.05, 0.3, 0.25)
print(resultPut)
