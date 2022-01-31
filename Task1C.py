from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
stations = build_station_list()

centre = (52.2053, 0.1218)
stations_in_ten = stations_within_radius(stations, centre, 10000)
stations_in_ten.sort()
print(stations_in_ten)