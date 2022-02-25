from floodsystem.station import MonitoringStation
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    list_of_tuples = []
    for n in range(len(stations)):
        x = stations[n].typical_range_consistent()
        if x == True:
            y = stations[n].relative_water_level()
            if y == None:
                pass
            elif y > tol:
                tuple = (stations[n].name, stations[n].relative_water_level())
                list_of_tuples.append(tuple)
    output = sorted_by_key(list_of_tuples, 1)
    output.reverse()
    return output

def stations_highest_rel_level(stations, N):
    stations_all = stations_level_over_threshold(stations, 0)
    return stations_all[:N]
