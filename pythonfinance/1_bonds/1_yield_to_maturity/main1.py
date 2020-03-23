import QuantLib as ql
import math

# Consider a 2 year bond with a 10 000$ face value, and 7% coupon,
# with semiannual payments. Suppose the current semiannual yield (to maturity)
# of the is 9%. What is the bond trading at?

# Construct yield curve
calc_date = ql.Date(1, 1, 2017)
ql.Settings.instance().evaluationDate = calc_date

spot_dates = [ql.Date(1, 1, 2017), ql.Date(1, 1, 2018), ql.Date(1, 1, 2027)]
spot_rates = [0.04, 0.04, 0.04]

day_count = ql.SimpleDayCounter()
calendar = ql.NullCalendar()
interpolation = ql.Linear()
compounding = ql.Compounded
compounding_frequency = ql.Semiannual
spot_curve = ql.ZeroCurve(
    spot_dates,
    spot_rates,
    day_count,
    calendar,
    interpolation,
    compounding,
    compounding_frequency,
)

spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)

# Construct bond schedule
issue_date = ql.Date(1, 1, 2017)
maturity_date = ql.Date(1, 1, 2022)
tenor = ql.Period(ql.Annual)
calendar = ql.NullCalendar()
business_convention = ql.Unadjusted
date_generation = ql.DateGeneration.Backward
month_end = False

schedule = ql.Schedule(
    issue_date,
    maturity_date,
    tenor,
    calendar,
    business_convention,
    business_convention,
    date_generation,
    month_end,
)

# Create FixedRateBond Object

coupon_rate = 0.05
coupons = [coupon_rate]
settlement_days = 0
face_value = 100

fixed_rate_bond = ql.FixedRateBond(
    settlement_days, face_value, schedule, coupons, day_count
)

# Set Valuation engine
bond_engine = ql.DiscountingBondEngine(spot_curve_handle)
fixed_rate_bond.setPricingEngine(bond_engine)

# Calculate present value
value = fixed_rate_bond.NPV()
print(value)


for i, c in enumerate(fixed_rate_bond.cashflows()):
    T = day_count.yearFraction(calc_date, c.date())

    # discount factor
    B = 1 / math.pow(1.02, 2 * T)

    # print(
    #     f"{0} {1} {2} {3} {4}",
    #     c.date(),
    #     c.amount(),
    #     T,
    #     B,
    #     spot_curve.discount(c.date()),
    # )

    print(
        "%20s %12f %12f %12f %12f"
        % (c.date(), c.amount(), T, B, spot_curve.discount(c.date()))
    )

