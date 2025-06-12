'''
pip install geojson
'''

import xarray as xr
import numpy as np
import geojson
from geojson import Feature, Point, FeatureCollection

file_path = input("Please enter the path to the NetCDF file: ")
ds = xr.open_dataset(file_path)

hs = ds['hs']
x = ds['x']
y = ds['y']

features = []

hs_data = hs.isel(time=0).values

x_data = x.values
y_data = y.values

if len(x_data.shape) == 1 and len(y_data.shape) == 1:
    x_grid, y_grid = np.meshgrid(x_data, y_data)
else:
    x_grid = x_data
    y_grid = y_data

for i in range(hs_data.shape[0]):
    for j in range(hs_data.shape[1]):
        if not np.isnan(hs_data[i, j]):
            point = Point((x_grid[i, j], y_grid[i, j]))
            feature = Feature(geometry=point, properties={'hs': float(hs_data[i, j])})
            features.append(feature)

collection = FeatureCollection(features)
with open('hs.geojson', 'w') as f:
    geojson.dump(collection, f, indent=2)
