from floodsystem.analysis import get_gradient
from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.dates

def risk_assessment(stations):

        list_tuples = []
        for station in stations:
            if station.relative_water_level() == None:
                pass
            else:
                y = station.relative_water_level()
            dt = 2
            dates, levels = fetch_measure_levels(station.measure_id, timedelta(days=dt))
            dates_num = matplotlib.dates.date2num(dates)
            data_values = {}
            for i in range(len(dates_num)-1):
                try:
                    data_values[dates_num[i]] = levels[i]
                except:
                    pass
            values_to_remove = []
            for level in data_values.values():
                if type(level) != float:
                    x = (level[0], level[1])
                    values_to_remove.append(x)
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

                if y > 2 :
                    tuple4 = [station.name, 4]
            
                    if gradient <= -1 and y < 3:
                        tuple4[1] -= 1
                    tuple = (tuple4[0], tuple4[1])
                    list_tuples.append(tuple)

                elif y > 1.6:
                    tuple3 = [station.name, 3]
            
                    if gradient >= 1 and y > 1.9:
                        tuple3[1] += 1
                
                    elif gradient <= -1 and y < 1.7:
                        tuple3[1] -= 1
                    tuple = (tuple3[0], tuple3[1])
                    list_tuples.append(tuple)

                elif y > 0.5:
                    tuple2 = [station.name, 2]
           
                    if gradient >= 1 and y > 1.2:
                        tuple2[1] += 1
                
                    elif gradient <= -1 and y < 0.7:
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
