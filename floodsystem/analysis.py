import matplotlib as plt
import numpy as np

def polyfit(dates, levels, p):
    """"""
    x = plt.dates.date2num(dates)
    y = levels

    d0 = x[0]

    p_coeff = np.polyfit(x - d0, y, p)

    poly = np.poly1d(p_coeff)

    return poly, d0

    