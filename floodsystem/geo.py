# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from pickle import TUPLE1
from floodsystem.station import MonitoringStation
from haversine import haversine
from floodsystem.utils import sorted_by_key  # noqa




def stations_by_distance(stations, p):
    z = []
    for n in range(len(stations)):
        tuple1 = (stations[n].name , haversine(stations[n].coord, p))
        z.append(tuple1)
    x = sorted_by_key(z, 1)
    return x
    

def stations_within_radius(stations, centre, r):
    Close = []
    for n in range(len(stations)):
        if haversine(centre, stations[n].coord) < r :
            Close.append(stations[n].name)
    AlphaClose = sorted(Close)
    return AlphaClose


def rivers_with_station(stations):
    Rivers = set()
    for n in range(len(stations)):
        if stations[n].river not in Rivers:
            Rivers.add(stations[n].river)
    AlphaRivers = sorted(Rivers)
    return AlphaRivers

def stations_by_river(stations):
    RiverStat = {}
    RiverStat.update({'River Cam': ''})
    for n in range(len(stations)):
        if stations[n].river == 'River Cam':
            RiverStat['River Cam'] = RiverStat['River Cam'] + ' ' + '{},'.format(stations[n].name)
    x = RiverStat['River Cam']
    return x

def rivers_by_station_number(stations, N):
    river2 ={}
    for n in range(len(stations)):
        if stations[n].river not in river2:
             river2.update({stations[n].river: 1})
        elif stations[n].river in river2:
             river2[stations[n].river] = river2[stations[n].river] + 1

    
    rivernumpy = river2.items()
    rivernumppy = list(rivernumpy)
    rivernumppy.sort(key = lambda x:x[1], reverse = True)
    return rivernumppy[:N+1]

   


    
        

    
    

