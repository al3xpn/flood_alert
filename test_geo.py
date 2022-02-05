"""Unit test for the  geo.py module"""

from floodsystem.geo import rivers_with_station, stations_by_distance, stations_by_river
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    """Tests the function stations_by_distance() in the geo.py submodule"""
    p = (52.188229, 0.102169)
    stations = build_station_list()
    sorted_distance_list = stations_by_distance(stations, p)
    assert len(sorted_distance_list) == 2165  #number of measuring stations it should return

    assert sorted_distance_list[-1][0] == 'Penberth'

    assert type(sorted_distance_list[60]) == tuple


def test_rivers_with_station():
    """Tests the function rivers_by_station() in the geo.py submodule"""
    stations = build_station_list()
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

def test_stations_by_river():
    stations = build_station_list()
    assert type(stations_by_river(stations)) == dict
