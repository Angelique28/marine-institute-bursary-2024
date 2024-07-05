from netCDF4 import Dataset, num2date
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

my_longitude, my_latitude = -9.1, 53.2

# File name
file = r"O:\ROMS\OUTPUT\Bantry_Bay\AVERAGE_DAILY\2016\BANT_2016120112.nc"

def gregorian_to_datetime(timelist):
    return [datetime(i.year, i.month, i.day, i.hour) for i in timelist]

with Dataset(file, 'r') as nc:
    lon = nc.variables['lon_rho'][:] # Longitude
    lat = nc.variables['lat_rho'][:] # Latitude
    

    time = num2date(nc.variables['ocean_time'][:],
                    nc.variables['ocean_time'].units) # Time
    
    print(nc.variables['temp'].shape)
    print(nc.variables['temp'].dimensions)
    print(nc.variables['temp'][0,:,0,0])
    
    depths = nc.variables['s_rho'][:]
    print("Depths:", depths)

    
    print(nc.variables['salt'].shape)
    print(nc.variables['salt'].dimensions)
    
    # Temperature has dimensions of time, depth (s_rho), latitude (eta_rho) and longitude (xi_rho)
    temperature = nc.variables['temp'][:]
    # Salinity has dimensions of time, depth (s_rho), latitude (eta_rho) and longitude (xi_rho)
    salinity = nc.variables['salt'][:]
    
    
# Map Temperature
fig, ax = plt.subplots(1)    
plot = ax.pcolor(lon, lat, temperature[0, 19, :, :], vmin=9, vmax=13)
colorbar = fig.colorbar(plot, ax=ax, label='(°C)')
ax.set_title('Bantry Bay December 2016 - ROMS')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')



# Map Salinity
# =============================================================================
# fig, ax = plt.subplots(1)
# plot = ax.pcolor(lon, lat, salinity[0, 19, :, :], vmin=34, vmax=35.75)
# colorbar = fig.colorbar(plot, ax=ax, label='(psu)')
# ax.set_title('Bantry Bay December 2016 - ROMS')
# ax.set_xlabel('Longitude')
# ax.set_ylabel('Latitude')
# =============================================================================
