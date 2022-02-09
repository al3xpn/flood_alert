from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    #build list of stations
    stations = build_station_list()

    #apply function to form a list of tuples
    river_tuples_nine = rivers_by_station_number(stations, 9)

    #print the formed list
    print(river_tuples_nine)

if __name__ == "__main__":
<<<<<<< HEAD
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
=======
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
>>>>>>> ad8421f27cbf30156fefc368e5b49f13c5fe49de
