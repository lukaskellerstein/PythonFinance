
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm

from black_scholes import charm, delta, gamma, rho, theta, vega

###########################################################################
# PLOT


# -------------------------------------------------------------------------
# Sensitivity on == Strike Price vs. Stock Price ==
# -------------------------------------------------------------------------

fig, ax = plt.subplots(nrows=3, ncols=2, sharex=True, sharey=True, figsize=(40, 30))
fig.suptitle('Sensitivity of 1st Order European Option Greeks to Strike + Underlying', fontsize=20, fontweight='bold')
fig.text(0.5, 0.08, 'Stock/Underlying Price ($)', ha='center', fontsize=18, fontweight='bold')
vals = [15,25,35]

r = 0.01
vol = 0.1
T = 10
t = 0
plt.subplot(321)
for i in vals:
    tmp_c = [delta(s, i, r, vol, T, t, "call") for s in np.arange(1, 100)]
    tmp_p = [delta(s, i, r, vol, T, t, "put") for s in np.arange(1, 100)]
    plt.plot(tmp_c, label=(f"Delta Call K={i}"))
    plt.plot(tmp_p, label=(f"Delta Put K={i}"))

plt.ylabel("Delta")
plt.legend()

plt.subplot(322)
for i in vals:
    tmp_c = [gamma(s, i, r, vol, T, t, "call") for s in np.arange(1, 100)]
    tmp_p = [gamma(s, i, r, vol, T, t, "put") for s in np.arange(1, 100)]
    plt.plot(tmp_c, label=(f"Gamma Call K={i}"))
    plt.plot(tmp_p, label=(f"Gamma Put K={i}"))

plt.ylabel("Gamma")
plt.legend()

plt.subplot(323)
for i in vals:
    tmp_c = [vega(s, i, r, vol, T, t, "call") for s in np.arange(1, 100)]
    tmp_p = [vega(s, i, r, vol, T, t, "put") for s in np.arange(1, 100)]
    plt.plot(tmp_c, label=(f"Vega Call K={i}"))
    plt.plot(tmp_p, label=(f"Vega Put K={i}"))

plt.ylabel("Vega")
plt.legend()

plt.subplot(324)

for i in vals:
    tmp_c = [rho(s, i, r, vol, T, t, "call") for s in np.arange(1, 100)]
    tmp_p = [rho(s, i, r, vol, T, t, "put") for s in np.arange(1, 100)]
    plt.plot(tmp_c, label=(f"Rho Call K={i}"))
    plt.plot(tmp_p, label=(f"Rho Put K={i}"))

plt.ylabel("Rho")
plt.legend()

plt.subplot(325)
for i in vals:
    tmp_c = [theta(s, i, r, vol, T, t, "call") for s in np.arange(1, 100)]
    tmp_p = [theta(s, i, r, vol, T, t, "put") for s in np.arange(1, 100)]
    plt.plot(tmp_c, label=(f"Theta Call K={i}"))
    plt.plot(tmp_p, label=(f"Theta Put K={i}"))

plt.ylabel("Theta")
plt.legend()

plt.subplot(326)
for i in vals:
    tmp_c = [charm(s, i, r, vol, T, t, "call") for s in np.arange(1, 100)]
    tmp_p = [charm(s, i, r, vol, T, t, "put") for s in np.arange(1, 100)]
    plt.plot(tmp_c, label=(f"Charm Call K={i}"))
    plt.plot(tmp_p, label=(f"Charm Put K={i}"))

plt.ylabel("Charm")
plt.legend()
plt.show()
