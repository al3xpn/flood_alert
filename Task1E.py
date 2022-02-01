from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

stations = build_station_list
river_tuples_nine = rivers_by_station_number(stations, 9)
print(river_tuples_nine)