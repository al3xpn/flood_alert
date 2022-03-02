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

def get_gradient(dates, levels, p):
    if len(dates) != 0:
        try:
            p_coeff = np.polyfit(dates - dates[-1], levels, p)     
        except LinalgError:
            pass
        poly = np.poly1d(p_coeff)   
        derivative = np.polyder(poly)
        today = dates[0] - dates[-1]
        gradient = derivative(today)
        return gradient
        
    else:
        return None   