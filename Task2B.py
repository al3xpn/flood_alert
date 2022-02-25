from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)

def test_stations_level_over_threshold(): #THIS PART IS THE TEST NOT THE TASK
    x = stations_level_over_threshold(stations, 0.8)
    assert len(x) > 0

def run():

    #form list of stations over the threshold of 0.8
    x = stations_level_over_threshold(stations, 0.8) 

    #iterates through formed list to output required information
    for n in range(len(x)):
        print("{}, {}".format(x[n][0], x[n][1]))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
