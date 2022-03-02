from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.station import MonitoringStation

def run():
    """Plots a graph of the water levels against time for the past 10 days of the 5 stations which the current relative water level is greatest."""
    stations = build_station_list()
    update_water_levels(stations)
    dt = 10
    top_5 = stations_highest_rel_level(stations, 5)
    top_5_stations = []

    for n in range(len(top_5)):
        top_5_stations.append(top_5[n][0])

    for station in top_5_stations:
        dates , levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)




if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()