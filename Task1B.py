from matplotlib.pyplot import close
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def run():
    """Prints a list of tuples (station name, town, distance) for the 10 closest and the 10 furthest stations from the Cambridge city centre, (52.2053, 0.1218)."""
    stations = build_station_list()  #builds list of stations
    
    p = (52.2053, 0.1218)    #coordinate for cambridge city centre

    full_list= stations_by_distance(stations, p)   #full list of all mintoring stations, ordered with closest to cty centre
    closest_10= full_list[:10]        #10 closest stations to city centre
    furthest_10= full_list[-10:]       #10 furthest stations from city centre

    for n in range(len(closest_10)):
        for station in stations:
            if station.name == closest_10[n][0]:   #only iterates over stations in the top 10 closest
                single_list = list(closest_10[n]) #was tuple before, turn into list so can insert town name
                single_list.insert(1, station.town)   #inserts town name into list between name and distance
                single_tuple=tuple(single_list)     #turn it back to tuple
                closest_10[n] = single_tuple       #replace item in list
    print(closest_10)

    for n in range(len(furthest_10)):
        for station in stations:
            if station.name == furthest_10[n][0]:   #iterates over top 10 furthest
                single_list = list(furthest_10[n]) #was tuple before, turn into list so can insert
                single_list.insert(1, station.town)  
                single_tuple=tuple(single_list)
                furthest_10[n] = single_tuple
    print(furthest_10)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()