from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():

    """Requirements for Task 1B"""

    #define Stations
    stations = build_station_list()

    #Generate list 
    x = stations_by_distance(stations, (52.2053, 0.1218))

    #Print closest 10 and furthest 10
    print(x[:10])
    print("------------")
    print(x[-10:])


    

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
