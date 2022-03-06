import numpy as np
from sympy import lowergamma
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import get_gradient
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.warnings import risk_assessment
from floodsystem.station import MonitoringStation

def run():
    #create list of stations
    stations = build_station_list()

    #update their water level data
    update_water_levels(stations)
    
    #runs code to divide stations into lists of tuples based on their risk of flooding
    x = risk_assessment(stations)
    severe = []
    high = []
    moderate = []
    low = []
    for tuple in x:
        if tuple[1] == 4:
            severe.append(tuple)
        elif tuple[1] == 3:
            high.append(tuple)
        elif tuple[1] == 2:
            moderate.append(tuple)
        elif tuple[1] == 1:
            low.append(tuple)
        else:
            print("error")
    print(severe)
    print(high)

if __name__ == "__main__":
    run()
