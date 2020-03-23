import QuantLib as ql


amount = 105
date = ql.Date(15, 6, 2020)
cf = ql.SimpleCashFlow(amount, date)

print(cf.amount())
print(cf.date())
