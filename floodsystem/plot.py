import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
from .analysis import polyfit


from matplotlib.dates import date2num

def plot_water_levels(station, dates, levels):
    
        
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    
    poly, d0 = polyfit(dates, levels, p)
    hi = date2num(dates)
    plt.plot(dates, levels, '-')
   
    plt.plot(dates, poly(hi-d0))
    
    
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()