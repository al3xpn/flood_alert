from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    #create list of all stations
    stations = build_station_list()

    #get the latest information for each station
    update_water_levels(stations)

    #create a list of tuples of the top 10 stations with the highest relative water level and their relative water levels
    highest_ten = stations_highest_rel_level(stations, 10)

    #outputs these tuples in the form: name, relative water level
    for i in range(len(highest_ten)):
        print("{}, {}".format(highest_ten[i][0], highest_ten[i][1]))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
