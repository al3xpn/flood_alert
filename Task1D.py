from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

def run():
    """Prints how many rivers have at least one monitoring station and prints the first 10 in alphabetical order."""
    stations = build_station_list()
    rivers = list(rivers_with_station(stations))  #forms the list of rivers that have a station
    num_rivers = len(rivers)
    rivers.sort()
    first_10 = rivers[:10]    #gives us the first 10 rivers that have been alphabetically sorted

    print('{} stations. First 10 - {}'.format(num_rivers, first_10) )


def run():
    """Prints the names of the stations located on the 'River Aire', 'River Cam' and 'River Thames'"""
    stations = build_station_list()
    river_stations = stations_by_river(stations)
    river_aire = river_stations['River Aire']
    river_cam = river_stations['River Cam']
    river_thames = river_stations['River Thames']

    print('River Aire stations: {}'.format(river_aire))
    print('---')
    print('River Cam stations: {}'.format(river_cam))
    print('---')
    print('River Thames stations: {}'.format(river_thames))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()