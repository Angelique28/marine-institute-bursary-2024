from netCDF4 import Dataset, num2date
from gsw import distance
import numpy as np

def find_ROMS_indexes(lon_ROMS, lat_ROMS, my_lon, my_lat):
    ''' This function find the longitude and latitude indexes in a ROMS grid
    that are closest to our site of interest '''
    
    # Get size of ROMS grid
    M, L = lon_ROMS.shape

    # The function that calculates distances expects flattened (1-dimensional) arrays
    lon1D = np.ndarray.flatten(lon_ROMS)
    lat1D = np.ndarray.flatten(lat_ROMS)

    
    mylon = my_lon * np.ones_like(lon1D)
    mylat  = my_lat * np.ones_like(lat1D)
        
    nlon = np.stack((lon1D, mylon), axis=1)
    nlat = np.stack((lat1D, mylat), axis=1)
        
    D = distance(nlon, nlat, axis=1)

    w = np.argmin(D)
    
    mindist = D[w][0]
  
    J, I = np.unravel_index(w, (M, L), order='C')
    
    nearest_lon = lon_ROMS[J, I]
    nearest_lat = lat_ROMS[J, I]
    
    print(f'Nearest ROMS site is %.4f, %.4f' % (nearest_lat, nearest_lon))
    print(f'Distance is %d m' % round(mindist))
    
    
    return J, I
    

# Your site of interest
latitude, longitude = 54.59672, -9.28952

# This is a ROMS file
f = r"O:\ROMS\OUTPUT\NE_Atlantic\SNAPSHOT_1HOUR\2020\NEATL_2020010103.nc"

# Open ROMS file
with Dataset(f, 'r') as nc:
    # Longitude
    lon = nc.variables['lon_rho'][:]
    # Latitude
    lat = nc.variables['lat_rho'][:]
    
J, I = find_ROMS_indexes(lon, lat, longitude, latitude)
