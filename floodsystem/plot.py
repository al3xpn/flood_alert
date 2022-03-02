import matplotlib.pyplot as plt
import matplotlib
from floodsystem.analysis import polyfit
import numpy as np
def plot_water_levels(station, dates, levels):
    """For 2E - Plots graph for data and low/high ranges against time"""
    low_range_list = [station.typical_range[0]] * len(dates) #create a list of numbers (typical low level) that is the same length of the list of dates so can be plotted together
    high_range_list = [station.typical_range[1]] * len(dates)
    plt.plot(dates, low_range_list, label = "Low range")    #just plotting the values
    plt.plot(dates, high_range_list, label = "High range")
    plt.plot(dates, levels , label = "Historical Data")    #historical data (stuff that changes)

    plt.legend(loc='upper right')      #added lables to show which line is which
    plt.xlabel('Date/Time(Year-Month-Day)')
    plt.ylabel('Water level (m)')
    plt.title(station.name)
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """For 2F - Plots graph for data, low/high ranges and polynomial best fit against time"""
    poly, d0 = polyfit(dates, levels, p)

    low_range_list = [station.typical_range[0]] * len(dates)  #once again creating list of the different levels
    high_range_list = [station.typical_range[1]] * len(dates)
    x = matplotlib.dates.date2num(dates)    #creating list of dates that are now float values, not datetime values
    x = x - x[0]      #as they are now just large floats, i have take away the first value so that the list starts at 0 (in time) and increases from there
    plt.plot(dates, poly(x), label = "Best fit polynomial")   #plot dates against the polynomial values (think of poly as just y= x^4 + 4x^3 + ... (for example) for different values of x)
    plt.plot(dates, levels, label = "Historical Data")
    plt.plot(dates, low_range_list, label = "Low range")
    plt.plot(dates, high_range_list, label = "High range")

    plt.legend(loc='upper left')
    plt.xlabel('Date/Time(Month-Day-Hour)')
    plt.ylabel('Water level (m)')
    plt.title(station.name)
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt.show()

