''' example of time series code '''

from netCDF4 import Dataset, num2date
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

my_longitude, my_latitude = -9.1, 53.2


# This is an online file with approximately one month of data
f = "http://milas.marine.ie/thredds/dodsC/IMI_ROMS_HYDRO/GALWAY_BAY_NATIVE_70M_8L_1H/COMBINED_AGGREGATION"

def gregorian_to_datetime(timelist):
    return [datetime(i.year, i.month, i.day, i.hour) for i in timelist]

with Dataset(f, 'r') as nc:
    # Read time
    time = num2date(nc.variables['ocean_time'][:], 
                    nc.variables['ocean_time'].units)
    
    lon = nc.variables['lon_rho'][:]; lon = lon[0,:] # Longitude
    lat = nc.variables['lat_rho'][:]; lat = lat[:,0]  # Latitude
    
    index_longitude = np.argmin( abs(lon - my_longitude) ) # get closest longitude
    index_latitude = np.argmin( abs(lat - my_latitude) ) # get closest latitude
    
    
    # Sea level
    sea_level = nc.variables['zeta'][:, index_latitude, index_longitude]
    
    # temperature
    temperature = nc.variables['temp'][:, -1, index_latitude, index_longitude] # '-1' for surface depth
    
time = gregorian_to_datetime(time)
plt.plot(time, temperature)
plt.xlim((time[0], time[-1]))
plt.xticks(rotation=45, fontsize=12)
plt.ylim((11,20))
plt.title



