from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import BigOlFlood,get_gradient

stations = build_station_list()
update_water_levels(stations)

x = BigOlFlood(stations)
High = []
Medium = []
Low = []
for town, average_level in x.items():
    if 1 < average_level < 1.5:
        Low.append(town)
    elif 1.5 < average_level < 1.75:
        Medium.append(town)
    elif 1.75 < average_level:
        High.append(town)
    else:
        pass
print('High Risk : {}' .format(High))
print('Medium Risk: {}'.format(Medium))
print('Low Risk: {}'.format(Low))
