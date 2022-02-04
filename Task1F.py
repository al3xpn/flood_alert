from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()

def run():
    """Builds a list of all stations with inconsistent typical range data. Print a list of station names, in alphabetical order, for stations with inconsistent data."""

    inconsistent_list = inconsistent_typical_range_stations(stations)


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
