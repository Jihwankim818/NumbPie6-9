from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
stations = build_station_list()
def test_stations_by_distance():
    x = stations_by_distance(stations, (52.2053, 0.1218))
    z = x[:10]
    assert len(x) > 0
    assert len(z) == 10