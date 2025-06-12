# Guide

## Clone the Reepository
git clone https://github.com/AlexandrosLiaskos/NC_hs.git

## Start the virtual environment
source venv/bin/activate

## Run the reproject script (Add the input file path of the nc and the desired output)
python 01__reproject.py

## Run the conversion to geojson with the hs variable (Add the input fiele path of the nc file)
python 02__extract_hs_to_geojson.py
