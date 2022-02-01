from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""
    stations = build_station_list()
    rivers = list(rivers_with_station(stations))
    print(rivers)
    num_rivers = len(rivers)
    print(num_rivers)
    sorted_rivers= rivers.sort()
    first_10 = sorted_rivers[:10]

    print('{} stations. First 10 - {}'.format(num_rivers, first_10) )


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()