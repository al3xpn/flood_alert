from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():

    #make a list
    stations = build_station_list() 

    centre = (52.2053, 0.1218)

    #run function
    stations_in_ten = stations_within_radius(stations, centre, 10)

    #sort function
    stations_in_ten.sort()

    print(stations_in_ten)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()