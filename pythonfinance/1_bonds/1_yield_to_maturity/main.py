import QuantLib as ql

# Consider a 2 year bond with a 10 000$ face value, and 7% coupon,
# with semiannual payments. Suppose the current semiannual yield (to maturity)
# of the is 9%. What is the bond trading at?

start_date = ql.Date(15, 1, 2021)
end_date = ql.Date(15, 1, 2023)
face_value = 10000
coupon_rate = 0.07


todaysDate = start_date
ql.Settings.instance().evaluationDate = todaysDate
# spotDates = [ql.Date(15, 1, 2015), ql.Date(15, 7, 2015), ql.Date(15, 1, 2016), ql.Date(15, 7, 2016), ql.Date(15, 1, 2017)]
# semiannual spot-dates
# spotDates = [
#     start_date + ql.Period(i * 6, ql.Months) for i in range(0, 4)
# ]  # <---- 4 = 2 years and semiannual
# spotRates = [0.0, 0.005, 0.007]
# spotRates = [coupon_rate for i in range(0, 4)]

spotDates = [
    ql.Date(15, 1, 2021),
    ql.Date(15, 7, 2021),
    ql.Date(15, 1, 2022),
    ql.Date(15, 7, 2022),
    ql.Date(15, 1, 2023),
]
spotRates = [coupon_rate, coupon_rate, coupon_rate, coupon_rate, coupon_rate]

dayCount = ql.Thirty360()
calendar = ql.UnitedStates()
interpolation = ql.Linear()
compounding = ql.Compounded
compoundingFrequency = ql.Semiannual
spotCurve = ql.ZeroCurve(
    spotDates,
    spotRates,
    dayCount,
    calendar,
    interpolation,
    compounding,
    compoundingFrequency,
)
spotCurveHandle = ql.YieldTermStructureHandle(spotCurve)


issueDate = start_date
maturityDate = end_date
tenor = ql.Period(ql.Semiannual)
calendar = ql.UnitedStates()
bussinessConvention = ql.Unadjusted
dateGeneration = ql.DateGeneration.Backward
monthEnd = False
schedule = ql.Schedule(
    issueDate,
    maturityDate,
    tenor,
    calendar,
    bussinessConvention,
    bussinessConvention,
    dateGeneration,
    monthEnd,
)
print(list(schedule))


# Now lets build the coupon
dayCount = ql.Thirty360()
couponRate = coupon_rate
coupons = [couponRate]

# Now lets construct the FixedRateBond
settlementDays = 0
faceValue = face_value
fixedRateBond = ql.FixedRateBond(settlementDays, faceValue, schedule, coupons, dayCount)


# create a bond engine with the term structure as input;
# set the bond to use this bond engine
bondEngine = ql.DiscountingBondEngine(spotCurveHandle)
fixedRateBond.setPricingEngine(bondEngine)

# Calculate present value
value = fixedRateBond.NPV()
print(value)
