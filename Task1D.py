from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
def run():

    """Requirements for Task 1D"""

    #define Stations
    stations = build_station_list()

    #Generate list of rivers
    x = rivers_with_station(stations)
    print("{} rivers".format(len(x)))
    print("First 10 - {}".format(x[:10]))

    #Generate dictionary
    x = stations_by_river(stations)
    print(x)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()