#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   graphics_methods.py
@Time    :   2024/08/27 14:37:24
@Author  :   Roney D. Silva
@Contact :   roneyddasilva@gmail.com
"""
import warnings

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

import matplotlib.colors as mc
plt.style.use("./common_functions/roney3.mplstyle")
my_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

# Crie o colormap personalizado
my_custom_colormap = LinearSegmentedColormap.from_list(
    "my_colormap", [my_colors[0], my_colors[1], my_colors[3]]
)


meter_per_second_squared = "\\unit{\\meter\\per\\second\\squared}"
time_in_second = "\\unit{\\second}"
time_in_hour = "\\unit{\\hour}"


def set_xlabel_time(_ax: plt.axes, unit: str):
    if unit == "second":
        _ax.set_xlabel(r"Tempo $[\unit{\second}]$")
    elif unit == "millisecond":
        _ax.set_xlabel(r"Tempo $[\unit{\mili\second}]$")
    elif unit == "hour":
        _ax.set_xlabel(r"Tempo $[\unit{\hour}]$")


def set_ylabel_loop(_ax: plt.axes, names=["x", "y", "z"], unit=""):
    for i in range(len(names)):
        if unit != "":
            _unit = "[" + unit + "]"
        _ax[i].set_ylabel(names[i] + unit)


def colored_line(x, y, c, ax, **lc_kwargs):
    """
    Plot a line with a color specified along the line by a third value.

    It does this by creating a collection of line segments. Each line segment is
    made up of two straight lines each connecting the current (x, y) point to the
    midpoints of the lines connecting the current point with its two neighbors.
    This creates a smooth line with no gaps between the line segments.

    Parameters
    ----------
    x, y : array-like
        The horizontal and vertical coordinates of the data points.
    c : array-like
        The color values, which should be the same size as x and y.
    ax : Axes
        Axis object on which to plot the colored line.
    **lc_kwargs
        Any additional arguments to pass to matplotlib.collections.LineCollection
        constructor. This should not include the array keyword argument because
        that is set to the color argument. If provided, it will be overridden.

    Returns
    -------
    matplotlib.collections.LineCollection
        The generated line collection representing the colored line.
        copy from: https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html#sphx-glr-gallery-lines-bars-and-markers-multicolored-line-py
    """
    if "array" in lc_kwargs:
        warnings.warn('The provided "array" keyword argument will be overridden')
    if "cmap" not in lc_kwargs:
        lc_kwargs['cmap'] = my_custom_colormap
    # Default the capstyle to butt so that the line segments smoothly line up
    default_kwargs = {"capstyle": "butt"}
    default_kwargs.update(lc_kwargs)

    # Compute the midpoints of the line segments. Include the first and last points
    # twice so we don't need any special syntax later to handle them.
    x = np.asarray(x)
    y = np.asarray(y)
    x_midpts = np.hstack((x[0], 0.5 * (x[1:] + x[:-1]), x[-1]))
    y_midpts = np.hstack((y[0], 0.5 * (y[1:] + y[:-1]), y[-1]))

    # Determine the start, middle, and end coordinate pair of each line segment.
    # Use the reshape to add an extra dimension so each pair of points is in its
    # own list. Then concatenate them to create:
    # [
    #   [(x1_start, y1_start), (x1_mid, y1_mid), (x1_end, y1_end)],
    #   [(x2_start, y2_start), (x2_mid, y2_mid), (x2_end, y2_end)],
    #   ...
    # ]
    coord_start = np.column_stack((x_midpts[:-1], y_midpts[:-1]))[:, np.newaxis, :]
    coord_mid = np.column_stack((x, y))[:, np.newaxis, :]
    coord_end = np.column_stack((x_midpts[1:], y_midpts[1:]))[:, np.newaxis, :]
    segments = np.concatenate((coord_start, coord_mid, coord_end), axis=1)

    lc = LineCollection(segments, **default_kwargs)
    lc.set_array(c)  # set the colors of each segment
    _ax = ax.add_collection(lc)
    ax.autoscale_view()  # necessário pra atualizar os limites do gráfico
    return _ax
