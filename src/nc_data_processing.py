# process the raw data files (.nc) that contain hourly data for Texas
# the package used for .nc file processing is net CDF4

# import packages
import netCDF4 as nc
import numpy as np
from numpy import shape
import pandas as pd

# load wind/solar data from file directory, watch out for the difference of / and \
Wind = 'D:/Desk_top/Spring_2022/2022_Fall_Courses/COMS_6998_ML&Climate/ML-Climate_ZhiyuanFan/data/ERCOT_hourly_WS_0_5_deg.nc'
Solar = 'D:/Desk_top/Spring_2022/2022_Fall_Courses/COMS_6998_ML&Climate/ML-Climate_ZhiyuanFan/data/ERCOT_hourly_RAD_0_5_deg.nc'

# rename the loaded file as nc input
Windspeed = nc.Dataset(Wind)
Solarradiation = nc.Dataset(Solar)

# check the dimensions of the wind and solar data
for dim in Windspeed.dimensions.values():
     print(dim)

for dim in Solarradiation.dimensions.values():
     print(dim)

# for our case of wind and solar input, the dimension is not the same in time series
# the dimension is the same for spatial (lat-lon-index)

# print the information for two datasets and check
print(Windspeed)
print(Solarradiation)

# check the time (dates) for each dataset
time_WS = Windspeed['time'][:]
time_SR = Solarradiation['time'][:]

# check the overlapping time series
time_overlap = np.intersect1d(time_WS, time_SR)

# it actually contains all the SR data time steps
print(shape(time_overlap))

print(time_overlap[350632])
print(type(time_overlap))

for index,i in enumerate(time_SR):
    if i == time_overlap[0]:
        start_t_solar = index
        print(start_t_solar)
    if i == time_overlap[-1]:
        end_t_solar = index
        print(end_t_solar)

# load all the solar data at desired locations since it's a subset of wind time series
# store the data into csv
print(shape(Solarradiation['ssrd'][start_t_solar:end_t_solar,[18,19,20,21,24,25,26,27,30,31,32,33,37,38,39,40]]))
arr_solar = Solarradiation['ssrd'][start_t_solar:end_t_solar:,[18,19,20,21,24,25,26,27,30,31,32,33,37,38,39,40]]
DF_hold = pd.DataFrame(arr_solar)
DF_hold.to_csv("D:/Desk_top/Spring_2022/2022_Fall_Courses/COMS_6998_ML&Climate/ML-Climate_ZhiyuanFan/data/Solar_sub.csv")

# find the index that matches the wind/solar time series
for index,i in enumerate(time_WS):
    if i == time_overlap[0]:
        start_t_wind = index
        print(start_t_wind)
    if i == time_overlap[-1]:
        end_t_wind = index
        print(end_t_wind)

# load all the solar data at desired locations since it's a subset of wind time series
# store the data into csv
print(shape(Windspeed['WS'][start_t_wind:end_t_wind,[18,19,20,21,24,25,26,27,30,31,32,33,37,38,39,40]]))
arr_wind = Windspeed['WS'][start_t_wind:end_t_wind,[18,19,20,21,24,25,26,27,30,31,32,33,37,38,39,40]]
DF_hold = pd.DataFrame(arr_wind)
DF_hold.to_csv("D:/Desk_top/Spring_2022/2022_Fall_Courses/COMS_6998_ML&Climate/ML-Climate_ZhiyuanFan/data/Wind_sub.csv")

# open and assess the temperature data

# with open('D:/Desk_top/Spring_2022/2022_Fall_Courses/COMS_6998_ML&Climate/ML-Climate_ZhiyuanFan/data/ERCOT_Temp_Hourly.txt','r') as temp:
#      lines = temp.readlines()
#

# print("The type of lines[1]: {}".format(type(lines[1])))
# lines2 = lines[1].split(" ")
# print("The type of lines2: {}".format(type(lines2)))
# print(lines2)
# lines3 = [float(item) for item in lines2[1:]]
# print(lines3)
# print(len(lines3))

# new_lines = [[]] * 216
# for line in lines[1:]:
#     line2 = line.split(" ")
#     line3 = [float(item) for item in line2[1:]]
#     for index, item in enumerate(line3):
#         new_lines[index] = item
#
#



# temp = np.loadtxt("D:/Desk_top/Spring_2022/2022_Fall_Courses/COMS_6998_ML&Climate/ML-Climate_ZhiyuanFan/data/ERCOT_Temp_Hourly.txt", skiprows=1, dtype='str')
# print(shape(temp))








# print(ds)
#
# for dim in ds.dimensions.values():
#     print(dim)
#
# sample = ds['WS'][:,1]
# print(sample)
#
# print(shape(sample))
