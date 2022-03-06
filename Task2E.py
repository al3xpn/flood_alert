from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.flood import stations_highest_rel_level

def run():
    """Plots a graph of the water levels against time for the past 10 days of the 5 stations which the current relative water level is greatest."""
    stations = build_station_list()
    update_water_levels(stations)
    dt = 10     #number of days to extend back to
    highest = stations_highest_rel_level(stations, 20)    #getting top 20 stations with highest relative level, list of tuples: tuple = (station(object), relative level)
    highest_stations = []
    for n in range(len(highest)):
        highest_stations.append(highest[n][0])      #once again just create a list of the highest rel level station objects
    counter = 0      #create a counter
    for station in highest_stations:
        dates , levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        if len(dates) == len(levels):               #had to add this check because the code before this worked fine for most stations, except one that did not have the same number of levels compared to the dates recorded
            plot_water_levels(station, dates, levels)   #plots graph of levels against time, including lines for typical high/low ranges
            counter += 1
        else: 
            pass
        if counter == 5:
            break
    



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()