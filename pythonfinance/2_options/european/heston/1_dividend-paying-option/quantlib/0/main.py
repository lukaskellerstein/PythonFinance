import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps, cumtrapz, romb
import math


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
# The Heston process is constructed here.
#
# The Heston process calculates with changing volatility during the trade
# -----------------------------------------------------------
v0 = volatility * volatility  # spot variance
kappa = 0.1
theta = v0
sigma = 0.1
rho = -0.75

spot_handle = ql.QuoteHandle(ql.SimpleQuote(spot_price))
flat_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, risk_free_rate, day_count)
)
dividend_yield = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, dividend_rate, day_count)
)
heston_process = ql.HestonProcess(
    flat_ts, dividend_yield, spot_handle, v0, kappa, theta, sigma, rho
)


# ------------------------------------------------
# -----------------------------------------------
# Computation - ver. 3 - Heston
# -----------------------------------------------
# -----------------------------------------------
pricing_engine = ql.AnalyticHestonEngine(ql.HestonModel(heston_process), 0.01, 1000)
european_option.setPricingEngine(pricing_engine)
h_price = european_option.NPV()
print("The Heston model price is ", h_price)

