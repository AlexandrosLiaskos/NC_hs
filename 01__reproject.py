'''
pip install xarray rioxarray netCDF4 h5netcdf
'''

import xarray
import rioxarray

input_file = input("Enter the path to the input NetCDF file (.nc): ")
output_file = input("Enter the path for the output NetCDF file (.nc): ")

rds = xarray.open_dataset(input_file).rio.set_spatial_dims(x_dim="rlon", y_dim="rlat")
proj4_string = rds.projection_3.attrs["proj4"]
rds.rio.write_crs(proj4_string, inplace=True)
reprojected = rds.rio.reproject("EPSG:4326")
reprojected.to_netcdf(output_file)
