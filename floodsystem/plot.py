import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """"""

    plt.plot(dates, station.typical_range[0])
    plt.plot(dates, station.typical_range[1])
    plt.plot(dates, levels)

    plt.xlabel('Date/Time')
    plt.ylabel('Water level (m)')
    plt.title(station)
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

