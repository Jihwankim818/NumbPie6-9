from .utils import sorted_by_key
from floodsystem.stationdata import build_station_list, update_water_levels
from pickle import TUPLE1
from floodsystem.station import MonitoringStation
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy as np
from matplotlib.dates import date2num

stations = build_station_list()
update_water_levels(stations)

def stations_level_over_threshold(stations, tol):
    z = []
    for n in range(len(stations)):
        x = stations[n].typical_range_consistent()
        if x == True:
            y = stations[n].relative_water_level()
            if y == None:
                pass
            elif y > tol:
                Tuple2 = (stations[n].name, stations[n].relative_water_level())
                z.append(Tuple2)
    h = sorted_by_key(z, 1)
    h.reverse()
    return h

def stations_highest_rel_level(stations, N):
    AllStations = stations_level_over_threshold(stations, 0)
    return AllStations[:N]

def BigOlFlood(stations):
    Towns = {}
    Rivers = {}
    for n in range(len(stations)):
        x = stations[n].typical_range_consistent()
        if x == True:
            y = stations[n].relative_water_level()
            if y == None:
                pass
            elif stations[n].town not in Towns:
                Towns.update({stations[n].town: stations[n].relative_water_level()})
                Rivers.update({stations[n].town: 1})
            else:
                Rivers[stations[n].town] += 1
                Towns[stations[n].town] += stations[n].relative_water_level()
                Towns[stations[n].town] = Towns[stations[n].town] / Rivers[stations[n].town]
    return Towns
    
    

    






