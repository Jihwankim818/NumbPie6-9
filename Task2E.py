import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
import datetime

from floodsystem.stationdata import build_station_list

#I will update new one soon as u finish the coding
highlist = ['Ledgard Bridge','Godstow Lock', 'Windyridge Road','Castle Mill (Bedford)', 'Newark Weir']
def plot_water_levels(station, dates, levels):
    
        
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title('station[n].name')
    plt.tight_layout()
    plt.show()

stations = build_station_list()
def run():
    newlist = []
    for n in range(len(stations)):
        if stations[n].name in highlist:
            newlist.append(stations[n])
        else:
            pass
    return newlist
    




dt = 2
dates, levels = fetch_measure_levels(hello(stations)[1].measure_id, dt=datetime.timedelta(days=dt))
print(dates,levels)

plot_water_levels(hello(stations)[1], dates, levels)