from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river
stations = build_station_list()
def test_rivers_with_station():
    x = rivers_with_station(stations)
    assert len(x) > 0

def test_stations_by_river():
    x = stations_by_river(stations)
    assert x[0] == 'Cam'