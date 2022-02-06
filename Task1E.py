from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from pickle import TUPLE1
from floodsystem.station import MonitoringStation
from haversine import haversine
from floodsystem.utils import sorted_by_key  # noqa#




def run():

    """Requirements for Task 1E"""

    #define Stations
    stations = build_station_list()
    BigG = rivers_by_station_number(stations, 9)
    print(BigG)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()


