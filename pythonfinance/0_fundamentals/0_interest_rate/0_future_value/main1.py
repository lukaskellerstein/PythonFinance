import QuantLib as ql


# ------------------------------------------------------
# Compounding interest - example 1
# ------------------------------------------------------
# Borrowing 5000$ for 7% Annual IR for 10 years. What will be a Future value?


# IR
annual_rate = 0.07  # Annual IR
day_count = ql.ActualActual()
compound_type = ql.Compounded  # <----------------- Compounded interest
frequency = ql.Annual

# ----------
interest_rate = ql.InterestRate(annual_rate, day_count, compound_type, frequency)
# ----------

# Future value
how_long = 10  # years
FV = interest_rate.compoundFactor(how_long)
print(FV)


# ------------------
# RESULT
# ------------------
borrowing = 5000  # $

result = borrowing * FV
print(result)

