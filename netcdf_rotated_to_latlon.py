from netCDF4 import Dataset
import os
import math

file_dir = os.path.dirname(os.path.abspath('__file__'))
file_name = "filename.nc"

data = Dataset(file_name)
print(data.variables.keys())

lat = data.variables['lat']
lon = data.variables['lon']

lat_bnds = data.variables['lat_bnds']
lon_bnds = data.variables['lon_bnds']

lat_location = 52.5162   # Latitude (WGS 84)
lon_location = 13.3778   # Longitude (WGS 84)

min_dist = math.inf
min_i = None
min_j = None
for i in range(412):
    for j in range(424):
        dist = (lat[i][j] - lat_location)**2 + (lon[i][j] - lon_location)**2
        if dist < min_dist:
            min_dist = dist
            min_i = i
            min_j = j

print(min_i, min_j, lat[min_i][min_j], lon[min_i][min_j])
print(lat_bnds[min_i][min_j])
print(lon_bnds[min_i][min_j])
