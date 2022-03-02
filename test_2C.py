from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
update_water_levels(stations)


def test_stations_highest_rel_level():
    x = stations_highest_rel_level(stations, 10)

    assert len(x) == 10
    assert x[0][0] == 'Letcombe Bassett'

