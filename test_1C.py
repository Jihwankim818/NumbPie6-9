from os import stat
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

stations = build_station_list()
def test_stations_within_radius():
    x = stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert len(x) == 11