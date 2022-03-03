import matplotlib as plt
import numpy as np
from numpy.linalg import LinAlgError

def polyfit(dates, levels, p):
    """"""
    x = plt.dates.date2num(dates)        #turns dates into a list of floats instead of datetime objects
    y = levels                  #just the levels of river at given date

    d0 = x[0]               #offset (first date value)
    #x - d0 is required as dates.date2num returns the number of days since the origin of the gregorian calendar so gives too large values and causes rounding errors.
    p_coeff = np.polyfit(x - d0, y, p)    
    # Find coefficients of best-fit polynomial f(x) of degree 4
    poly = np.poly1d(p_coeff)   # Convert coefficient into a polynomial that can be evaluated

    return poly, d0

def get_gradient(dates, levels, p):
    if len(dates) != 0:
        try:
            p_coeff = np.polyfit(dates - dates[-1], levels, p)     
        except LinAlgError:
            pass
        poly = np.poly1d(p_coeff)   
        derivative = np.polyder(poly)
        today = dates[0] - dates[-1]
        gradient = derivative(today)
        return gradient
        
    else:
        return None   