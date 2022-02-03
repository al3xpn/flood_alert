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

def stations_by_distance(stations, p):
    """Finds the distance from a coordinate 'p' to the stations, and orders it with the closest first"""
    name_distance_list = []
    for station in stations:
        coord = station.coord   #forms a tuple of (... , ...)
        name = station.name     #forms a string name
        distance = float(haversine(coord, p))  #forms a float of the distance .....

        name_distance_tuple = (name, distance)
        name_distance_list.append(name_distance_tuple)  #forms the list

    sorted_name_distance = sorted_by_key(name_distance_list, 1)  #orders the list

    return sorted_name_distance

def stations_within_radius(stations, centre, r):
    """returns a list of all stationa within radius r of a geographic coordinate x"""
    list_within_radius=[] #opens a list
    for station in stations: #iterate through stations
        coord = station.coord #forms a tuple of (... , ...)
        name = station.name #forms a string name
        x = centre 
        distance = float(haversine(coord, x)) #calculates the distance between the station and the centre (x) as a float
        if distance <= r: #if station is within the radius
            list_within_radius.append(name) #adds the name of the station to a list
    return list_within_radius


def rivers_by_station_number(stations, N):
    rivers = ()
    river_number_list = []
    river1 = 'test'
    count = 1
    sorted_stations = sorted(stations)
    for station in sorted_stations:
        river2 = station.river
        if river2 == river1:
            count = count + 1
        else:
            river_number_tuple = (river1, count)
            river_number_list.append(river_number_tuple)
            count = 1
        river1 = river2
    sorted_river_number_list = sorted(river_number_list)
    sorted_river_number_list.reverse()
    x = sorted_river_number_list([N][1])
    y = 1
    M = N
    while sorted_river_number_list([N+y][1]) == x:
        M = M + 1
        y = y + 1
    river_number_list_N = sorted_river_number_list[0:M]
    return river_number_list_N

def rivers_by_station_number2(stations, N):
    river_list = ()
    for station in stations:
        river = station[5]
        river_list.append(river)
    river_list.sort()
    river1 = "test"
    count = 1
    for river in river_list:
        if river == river1:
            count = count + 1
        else:
            river_number_tuple = (river)


