import numpy as np
from sympy import lowergamma
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import get_gradient
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib
from floodsystem.station import MonitoringStation




def risk_assessment(stations):

        #open a list of tuples
        list_tuples = []

        #iterates through stations
        for station in stations:

            #if there is no water level data, ignore this station
            if station.relative_water_level() == None:
                pass

            #if there is data, find the relative water level of the station through function relative_water_level
            else:
                y = station.relative_water_level()
            dt = 2

            #fetch data for water levels each day
            dates, levels = fetch_measure_levels(station.measure_id, timedelta(days=dt))
            #plot this data
            dates_num = matplotlib.dates.date2num(dates)

            data_values = {}
            #add the levels to a dictionary
            for i in range(len(dates_num)-1):
                try:
                    data_values[dates_num[i]] = levels[i]
                except:
                    pass
            values_to_remove = []
            #if any of the levels in the dictionary are not of the type float, add them to a list to be removed
            for level in data_values.values():
                if type(level) != float:
                    x = (level[0], level[1])
                    values_to_remove.append(x)
            #
            for level in values_to_remove:
                a = list(level)
                data_values.pop(list(data_values.keys())[list(data_values.values()).index(a)])
            for date in data_values:
                if data_values[date] == None:
                    data_values.pop(date)
        
            x_dates = []
            y_levels = []
            for date in data_values:
                x_dates.append(date)
                y_levels.append(data_values[date])
            


            if len(dates) != 0:

                gradient = get_gradient(x_dates, y_levels, p=4)
                if gradient == None:
                    continue

                if y > 10 :
                    tuple4 = [station.name, 4]
            
                    if gradient <= -1 and y < 11:
                        tuple4[1] -= 1
                    tuple = (tuple4[0], tuple4[1])
                    list_tuples.append(tuple)

                elif y > 5:
                    tuple3 = [station.name, 3]
            
                    if gradient >= 1 and y > 9:
                        tuple3[1] += 1
                
                    elif gradient <= -1 and y < 6:
                        tuple3[1] -= 1
                    tuple = (tuple3[0], tuple3[1])
                    list_tuples.append(tuple)

                elif y > 0.5:
                    tuple2 = [station.name, 2]
           
                    if gradient >= 1 and y > 4:
                        tuple2[1] += 1
                
                    elif gradient <= -1 and y < 1:
                        tuple2[1] -= 1
                    tuple = (tuple2[0], tuple2[1])
                    list_tuples.append(tuple)
                else:
                    tuple1 = [station.name, 1]
            
                    if gradient >= 1 and y > 0:
                        tuple1[1] += 1
            
                    tuple = (tuple1[0], tuple1[1])
                    list_tuples.append(tuple)
            else:
                continue
        else:
            pass
        
        return list_tuples
