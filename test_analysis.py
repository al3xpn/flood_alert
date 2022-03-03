import datetime
from floodsystem.analysis import polyfit
from floodsystem.stationdata import update_water_levels, build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import random 

def test_polyfit():
    """Tests the function polyfit used for 2F."""
    stations = build_station_list()
    update_water_levels(stations)
    dt=2
    station = stations[(random.randint(1, len(stations)))]          #gets a random station from the list of stations
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))            #gathers dates and levels for that station
    poly, d0 = polyfit(dates, levels, 4)                #forms the polynomial of best fit for the given data

    assert float('%.1g' % poly(0)) == float('%.1g' % station.latest_level)     #asserts that the result from the polynomial is equal to the relative water level at that time (to 1 sig fig) e.g. current time



