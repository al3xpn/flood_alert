from floodsystem.station import MonitoringStation
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol): #nputs a list of stations with their relative water level and a tolerance number and returns a list of all stations with a relative water level above the tolerance in descending order

    #opens empty list of tuples
    list_of_tuples = []

    #iterates through list
    for n in range(len(stations)):

        #checks the validty of the informaton in the list
        x = stations[n].typical_range_consistent()
        if x == True:

            #if passes checks, get the relatve water level of the station
            y = stations[n].relative_water_level()

            #if there is no data for relative water level, ignore this station
            if y == None:
                pass

            #if the relative water level is above the tolerance level
            elif y > tol:

                #list of tuples adds onto the end a tuple of the station's name and then its relative water level
                tuple = (stations[n].name, stations[n].relative_water_level())
                list_of_tuples.append(tuple)
    
    #list of tuples is sorted by ascending relative water level and then reversed and the final list is returned
    output = sorted_by_key(list_of_tuples, 1)
    output.reverse()
    return output

def stations_highest_rel_level(stations, N): #inputs a list of stations and the number of outputs wanted (N) and returns the top N stations with the highest relative water level

    #creates a list of all of the stations as tuples with their relative water level, ordered by descending relative water level
    stations_all = stations_level_over_threshold(stations, 0)

    #returns the first (top) N stations in the list
    return stations_all[:N]
