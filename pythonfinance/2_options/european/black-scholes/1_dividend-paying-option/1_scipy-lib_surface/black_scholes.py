import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


###########################################################################
# BLACK-SCHOLES model

# S: underlying stock price
# K: Option strike price
# r: risk free rate
# D: dividend value
# vol: Volatility
# T: time to expiry (assumed that we're measuring from t=0 to T)
def d1_calc(S, K, r, vol, T, t):
    # Calculates d1 in the BSM equation
    return (np.log(S / K) + (r + 0.5 * vol ** 2) * (T - t)) / (vol * np.sqrt(T - t))


def BS_call(S, K, r, vol, T, t):
    d1 = d1_calc(S, K, r, vol, T, t)
    d2 = d1 - vol * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def BS_put(S, K, r, vol, T, t):
    return BS_call(S, K, r, vol, T, t) - S + np.exp(-r * (T - t)) * K


###########################################################################
# 1st Order Greeks


def delta(S, K, r, vol, T, t, otype):
    d1 = d1_calc(S, K, r, vol, T, t)
    d2 = d1 - vol * np.sqrt(T - t)

    if otype == "call":
        delta = np.exp(-(T - t)) * norm.cdf(d1)
    elif otype == "put":
        delta = -np.exp(-(T - t)) * norm.cdf(-d1)

    return delta


# Gamma for calls/puts the same
def vega(S, K, r, vol, T, t, otype):
    d1 = d1_calc(S, K, r, vol, T, t)
    return S * norm.pdf(d1) * np.sqrt(T - t)


def rho(S, K, r, vol, T, t, otype):
    d1 = d1_calc(S, K, r, vol, T, t)
    d2 = d1 - vol * np.sqrt(T - t)

    if otype == "call":
        rho = K * (T - t) * np.exp(-r * (T - t)) * norm.cdf(d2)
    elif otype == "put":
        rho = -K * (T - t) * np.exp(-r * (T - t)) * norm.cdf(-d2)
    return rho


def theta(S, K, r, vol, T, t, otype):
    d1 = d1_calc(S, K, r, vol, T, t)
    d2 = d1 - vol * np.sqrt(T - t)

    if otype == "call":
        theta = -(S * norm.pdf(d1) * vol / (2 * np.sqrt(T - t))) - r * K * np.exp(
            -r * (T - t)
        ) * norm.cdf(d2)
    elif otype == "put":
        theta = -(S * norm.pdf(d1) * vol / (2 * np.sqrt(T - t))) + r * K * np.exp(
            -r * (T - t)
        ) * norm.cdf(-d2)

    return theta


###########################################################################
# 2nd Order Greeks


def gamma(S, K, r, vol, T, t, otype):
    d1 = d1_calc(S, K, r, vol, T, t)
    gamma = (norm.pdf(d1)) / (S * vol * np.sqrt(T - t))

    return gamma


def charm(S, K, r, vol, T, t, otype):
    d1 = d1_calc(S, K, r, vol, T, t)
    d2 = d1 - vol * np.sqrt(T - t)
    charm = (
        -norm.pdf(d1)
        * (2 * r * (T - t) - d2 * vol * np.sqrt(T - t))
        / (2 * (T - t) * vol * np.sqrt(T - t))
    )

    return charm
