import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm

from black_scholes import charm, delta, gamma, rho, theta, vega

###########################################################################
# PLOT


# -------------------------------------------------------------------------
# Sensitivity on == Risk-Free rate vs. Stock Price ==
# -------------------------------------------------------------------------
fig, ax = plt.subplots(
    nrows=3, ncols=2, sharex=True, sharey=True, figsize=(30, 20)
)
fig.suptitle(
    "Sensitivity of 1st Order European Option Greeks to Risk-Free Rate + Underlying",
    fontsize=20,
    fontweight="bold",
)
fig.text(
    0.5,
    0.08,
    "Stock/Underlying Price ($)",
    ha="center",
    fontsize=18,
    fontweight="bold",
)

vals = [0, 0.01, 0.1]
K = 15
r = 0.01
vol = 0.1
T = 10
t = 0
plt.subplot(321)
for i in vals:
    tmp_c = [delta(s, K, i, vol, T, t, "call") for s in np.arange(1, 100)]
    tmp_p = [delta(s, K, i, vol, T, t, "put") for s in np.arange(1, 100)]
    plt.plot(tmp_c, label=("Delta Call r=%.2f" % i))
    plt.plot(tmp_p, label=("Delta Put r=%.2f" % i))

plt.ylabel("Delta")
plt.legend()

plt.subplot(322)
for i in vals:
    tmp_c = [gamma(s, K, i, vol, T, t, "call") for s in np.arange(1, 100)]
    tmp_p = [gamma(s, K, i, vol, T, t, "put") for s in np.arange(1, 100)]
    plt.plot(tmp_c, label=("Gamma Call r=%.2f" % i))
    plt.plot(tmp_p, label=("Gamma Put r=%.2f" % i))

plt.ylabel("Gamma")
plt.legend()

plt.subplot(323)
for i in vals:
    tmp_c = [vega(s, K, i, vol, T, t, "call") for s in np.arange(1, 100)]
    tmp_p = [vega(s, K, i, vol, T, t, "put") for s in np.arange(1, 100)]
    plt.plot(tmp_c, label=("Vega Call r=%.2f" % i))
    plt.plot(tmp_p, label=("Vega Put r=%.2f" % i))

plt.ylabel("Vega")
plt.legend()

plt.subplot(324)

for i in vals:
    tmp_c = [rho(s, K, i, vol, T, t, "call") for s in np.arange(1, 100)]
    tmp_p = [rho(s, K, i, vol, T, t, "put") for s in np.arange(1, 100)]
    plt.plot(tmp_c, label=("Rho Call r=%.2f" % i))
    plt.plot(tmp_p, label=("Rho Put r=%.2f" % i))

plt.ylabel("Rho")
plt.legend()

plt.subplot(325)
for i in vals:
    tmp_c = [theta(s, K, i, vol, T, t, "call") for s in np.arange(1, 100)]
    tmp_p = [theta(s, K, i, vol, T, t, "put") for s in np.arange(1, 100)]
    plt.plot(tmp_c, label=("Theta Call r=%.2f" % i))
    plt.plot(tmp_p, label=("Theta Put r=%.2f" % i))

plt.ylabel("Theta")
plt.legend()

plt.subplot(326)
for i in vals:
    tmp_c = [charm(s, K, i, vol, T, t, "call") for s in np.arange(1, 100)]
    tmp_p = [charm(s, K, i, vol, T, t, "put") for s in np.arange(1, 100)]
    plt.plot(tmp_c, label=("Charm Call r=%.2f" % i))
    plt.plot(tmp_p, label=("Charm Put r=%.2f" % i))

plt.ylabel("Charm")
plt.legend()
plt.show()
