from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def run():
    """Prints a list of tuples (station name, town, distance) for the 10 closest and the 10 furthest stations from the Cambridge city centre, (52.2053, 0.1218)."""
    stations = build_station_list()  #builds list of stations
    towns=[]
    for station in stations:
        towns.append(station.town)
    
    p = (52.2053, 0.1218)    #coordinate for cambridge city centre

    full_list= stations_by_distance(stations, p)   #full list of all mintoring stations, ordered with closest to cty centre
    closest_10= full_list[:10]        #10 closest stations to city centre
    furthest_10= full_list[-10:]       #10 furthest stations from city centre
    for n in closest_10:
        closest_10.append(towns[n])

    #town = station.town
    #station[1] = town
    #print(full_list)
    print(closest_10)

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()