''' Example: how to read NetCDF '''

from netCDF4 import Dataset, num2date
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

my_longitude, my_latitude = -9.1, 53.2

# File name
file = r"O:\ROMS\OUTPUT\Galway_Bay\AVERAGE\2012-2021\GALWAY-BAY-AVG-20220301.nc"

def gregorian_to_datetime(timelist):
    return [datetime(i.year, i.month, i.day, i.hour) for i in timelist]

with Dataset(file, 'r') as nc:
    lon = nc.variables['lon_rho'][:] # Longitude
    lat = nc.variables['lat_rho'][:] # Latitude
    

    time = num2date(nc.variables['ocean_time'][:],
                    nc.variables['ocean_time'].units) # Time
    
    print(nc.variables['temp'].shape)
    print(nc.variables['temp'].dimensions)

    
    print(nc.variables['salt'].shape)
    print(nc.variables['salt'].dimensions)
    
    # Temperature has dimensions of time, depth (s_rho), latitude (eta_rho) and longitude (xi_rho)
    temperature = nc.variables['temp'][:]
    # Salinity has dimensions of time, depth (s_rho), latitude (eta_rho) and longitude (xi_rho)
    salinity = nc.variables['salt'][:]
    
    
# Map Temperature
fig, ax = plt.subplots(1)    
plot = ax.pcolor(lon, lat, temperature[0, 7, :, :], vmin=6, vmax=10)
colorbar = fig.colorbar(plot, ax=ax, label='(°C)')
ax.set_title('Galway Bay June 2022-ROMS')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')




# Map Salinity
# =============================================================================
# fig, ax = plt.subplots(1)
# plot = ax.pcolor(lon, lat, salinity[0, 7, :, :], vmin=24, vmax=34)
# colorbar = fig.colorbar(plot, ax=ax, label='(psu)')
# ax.set_title('Galway Bay September 2016 - ROMS')
# ax.set_xlabel('Longitude')
# ax.set_ylabel('Latitude')
# =============================================================================


'''''''combining multiple data'''''''''''''
# Define the file paths
# =============================================================================
# file_paths = [f"O:/ROMS/OUTPUT/Galway_Bay/AVERAGE/2012-2021/GALWAY-BAY-AVG-202203{str(i).zfill(2)}.nc" for i in range(1,31)]
# 
# def gregorian_to_datetime(timelist):
#     return [datetime(i.year, i.month, i.day, i.hour) for i in timelist]
# 
# # Initialize lists to hold time and data arrays
# time_data = []
# temperature_data = []
# 
# # Loop through each file and read the data
# for file in file_paths:
#     with Dataset(file, 'r') as nc:
#         lon = nc.variables['lon_rho'][:] # Longitude
#         lat = nc.variables['lat_rho'][:] # Latitude
#         
# 
#         time = num2date(nc.variables['ocean_time'][:],
#                         nc.variables['ocean_time'].units) # Time
#         
#         # Temperature has dimensions of time, depth (s_rho), latitude (eta_rho) and longitude (xi_rho)
#         temperature = nc.variables['temp'][:]
#         # Salinity has dimensions of time, depth (s_rho), latitude (eta_rho) and longitude (xi_rho)
#         salinity = nc.variables['salt'][:]
#         
#         
#         # Append to the list
#         time_data.append(time)
#         temperature_data.append(temperature)
# 
# # Concatenate the data along the time dimension
# time_data = np.concatenate(time_data)
# temperature_data = np.concatenate(temperature_data, axis=0)
# 
# # Now you can work with the combined dataset
# print(f"Time Data Shape: {time_data.shape}")
# print(f"Temperature Data Shape: {temperature_data.shape}")
# 
# 
# # Map Temperature
# fig, ax = plt.subplots(1)    
# plot = ax.pcolor(lon, lat, temperature[0, 7, :, :], vmin=7, vmax=15)
# colorbar = fig.colorbar(plot, ax=ax, label='(°C)')
# ax.set_title('Galway Bay March 2022')
# ax.set_xlabel('Longitude')
# ax.set_ylabel('Latitude')
# 
# 
# 













