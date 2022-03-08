import matplotlib.dates 
import numpy as np
from numpy.linalg import LinAlgError

def polyfit(dates, levels, p):
    """"""
    x = matplotlib.dates.date2num(dates)        #turns dates into a list of floats instead of datetime objects
    y = levels                  #just the levels of river at given date

    d0 = x[0]               #offset (first date value)
    #x - d0 is required as dates.date2num returns the number of days since the origin of the gregorian calendar so gives too large values and causes rounding errors.
    p_coeff = np.polyfit(x - d0, y, p)    
    # Find coefficients of best-fit polynomial f(x) of degree 4
    poly = np.poly1d(p_coeff)   # Convert coefficient into a polynomial that can be evaluated

    return poly, d0

def get_gradient(dates, levels, p):

    #check it is not an empty set
    if len(dates) != 0:
        #plot a graph of the dates and levels
        try:
            p_coeff = np.polyfit(dates - dates[-1], levels, p)     
        except LinAlgError:
            pass
        poly = np.poly1d(p_coeff)   
        #find the derivative of the graph
        derivative = np.polyder(poly)
        #set today as the correct date
        today = dates[0] - dates[-1]
        #find gradient of poly graph (value of derivative graph) at today
        gradient = derivative(today)
        #output that gradient
        return gradient
        
    else:
        return None   