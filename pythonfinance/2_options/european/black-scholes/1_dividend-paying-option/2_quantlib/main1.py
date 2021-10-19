import QuantLib as ql
import matplotlib.pyplot as plt
import datetime
import time

# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# inputs - 1
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
calculation_date = ql.Date(15, 1, 2015)
spot_price = 100
volatility = 0.3  # the historical or implied vols for a year
dividend_rate = 0.25
risk_free_rate = 0.05
day_count = ql.Actual365Fixed()
calendar = ql.UnitedStates()

ql.Settings.instance().evaluationDate = calculation_date

# -----------------------------------------------------------
# The Black-Scholes-Merton process is constructed here.
#
# The Black-Scholes-Merton process assumes that the volatility is constant !!!!
# -----------------------------------------------------------
flat_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, risk_free_rate, day_count)
)
dividend_yield = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, dividend_rate, day_count)
)
flat_vol_ts = ql.BlackVolTermStructureHandle(
    ql.BlackConstantVol(calculation_date, calendar, volatility, day_count)
)

spot_price_quote = ql.SimpleQuote(spot_price)
spot_handle = ql.QuoteHandle(spot_price_quote)
bsm_process = ql.BlackScholesMertonProcess(
    spot_handle, dividend_yield, flat_ts, flat_vol_ts
)

pricing_engine = ql.AnalyticEuropeanEngine(bsm_process)


# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# inputs - 2
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
option_type = ql.Option.Call
strike_price = 95
maturity_date = ql.Date(15, 3, 2015)

# ----------------------------------------
# contruction
# ----------------------------------------
payoff = ql.PlainVanillaPayoff(option_type, strike_price)
exercise = ql.EuropeanExercise(maturity_date)
european_option = ql.VanillaOption(payoff, exercise)
european_option.setPricingEngine(pricing_engine)


# ----------------------------------------
# ????
# ----------------------------------------
start_timer = time.time()
spotPrices = range(1, 200)
optionPrices = []
for spotPrice in spotPrices:
    spot_price_quote.setValue(spotPrice)

    optionPrices.append(european_option.NPV())

    # print(
    #     "AnalyticEuropeanEngine pricing engine - The theoretical price is ",
    #     european_option.NPV(),
    # )
    # print("Delta", european_option.delta())
    # print("Gamma", european_option.gamma())
    # print("Theta", european_option.theta())
    # print("Vega", european_option.vega())

end_timer = time.time()
print((end_timer - start_timer) * 1000)

optionPrice = optionPrices[95]  # 95 strike price = index
print(
    "The option price is ",
    european_option.NPV(),
    " for strike price: ",
    strike_price,
    ", expiration in 1 year",
)


# ----------------------------------------
# MY ????
# ----------------------------------------
start_timer = time.time()
strikePrices = range(1, 200)
optionPrices2 = []
print("Current stock price: ", spot_price)
for strkPrice in strikePrices:
    payoff4 = ql.PlainVanillaPayoff(option_type, strkPrice)
    exercise4 = ql.EuropeanExercise(maturity_date)
    my_option = ql.VanillaOption(payoff4, exercise4)
    my_option.setPricingEngine(pricing_engine)

    print(
        "Strike price: ",
        strkPrice,
        " options price: ",
        my_option.NPV(),
        " Delta: ",
        my_option.delta(),
        " Gamma: ",
        my_option.gamma(),
        " Theta: ",
        my_option.theta(),
        " Vega: ",
        my_option.vega(),
    )
    optionPrices2.append(my_option.NPV())

end_timer = time.time()
print((end_timer - start_timer) * 1000)
# ----------------------------------------
# PLOT 1
# ----------------------------------------
plt.plot(spotPrices, optionPrices, label="Payoff", lw=2, alpha=0.6)
plt.xlabel("spotPrices")
plt.ylabel("optionPrices")
plt.title("Option Payoff")
plt.legend()

plt.show()

# -----------------------------------------------
# PLOT 2
# -----------------------------------------------
# LONG CALL


# S = stock underlying
# K = strike price
# Price = premium paid for option
def long_call(S, K, Price):
    # Long Call Payoff = max(Stock Price - Strike Price, 0)

    # If we are long a call, we would only elect to call if the current stock price is greater than
    # the strike price on our option
    P = list(map(lambda x: max(x - K, 0) - Price, S))
    return P


def long_call_turning_point(K, Price):
    return K + Price


optionPrices = long_call(spotPrices, strike_price, optionPrice)  # option price
turning_point = long_call_turning_point(strike_price, optionPrice)

# axes
plt.grid(True, which="both")
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")

# plot
plt.plot(spotPrices, optionPrices)
plt.scatter(turning_point, 0)
plt.annotate(
    f"({turning_point},0)",  # this is the text
    (turning_point, 0),  # this is the point to label
    textcoords="offset points",  # how to position the text
    xytext=(0, 10),  # distance from text to points (x,y)
    ha="center",
)

plt.show()
