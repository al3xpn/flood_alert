from floodsystem.analysis import get_gradient
from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.dates

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
            
            #remove the data values in the to remove list
            for level in values_to_remove:
                a = list(level)
                data_values.pop(list(data_values.keys())[list(data_values.values()).index(a)])
            for date in data_values:
                if data_values[date] == None:
                    data_values.pop(date)
        
            #store dates and corresponding levels in two lists
            x_dates = []
            y_levels = []
            for date in data_values:
                x_dates.append(date)
                y_levels.append(data_values[date])
            


            if len(dates) != 0:

                #find the most recent gradient in the plots of levels against dates
                gradient = get_gradient(x_dates, y_levels, p=4)
                if gradient == None:
                    continue


                #if relative water level greater than 2, put in element 4 (severe)
                if y > 2 :
                    el4 = [station.name, 4]
                    
                    #if gradient less tahn -1 and relative water level less than 3, move down to tuple 3 (high)
                    if gradient <= -1 and y < 3:
                        el4[1] -= 1
                    
                    #form tuple of station name and value of the element (4,3,2,1) 
                    tuple = (el4[0], el4[1])
                    #add tuple to list of tuples
                    list_tuples.append(tuple)

                #if between 1.4 and 2, high
                elif y > 1.4:
                    el3 = [station.name, 3]
                    
                    #if grad > 1 and rel water level >1.75, move up, for teh following inequalities move down
                    if gradient >= 1 and y > 1.75:
                        el3[1] += 1
                
                    elif gradient <= -1 and y < 1.55:
                        el3[1] -= 1
                    tuple = (el3[0], el3[1])
                    list_tuples.append(tuple)

                #if between 0.5 and 1.4, moderate
                elif y > 0.5:
                    el2 = [station.name, 2]
           
                    if gradient >= 1 and y > 1.175:
                        el2[1] += 1
                
                    elif gradient <= -1 and y < 0.725:
                        el2[1] -= 1
                    tuple = (el2[0], el2[1])
                    list_tuples.append(tuple)

                #if below 0.5, low
                else:
                    el1 = [station.name, 1]
            
                    if gradient >= 1 and y > 0:
                        el1[1] += 1
            
                    tuple = (el1[0], el1[1])
                    list_tuples.append(tuple)
            else:
                continue
        else:
            pass
        

        return list_tuples
