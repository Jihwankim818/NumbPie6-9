import numpy as np
import matplotlib
def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    p_coeff = np.polyfit(x,y,p)
    poly = np.poly1d(p_coeff)
    d0 = x[0]
    return d0, poly
