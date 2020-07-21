import QuantLib as ql
import matplotlib.pyplot as plt

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
# contruction
# ----------------------------------------
payoff = ql.PlainVanillaPayoff(option_type, strike_price)

# construct the European Option
exercise = ql.EuropeanExercise(maturity_date)
european_option = ql.VanillaOption(payoff, exercise)


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
# Computation - ver. 1 - AnalyticEuropeanEngine
# -----------------------------------------------
# -----------------------------------------------
pricing_engine = ql.AnalyticEuropeanEngine(bsm_process)
european_option.setPricingEngine(pricing_engine)
bs_price = european_option.NPV()
print("AnalyticEuropeanEngine pricing engine - The theoretical price is ", bs_price)


# ------------------------------------------------
# -----------------------------------------------
# Computation - ver. 2 - Binomial-tree
# -----------------------------------------------
# -----------------------------------------------
steps = 200
pricing_engine = ql.BinomialVanillaEngine(bsm_process, "crr", steps)
european_option.setPricingEngine(pricing_engine)
print("Binomial-tree pricing engine - The theoretical price is ", european_option.NPV())


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
prices = [binomial_price(european_option, bsm_process, step) for step in steps]


# -----------------------------------------------
# PLOT
# -----------------------------------------------
plt.plot(steps, prices, label="Binomial Tree Price", lw=2, alpha=0.6)
plt.plot([0, 100], [bs_price, bs_price], "r--", label="BSM Price", lw=2, alpha=0.6)
plt.xlabel("Steps")
plt.ylabel("Price")
plt.title("Binomial Tree Price For Varying Steps")
plt.legend()

plt.show()
