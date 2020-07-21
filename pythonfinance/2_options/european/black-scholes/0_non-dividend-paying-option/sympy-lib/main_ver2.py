import sympy as sy
from sympy.stats import Normal, cdf
from sympy import init_printing

# ---------------------------------------------
# EURO CALL or PUT
# ---------------------------------------------
def sym_euro_vanilla(S, K, T, r, sigma, option="call"):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # sigma: volatility of underlying asset

    N = Normal("x", 0.0, 1.0)

    d1 = (sy.ln(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))
    d2 = (sy.ln(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))

    if option == "call":
        result = S * cdf(N)(d1) - K * sy.exp(-r * T) * cdf(N)(d2)
    if option == "put":
        result = K * sy.exp(-r * T) * cdf(N)(-d2) - S * cdf(N)(-d1)

    return result


resultCall = sym_euro_vanilla(100, 50, 1, 0.05, 0.25, option="call")
print(resultCall)

resultPut = sym_euro_vanilla(100, 50, 1, 0.05, 0.25, option="put")
print(resultPut)
