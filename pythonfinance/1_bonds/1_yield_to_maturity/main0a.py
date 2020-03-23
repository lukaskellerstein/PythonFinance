import QuantLib as ql
import math

# ---------------------------------------------------------------------------------
# A zero coupon bond with
# a 1000$ face value
# maturing in 6 months = 0.5 year
#
# Current Price on the market = 985 $
# ---------------------------------------------------------------------------------

time1 = 0.5
price = 985
face_value = 1000

# we calculate discount factor
d05 = 985 / 1000
print(d05)

# we calculate yield
y05 = -(math.log(d05) / time1)
y05_percent = y05 * 100


print(y05)
print(y05_percent)
