from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    """Builds a list of all stations with inconsistent typical range data. Print a list of station names, in alphabetical order, for stations with inconsistent data."""

    stations = build_station_list()
    inconsistent_list = inconsistent_typical_range_stations(stations)
    inconsistent_list.sort()

    return inconsistent_list


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
