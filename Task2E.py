from turtle import update
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

#I will update new one soon as u finish the coding


def run():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    N = 5
    highlist = stations_highest_rel_level(stations, N)
    # Station name to find
    x = []
    for station in stations:
       for i in range(len(highlist)):
          if station.name == highlist[i][0]:
             x.append(station)
          else:
             pass

    dt = 10
    for i in range(len(x)):
        dates, levels = fetch_measure_levels(
        x[i].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(x[i], dates, levels)
    
run()