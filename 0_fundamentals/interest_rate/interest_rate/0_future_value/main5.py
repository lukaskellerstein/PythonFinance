import QuantLib as ql

# ------------------------------------------------------
# Continuous Compounding interest - example 1
# ------------------------------------------------------
# Borrowing 20 000 $ with continuous IR 3.5% for 18 months (1.5 years).

# input
annual_rate = 0.035  # Annual IR
day_count = ql.ActualActual()
compound_type = ql.Continuous  # <----------------- Continuous interest
frequency = ql.Annual

# ----------
interest_rate = ql.InterestRate(annual_rate, day_count, compound_type, frequency)
# ----------

# Future value
how_long = 1.5  # years
FV = interest_rate.compoundFactor(how_long)
print(FV)

# ------------------
# RESULT
# ------------------
borrowing = 20000  # $

result = FV * borrowing
print(result)
