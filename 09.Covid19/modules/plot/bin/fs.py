# conda install lxml

import numpy as np
import pandas as pd

# Fiona reads and writes geographic data files and thereby helps Python programmers integrate geographic information systems with other computer systems.
import fiona
from fiona.crs import from_epsg

# Python interface to PROJ (cartographic projections and coordinate transformations library).
import pyproj

# GeoPandas is an open source project to make working with geospatial data in python easier.
import geopandas as gpd

# A Python script that converts a Shapefile, GeoJSON, or CSV to an equal area cartogram SVG or GeoJSON
# https://github.com/LokiTechnologies/EqualAreaCartogram
from eqcart import Cartogram


def main():
    pass


def to_shp(df, output):
    shp = './data/shp/SIG_202005/SIG.shp'
    gdf = gpd.GeoDataFrame.from_file(shp, encoding='euc-kr')
    merged = gdf.merge(df, on='SIG_CD')
    merged.crs = 'epsg:5179'
    merged.to_file(output, encoding='euc-kr')


def to_geojson(df, output):
    shp = './data/shp/SIG_202005/SIG.shp'
    gdf = gpd.GeoDataFrame.from_file(shp, encoding='euc-kr')
    merged = gdf.merge(df, on='SIG_CD')
    merged.crs = 'epsg:5179'
    merged.to_file(output, driver='GeoJSON')


def to_hex_svg(filepath, output, id_col, num_x_grid, num_y_grid):
    # filepath can be the location of a GeoJSON, SHP, CSV, or Excel File
    # num_x_grid, num_y_grid: reduced grid width and height to make map more dense
    cart = Cartogram(filepath,
                     id_col,
                     num_x_grid,
                     num_y_grid)

    cart.make_hex_svg(output)


def to_hex_geojson(filepath, output, id_col, num_x_grid, num_y_grid):
    # filepath can be the location of a GeoJSON, SHP, CSV, or Excel File
    # num_x_grid, num_y_grid: reduced grid width and height to make map more dense
    cart = Cartogram(filepath,
                     id_col,
                     num_x_grid,
                     num_y_grid)

    cart.make_hex_geojson(output)


if __name__ == "__main__":
    main()
