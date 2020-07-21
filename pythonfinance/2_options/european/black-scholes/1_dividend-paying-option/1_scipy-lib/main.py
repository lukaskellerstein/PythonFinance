import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

from black_scholes import BS_call, BS_put

###########################################################################
# PLOT

S = np.arange(0, 30)
vals_call = [BS_call(x, 50, 0.10, 0.2, 10, 0) for x in S]
vals_put = [BS_put(x, 50, 0.10, 0.2, 10, 0) for x in S]
plt.plot(S, vals_call, "r", label="Call")
plt.plot(S, vals_put, "b", label="Put")
plt.legend()
plt.ylabel("Stock Price ($)")
plt.xlabel("Option Price ($)")
plt.show()
