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
    
    #x = list(closest_10[4])
    #print(x)
    #x.insert(1, 'Test')
    #print(x)
    #print(tuple(x))
    #closest_10[5] = tuple(x)
    #print(closest_10)

    for n in range(len(closest_10)):
        single_list = list(closest_10[n]) #was tuple before, turn into list so can insert
        single_list.insert(1, 'Town')
        single_tuple=tuple(single_list)
        closest_10[n] = single_tuple
    print(closest_10)


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()