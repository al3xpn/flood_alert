from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit
def run():
    """Plots graphs for the 5 stations with highest current relative water level. Plots the level data extending back 2 days. Also plots high/low range and best fit of polynomial of degree 4 against time.""" 
    stations = build_station_list()
    update_water_levels(stations)
    dt = 2   #number of days extending back
    top_5 = stations_highest_rel_level(stations, 5)   #gets list of tuples for top 5 stations with highest relative water level , tuple = (station (object), relative level)
    top_5_stations = []   #create empty list to put just the station objects into

    for n in range(len(top_5)):
        top_5_stations.append(top_5[n][0])    #puts just the station objects in the list

    for station in top_5_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))   #gathers dates and the levels at those dates
        plot_water_level_with_fit(station, dates, levels, 4)    #plots graph
        
    
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()