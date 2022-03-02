import matplotlib.pyplot as plt
import matplotlib
from floodsystem.analysis import polyfit
import numpy as np
def plot_water_levels(station, dates, levels):
    """"""
    low_range_list = [station.typical_range[0]] * len(dates)
    high_range_list = [station.typical_range[1]] * len(dates)
    plt.plot(dates, low_range_list, label = "Low range")
    plt.plot(dates, high_range_list, label = "High range")
    plt.plot(dates, levels , label = "Historical Data")

    plt.legend(loc='upper right')
    plt.xlabel('Date/Time')
    plt.ylabel('Water level (m)')
    plt.title(station.name)
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """"""
    poly, d0 = polyfit(dates, levels, p)

    low_range_list = [station.typical_range[0]] * len(dates)
    high_range_list = [station.typical_range[1]] * len(dates)
    x = matplotlib.dates.date2num(dates)
    x = x - x[0]
    x1 = np.linspace(x[0], x[-1], len(dates))
    plt.plot(dates, poly(x1), label = "Best fit polynomial")
    plt.plot(dates, levels, label = "Historical Data")
    plt.plot(dates, low_range_list, label = "Low range")
    plt.plot(dates, high_range_list, label = "High range")

    plt.legend(loc='upper left')
    plt.xlabel('Date/Time')
    plt.ylabel('Water level (m)')
    plt.title(station.name)
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt.show()

