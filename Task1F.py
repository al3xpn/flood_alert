from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    """Builds a list of all stations with inconsistent typical range data. Print a list of station names, in alphabetical order, for stations with inconsistent data."""

    stations = build_station_list()       
    in_list = inconsistent_typical_range_stations(stations)
    in_list.sort()     #sorts the list alphabetically

    print(in_list)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
