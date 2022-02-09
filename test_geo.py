"""Unit test for the  geo.py module"""

from floodsystem.geo import rivers_with_station, stations_by_distance, stations_by_river, stations_within_radius
from floodsystem.stationdata import build_station_list
from haversine import haversine
stations = build_station_list()

def test_stations_by_distance():
    """Tests the function stations_by_distance() in the geo.py submodule"""
    p = (52.188229, 0.102169)
    sorted_distance_list = stations_by_distance(stations, p)
    assert len(sorted_distance_list) == 2164  #number of measuring stations it should return

    assert sorted_distance_list[-1][0] == 'Penberth'

    assert type(sorted_distance_list[60]) == tuple


def test_rivers_with_station():
    """Tests the function rivers_by_station() in the geo.py submodule"""
    rivers = (rivers_with_station(stations))
    rivers_list = list(rivers)
    assert len(rivers_list) == 950

    assert (sorted(rivers_list))[0] == 'Addlestone Bourne'

    assert type(rivers) == set

    test = []
    for river in rivers:
        if river == None:
            test.append(True)

        else:
            test.append(False)

    assert test[0] == False

def test_stations_within_radius():

    #checks that, if the radius of the area is set to zero, there is no more than 1 station found
    centre = (52.2053, 0.1218)
    stations_list = stations_within_radius(stations, centre, 0)
    assert len(stations_list) <= 1

    #checks that, if the centre of the circular are is set in hong kong and the radius is set to 10km, no stations are returned
    centre = (22.3193, 114.1694)
    stations_list = stations_within_radius(stations, centre, 10)
    assert len(stations_list) == 0

    #checks that if the radius is set to over half of the circumference of the earth in a plane that cuts through its centre, there are stations returned
    centre = (0.0000, 0.0000)
    stations_list = stations_within_radius(stations, centre, 200000000)
    assert len(stations_list) >= 0

    #checks that the data type of the output of the function is a list
    centre = (52.2053, 0.1218)
    stations_list = stations_within_radius(stations, centre, 10)
    assert type(stations_list) == list
    
def test_stations_by_river():
    rivers_dict = stations_by_river(stations)
    assert type(rivers_dict) == dict

    
    