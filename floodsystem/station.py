# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


from ast import Pass


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """For Task 1F"""
        if self.typical_range == None:   #if there is no range data, it is 'inconsistent so returns False'
            return False

        elif self.typical_range[1] < self.typical_range[0]:     #if the high range data is higher than the low range data, it is inconsistent so returns false
            return False

        elif (self.typical_range[1]-self.typical_range[0]) > 300:
            return False

        else:    #returns True when the data is consistent
            return True



    def relative_water_level(self):
        """For Task 2B"""
        check = self.typical_range_consistent()
        if check == True:
            if self.latest_level == None:
                return None

            else:
                ratio = ((self.latest_level - self.typical_range[0])/(self.typical_range[1] - self.typical_range[0]))
                
                if ratio > 300:   #this is done mainly to remove Letcombe Bassett from the data as the station is obviously broken
                    return None
                else:
                    return ratio
        else:
            return None


def inconsistent_typical_range_stations(stations):
    inconsistent_list = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == True:
            pass

        else:
            inconsistent_list.append(station.name)    #appends inconsistent list with stations that have inconsistent data

    return inconsistent_list


