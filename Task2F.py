



from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit
def run():
    """""" 
    stations = build_station_list()
    update_water_levels(stations)
    dt = 2
    top_5 = stations_highest_rel_level(stations, 5)
    top_5_stations = []

    for n in range(len(top_5)):
        top_5_stations.append(top_5[n][0])

    for station in top_5_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, 4)
    
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()