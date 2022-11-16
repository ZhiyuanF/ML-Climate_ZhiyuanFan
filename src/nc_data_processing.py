# process the raw data files (.nc) that contain hourly data for Texas
# the package used for .nc file processing is net CDF4

# import packages
import netCDF4 as nc
import numpy as np
from numpy import shape

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

# open and assess the temperature data

# with open('D:/Desk_top/Spring_2022/2022_Fall_Courses/COMS_6998_ML&Climate/ML-Climate_ZhiyuanFan/data/ERCOT_Temp_Hourly.txt','r') as temp:
#      lines = temp.readlines()
#
# print(shape(lines))
# # note that the temperature data has the same dimension of the wind data
# print(type(lines))
#
# print(lines[1])
#
temp = np.loadtxt("D:/Desk_top/Spring_2022/2022_Fall_Courses/COMS_6998_ML&Climate/ML-Climate_ZhiyuanFan/data/ERCOT_Temp_Hourly.txt", skiprows=1, dtype='str')
print(shape(temp))








# print(ds)
#
# for dim in ds.dimensions.values():
#     print(dim)
#
# sample = ds['WS'][:,1]
# print(sample)
#
# print(shape(sample))
