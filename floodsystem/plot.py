import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """"""
    low_range_list = [station.typical_range[0]] * len(dates)
    high_range_list = [station.typical_range[1]] * len(dates)
    plt.plot(dates, low_range_list, label = "Low range")
    plt.plot(dates, high_range_list, label = "High range")
    plt.plot(dates, levels , label = "Data")

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
    plt.plot(dates, poly)
    plt.plot(dates, levels)

    plt.xlabel('Date/Time')
    plt.ylabel('Water level (m)')
    plt.title(station)
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt.show()

