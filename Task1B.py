from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
stations = build_station_list()

print(stations_by_distance(stations, (52.188229, 0.102169)))


def run():
    #


if __name__ == "__main__":
    run()

print(len(stations_by_distance(stations, (52.188229, 0.102169))))