import QuantLib as ql

# ------------------------------------------------------
# Discount factor - example 1
# ------------------------------------------------------
# Suppose the prevailing annually compounded interest rate for 5 year term is 4.5%.
# 1. What is the discount factor?
# 2. What is the discounted value of payment of 1000$ in 5 years?
# 3. What is the Future value in 5 years of a 15000$ investment today?


# input
annual_rate = 0.045  # Annual IR
day_count = ql.ActualActual()
compound_type = ql.Compounded  # <----------------- Continuous interest
frequency = ql.Annual

# ----------
interest_rate = ql.InterestRate(annual_rate, day_count, compound_type, frequency)
# ----------


# 1. discount factor
discounted_factor = interest_rate.discountFactor(1)
print(discounted_factor)

# 2. discounted value
discounted_value = 1000 / discounted_factor
print(discounted_value)

# 3. FV
FV = 15000 * interest_rate.compoundFactor(5)
print(FV)
