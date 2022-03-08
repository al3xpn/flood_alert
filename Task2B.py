from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)


def run():

    #form list of stations over the threshold of 0.8
    x = stations_level_over_threshold(stations, 0.8) 

    #iterates through formed list to output required information
    for n in range(len(x)):
        print("{}, {}".format(x[n][0].name, x[n][1]))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
