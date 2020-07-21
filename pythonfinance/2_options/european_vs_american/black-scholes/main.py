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
eu_exercise = ql.EuropeanExercise(maturity_date)
european_option = ql.VanillaOption(payoff, eu_exercise)

# construct the American Option
am_exercise = ql.AmericanExercise(calculation_date, maturity_date)
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

# european
european_option.setPricingEngine(pricing_engine)
print("The theoretical price is ", european_option.NPV())

# american
american_option.setPricingEngine(pricing_engine)
print("The theoretical price is ", american_option.NPV())


# ------------------------------------------------
# -----------------------------------------------
# PLOT COMPARISON
# -----------------------------------------------
# -----------------------------------------------
def binomial_price(option, bsm_process, steps):
    binomial_engine = ql.BinomialVanillaEngine(bsm_process, "crr", steps)
    option.setPricingEngine(binomial_engine)
    return option.NPV()


steps = range(5, 200, 1)
eu_prices = [binomial_price(european_option, bsm_process, step) for step in steps]
am_prices = [binomial_price(american_option, bsm_process, step) for step in steps]
# theoretican European option price
european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
bs_price = european_option.NPV()


# -----------------------------------------------
# PLOT
# -----------------------------------------------
plt.plot(steps, eu_prices, label="European Option", lw=2, alpha=0.6)
plt.plot(steps, am_prices, label="American Option", lw=2, alpha=0.6)
plt.plot([5, 200], [bs_price, bs_price], "r--", label="BSM Price", lw=2, alpha=0.6)
plt.xlabel("Steps")
plt.ylabel("Price")
# plt.ylim(6.7, 7)
plt.title("Binomial Tree Price For Varying Steps")
plt.legend()

plt.show()
