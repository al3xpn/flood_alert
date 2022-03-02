from floodsystem.stationdata import build_station_list
from floodsystem.plot_2 import plot_water_levels
import floodsystem.flood
import floodsystem.datafetcher
import matplotlib.pyplot as plt
from datetime import timedelta, datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
import matplotlib.pyplot as plt
from floodsystem.station import inconsistent_typical_range_stations
import numpy as np

def run():
    stations = build_station_list()
    update_water_levels(stations)
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    stations_list = []
    for station in stations:
        if station not in inconsistent_stations:
            stations_list.append(station)
        else:
            pass
    
    y = floodsystem.flood.stations_highest_rel_level(stations_list, N=7)
    dt = 10
    print(y)

    station_list_two = []
    for name in y:
        station_name = name[0]
    # Find station
        for n in stations_list:
            if n.name == station_name:
                station_list_two.append(n)
    
    
    for s in range(len(station_list_two)-1):
        dates, levels = fetch_measure_levels(station_list_two[s].measure_id, dt=timedelta(days=dt))
        stations_list = []
        if len(dates) != 0 and np.size(levels) != 0:
            plot_water_levels(station_list_two[s], dates, levels)
        
        

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()