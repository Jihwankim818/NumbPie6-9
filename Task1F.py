from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from pickle import TUPLE1
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from haversine import haversine
from floodsystem.utils import sorted_by_key  # noqa


def run():

    """Requirements for Task 1F"""

    #define Stations
    stations = build_station_list()
    BigG = inconsistent_typical_range_stations(stations)
    BigG.sort()
    print(BigG)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()