import QuantLib as ql

# ---------------------------------------------------------------------------------
# A zero coupon bond with
# a 1000$ face value
# maturing in 6 months = 0.5 year
#
# Current Price on the market = 985 $
# ---------------------------------------------------------------------------------

settlementDays = 0

bond = ql.ZeroCouponBond(settlementDays, ql.TARGET(), 1000, ql.Date(20, 6, 2020))

