from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

stations = build_station_list()
def test_rivers_by_station_number():
    x = rivers_by_station_number(stations, 9)
    assert len(x) > 0
    assert x[0] == ('River Thames', 55)