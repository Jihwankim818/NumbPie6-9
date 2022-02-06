from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

stations = build_station_list()
def test_typical_range_consistent():
    for n in range(len(stations)):
        return stations[n].typical_range_consistent