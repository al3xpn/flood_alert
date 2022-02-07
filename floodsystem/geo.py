# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#from more_itertools import set_partitions

from floodsystem.station import MonitoringStation
#from floodsystem.stationdata import build_station_list
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
    """Returns a list of all stations within radius r of a geographic coordinate x"""
    list_within_radius=[] #opens a list
    for station in stations: #iterate through stations
        coord = station.coord #forms a tuple of (... , ...)
        name = station.name #forms a string name
        x = centre 
        distance = float(haversine(coord, x)) #calculates the distance between the station and the centre (x) as a float
        if distance <= r: #if station is within the radius
            list_within_radius.append(name) #adds the name of the station to a list
    return list_within_radius


def rivers_with_station(stations):
    """Returns a set with the names of the rivers with a monitoring station"""
    set_of_rivers = set()       #a set contains only unique elements so river names are not repeated
    for station in stations:
        set_of_rivers.add(station.river)     #just adds river name to the set

        if station.river == None:         #river name might not always be available so is ignored
            pass

    return set_of_rivers

def stations_by_river(stations):
    """Returns a dictionary that maps river names """
    riv_stat_dict = {}       #forms empty dictionary
    for station in stations:
        if station.river in riv_stat_dict:      #checks if the river name is already in the dictionary
            riv_stat_dict[station.river].append(station.name)    #if it is then we add the station name to the already existing list
            riv_stat_dict[station.river].sort()          #sort the list alphabetically
        else:
            riv_stat_dict[station.river] = [station.name]       #if the river name is not in the dictionary it creates a new key and value

    return riv_stat_dict