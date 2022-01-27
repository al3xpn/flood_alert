# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from more_itertools import set_partitions

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

stations = build_station_list()

def stations_by_distance(stations, p):
    """Finds the distance from a coordinate 'p' to the stations, and orders it with the closest first"""
    name_distance_list = []
    for station in stations:
        coord = station.coord   #forms a tuple of (... , ...)
        name = station.name     #forms a string name
        distance = float(haversine(coord, p))  #forms a float of the distance .....

        name_distance_tuple = (name, distance)
        name_distance_list.append(name_distance_tuple)

    sorted_name_distance = sorted_by_key(name_distance_list, 1)

    return sorted_name_distance

print(stations_by_distance(stations, ()))