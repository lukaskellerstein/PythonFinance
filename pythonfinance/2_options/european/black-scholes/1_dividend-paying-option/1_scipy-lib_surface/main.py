from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

from black_scholes import charm, delta, gamma, rho, theta, vega

# greek_function: input the function we want to calculate over


# x_var_name: 1st variable we vary
# y_var_name: 2nd variable we vary
# S: vector of underlying prices
# K: vector of strike prices
# r: vector of risk free rates
# vol: vector of volatilities
# T: vector of expiry
# t: vector of current date
# x: meshgrid of 1st variable we vary
# y: meshgrid of 2nd variable we vary
# otype: put/call
# plot: plot figure we want to write to
def greeks_plot_tool(
    greek_function,
    x_var_name,
    y_var_name,
    S,
    K,
    r,
    vol,
    T,
    t,
    x,
    y,
    otype,
    plot,
):

    # Initialise vector to store our option values and then iterate over
    # Assumption that we're using a constant sized vector length for each variable
    # Need to change the variables being iterated over here for each update (possibly a better way to do this)
    V = np.zeros((len(S), len(S)), dtype=np.float)
    for i in range(len(S)):
        for j in range(len(S)):
            V[i, j] = greek_function(
                S[i], K[i], r[i], vol[i], T[j], t[i], otype
            )

    # Initiliase plotting canvas
    surf = plot.plot_surface(
        x, y, V, rstride=1, cstride=1, alpha=0.75, cmap=cm.RdYlBu
    )
    plot.set_xlabel("\n" + x_var_name, linespacing=4)
    plot.set_ylabel("\n" + y_var_name, linespacing=4)
    plot.set_zlabel("%s(K, T)" % greek_function.__name__)
    plot.set_title("%s %s" % (otype, greek_function.__name__))

    # Calculate colour levels based on our meshgrid
    Vlevels = np.linspace(V.min(), V.max(), num=8, endpoint=True)
    xlevels = np.linspace(x.min(), x.max(), num=8, endpoint=True)
    ylevels = np.linspace(y.min(), y.max(), num=8, endpoint=True)

    cset = plot.contourf(
        x,
        y,
        V,
        Vlevels,
        zdir="z",
        offset=V.min(),
        cmap=cm.RdYlBu,
        linestyles="dashed",
    )
    cset = plot.contourf(
        x,
        y,
        V,
        xlevels,
        zdir="x",
        offset=x.min(),
        cmap=cm.RdYlBu,
        linestyles="dashed",
    )
    cset = plot.contourf(
        x,
        y,
        V,
        ylevels,
        zdir="y",
        offset=y.max(),
        cmap=cm.RdYlBu,
        linestyles="dashed",
    )

    # Set our viewing constraints
    for c in cset.collections:
        c.set_dashes([(0, (2.0, 2.0))])  # Dash contours
    plt.clabel(cset, fontsize=10, inline=1)
    plot.set_xlim(x.min(), x.max())
    plot.set_ylim(y.min(), y.max())
    plot.set_zlim(V.min(), V.max())

    # Colorbar
    colbar = plt.colorbar(surf, shrink=1.0, extend="both", aspect=10)
    l, b, w, h = plt.gca().get_position().bounds
    ll, bb, ww, hh = colbar.ax.get_position().bounds
    colbar.ax.set_position([ll, b + 0.1 * h, ww, h * 0.8])


S = np.linspace(70, 140, 40)
K = np.linspace(105.0, 105.0, 40)
T = np.linspace(0.1, 2.0, 40)
t = np.linspace(0.0, 0.0, 40)
r = np.linspace(0.0, 0.0, 40)
vol = np.linspace(0.12, 0.12, 40)

x, y = np.meshgrid(S, T)

fig = plt.figure(figsize=(30, 20))
fig.suptitle(
    "Greek Sensitivities to Stock Price and Expiry",
    fontsize=20,
    fontweight="bold",
)
greeks = [delta, gamma, vega, charm]

for i in range(len(greeks)):
    ax = fig.add_subplot(2, 2, i + 1, projection="3d")
    greeks_plot_tool(
        greeks[i],
        "Stock Price",
        "Expiry",
        S,
        K,
        r,
        vol,
        T,
        t,
        x,
        y,
        "call",
        ax,
    )

plt.show()
