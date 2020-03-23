import QuantLib as ql

# ---------------------------------------------------------------------------------
# A bond with a 5% coupon (annual),
# with semiannual payments,
# a 10 000 $ face value,
# and maturing in 1 year
#
# Current Price on the market = 10 124 $
# ---------------------------------------------------------------------------------

time1 = 0.5
time2 = 1
price = 10124
face_value = 10000

# coupon rate
annual_coupon_rate = 10000

# we calculate discount factor
d05 = 10124 / 10000
print(d05)
