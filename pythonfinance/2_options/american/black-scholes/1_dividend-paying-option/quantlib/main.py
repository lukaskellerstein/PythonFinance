import QuantLib as ql
import matplotlib.pyplot as plt
from timeit import default_timer as timer

start = timer()

# -----------------------------------------
# inputs
# -----------------------------------------
maturity_date = ql.Date(15, 1, 2016)
spot_price = 100
strike_price = 95
volatility = 0.3  # the historical or implied vols for a year
dividend_rate = 0.25
option_type = ql.Option.Call

risk_free_rate = 0.05
day_count = ql.Actual365Fixed()
calendar = ql.UnitedStates()

calculation_date = ql.Date(15, 1, 2015)
ql.Settings.instance().evaluationDate = calculation_date


# ----------------------------------------
# contruction of the Option
# ----------------------------------------
payoff = ql.PlainVanillaPayoff(option_type, strike_price)
settlement = calculation_date

# construct the American Option
am_exercise = ql.AmericanExercise(settlement, maturity_date)
american_option = ql.VanillaOption(payoff, am_exercise)

# -----------------------------------------------------------
# The Black-Scholes-Merton process is constructed here.
#
# The Black-Scholes-Merton process assumes that the volatility is constant !!!!
# -----------------------------------------------------------
spot_handle = ql.QuoteHandle(ql.SimpleQuote(spot_price))
flat_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, risk_free_rate, day_count)
)
dividend_yield = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, dividend_rate, day_count)
)
flat_vol_ts = ql.BlackVolTermStructureHandle(
    ql.BlackConstantVol(calculation_date, calendar, volatility, day_count)
)
bsm_process = ql.BlackScholesMertonProcess(
    spot_handle, dividend_yield, flat_ts, flat_vol_ts
)


# ------------------------------------------------
# -----------------------------------------------
# Computation - ver. 2 - Binomial-tree
# -----------------------------------------------
# -----------------------------------------------
steps = 200
pricing_engine = ql.BinomialVanillaEngine(bsm_process, "crr", steps)
american_option.setPricingEngine(pricing_engine)

option_price = american_option.NPV()
# option_iv = american_option.impliedVolatility()

option_payoff = american_option.payoff()

# option_price_curve = american_option.priceCurve()

a = american_option.Put
b = american_option.Call

print(option_price)
# print(option_iv)
print(option_payoff)
# print(option_price_curve)
print(a)
print(b)


# greeks
option_delta = american_option.delta()
option_gamma = american_option.gamma()
option_theta = american_option.theta()
# option_vega = american_option.vega()
# option_ro = american_option.rho()

# option_thetaPerDay = american_option.thetaPerDay()


print(option_delta)
print(option_gamma)
print(option_theta)
# print(option_vega)
# print(option_ro)
# print(option_thetaPerDay)

print("Binomial-tree pricing engine - The theoretical price is ", american_option.NPV())


# end timer
end = timer()
# print(option_ro)
# print(option_thetaPerDay)
print(f"Result in = {end - start} sec.")


# ------------------------------------------------
# -----------------------------------------------
# PLOT COMPARISON
# -----------------------------------------------
# -----------------------------------------------
def binomial_price(option, bsm_process, steps):
    binomial_engine = ql.BinomialVanillaEngine(bsm_process, "crr", steps)
    option.setPricingEngine(binomial_engine)
    return option.NPV()


steps = range(2, 100, 1)
prices = [binomial_price(american_option, bsm_process, step) for step in steps]


# -----------------------------------------------
# PLOT
# -----------------------------------------------
plt.plot(steps, prices, label="Binomial Tree Price", lw=2, alpha=0.6)
plt.xlabel("Steps")
plt.ylabel("Price")
plt.title("Binomial Tree Price For Varying Steps")
plt.legend()

plt.show()
