import QuantLib as ql

# ------------------------------------------------------
# IR conversion - example 1
# ------------------------------------------------------
# If the annual IR is 5%, what is corresponding semiannual IR?

# input
annual_rate = 0.05  # Annual IR
day_count = ql.ActualActual()
compound_type = ql.Compounded  # <----------------- Compounded interest
frequency = ql.Annual

# ----------
interest_rate = ql.InterestRate(annual_rate, day_count, compound_type, frequency)
# ----------

# ------------------
# RESULT
# ------------------
t = 1  # year
new_frequency = ql.Semiannual
new_interest_rate = interest_rate.equivalentRate(compound_type, new_frequency, t)
print(new_interest_rate)
