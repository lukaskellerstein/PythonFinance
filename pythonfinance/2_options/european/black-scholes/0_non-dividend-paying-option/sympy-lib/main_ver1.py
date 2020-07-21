import sympy as sy
from sympy.stats import Normal, cdf
from sympy import init_printing

# ---------------------------------------------
# EURO CALL
# ---------------------------------------------
def euro_call_sym(S, K, T, r, sigma):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # sigma: volatility of underlying asset

    N = Normal("x", 0.0, 1.0)

    d1 = (sy.ln(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))
    d2 = (sy.ln(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))

    call = S * cdf(N)(d1) - K * sy.exp(-r * T) * cdf(N)(d2)

    return call


resultCall = euro_call_sym(100, 50, 1, 0.05, 0.25)
print(resultCall)

# ---------------------------------------------
# EURO PUT
# ---------------------------------------------
def euro_put_sym(S, K, T, r, sigma):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # sigma: volatility of underlying asset

    N = Normal("x", 0.0, 1.0)

    d1 = (sy.ln(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))
    d2 = (sy.ln(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))

    put = K * sy.exp(-r * T) * cdf(N)(-d2) - S * cdf(N)(-d1)

    return put


resultPut = euro_put_sym(100, 50, 1, 0.05, 0.25)
print(resultPut)
