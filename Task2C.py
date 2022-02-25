from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list
    update_water_levels(stations)
    highest_ten = stations_highest_rel_level(stations, 10)
    for i in range(len(highest_ten)):
        print("{}, {}".format(highest_ten[i][0], highest_ten[i][1]))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
