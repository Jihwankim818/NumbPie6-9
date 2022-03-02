import numpy as np
from matplotlib.dates import date2num
def polyfit(dates, levels, p):
    x = date2num(dates)
    d0 = x[0]
    z = x - d0

    p_coeff = np.polyfit(z,levels,p)
    poly = np.poly1d(p_coeff)
    
    return poly, d0



