import QuantLib as ql

# ------------------------------------------------------
# Periodic Compounding interest - example 1
# ------------------------------------------------------
# Borrowing 15000$ for 6% semiannual IR for 5 years.


# input
annual_rate = 0.06  # Annual IR
day_count = ql.ActualActual()
compound_type = ql.Compounded  # <----------------- Compounded interest
frequency = ql.Semiannual

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
borrowing = 15000  # $

result = FV * borrowing
print(result)
