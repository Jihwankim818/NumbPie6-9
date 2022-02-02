import matplotlib.pyplot as plt
from datetime import datetime, timedelta

import matplotlib

def plot_water_levels(station, dates, levels):
    
        
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title('station[n].name')
    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates,levels,p)
    plt.plot(dates, levels, '-')
    plt.plot(dates, poly(matplotlib.dates.date2num(dates)))
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title('station[n].name')
    plt.tight_layout()
    plt.show()