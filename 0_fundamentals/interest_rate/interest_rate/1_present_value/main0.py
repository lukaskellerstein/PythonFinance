import QuantLib as ql

# ------------------------------------------------------
# Periodic Compounding interest - example 1
# ------------------------------------------------------
# Calculate the present value of a 15 000$ payment
# recieved in 8 years using a semiannual compounding rate of 6%.

# input
annual_rate = 0.06  # Annual IR
day_count = ql.ActualActual()
compound_type = ql.Compounded  # <----------------- Continuous interest
frequency = ql.Semiannual

# ----------
interest_rate = ql.InterestRate(annual_rate, day_count, compound_type, frequency)
# ----------

# Present value
how_long = 8  # years
PV = interest_rate.compoundFactor(how_long)
print(PV)

# ------------------
# RESULT
# ------------------
borrowing = 15000  # $

result = borrowing / PV
print(result)
