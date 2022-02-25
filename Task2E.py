from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def run():
    """Plots a graph of the water levels against time for the past 10 days of the 5 stations which the current relative water level is greatest."""
    stations = build_station_list()
    #greatest_5 = stations_highest_rel_level(stations, 5)
    dt = 10
    test = stations[0:5]
    for station in test:
        dates , levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        print(plot_water_levels(station, dates, levels))
    #print(levels)
    #print(type(dates[0]))
    #for n in range(len(dates)):
        #dates[n] = dates[n].strftime("%m/%d/%Y")
    #print(type(dates[0]))
    #print(dates)
    #for station in greatest_5:
        #dates , levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        #print(plot_water_levels(station, dates, levels))



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()