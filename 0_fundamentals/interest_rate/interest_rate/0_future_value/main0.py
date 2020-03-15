import QuantLib as ql


# ------------------------------------------------------
# Simple interest - example 1
# ------------------------------------------------------
# Borrowing 100$ for 5 years with Annual IR = 10%. What will be a Future value?


# input
annual_rate = 0.10  # Annual IR
day_count = ql.ActualActual()
compound_type = ql.Simple  # <----------------- Simple compounding
frequency = ql.Annual

# ----------
interest_rate = ql.InterestRate(annual_rate, day_count, compound_type, frequency)
# ----------

# Future value
how_long = 5  # years
FV = interest_rate.compoundFactor(how_long)
print(FV)

# ------------------
# RESULT
# ------------------
borrowing = 100  # $
result = borrowing * FV
print(result)

