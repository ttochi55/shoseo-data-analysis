# import os
# import sys
from matplotlib.pyplot import legend
import numpy as np
import pandas as pd
# import time
# import json
# import re

# A Fast, Extensible Progress Bar for Python and CLI
from tqdm import tqdm

# Statistical data visualization using matplotlib.
import seaborn as sns

# Fiona reads and writes geographic data files and thereby helps Python programmers integrate geographic information systems with other computer systems.
import fiona
from fiona.crs import from_epsg

# Python interface to PROJ (cartographic projections and coordinate transformations library).
import pyproj

# GeoPandas is an open source project to make working with geospatial data in python easier.
import geopandas as gpd

# geoplot is a geospatial data visualization library designed for data scientists and geospatial analysts that just want to get things done.
import geoplot as gplt
import geoplot.crs as gcrs

# Plot population estimates with an accurate legend
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Python Data. Leaflet.js Maps.
import folium

# matplotlib: plotting with Python.
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager

# Set the matplotlib color cycle using a seaborn palette.
sns.set_palette('pastel')

# A module for finding, managing, and using fonts across platforms.
mpl.font_manager._rebuild()
sorted([f.name for f in mpl.font_manager.fontManager.ttflist if f.name.startswith('Malgun')])

# 폰트 설정
mpl.rc('font', family='Malgun Gothic')

# 유니코드에서  음수 부호설정
mpl.rc('axes', unicode_minus=False)


def main():
    pass


def choropleth(df, column='', figsize=(15, 15)):

    sig_gdf = gpd.GeoDataFrame.from_file(
        './data/shp/SIG_202005/SIG.shp', encoding='euc-kr')
    # gdf = gpd.GeoDataFrame(df)
    # gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['SIG_X'], df['SIG_Y']))
    gdf = sig_gdf.merge(df, on='SIG_CD')
    gdf.crs = "epsg:5179"

    # gdf = gpd.GeoDataFrame.from_file(shp, encoding='euc-kr')

    fig = plt.figure(figsize=figsize)
    fig.suptitle('대한민국', fontsize=20)

    ax = plt.subplot(1, 1, 1)
    ax.set_axis_off()

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)

    gdf.plot(column=column, ax=ax, legend=True,
             cax=cax, cmap='OrRd', edgecolor='k', linewidth=.1)

    # ctp_shp = './data/shp/CTPRVN_202005/CTPRVN.shp'
    # ctp_gdf = gpd.GeoDataFrame.from_file(ctp_shp, encoding='euc-kr')
    # ctp_gdf.crs = "epsg:5179"
    # ctp_gdf.geometry.boundary.plot(
    #     ax=ax, color=None, edgecolor='w', linewidth=1)

    plt.show()


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


if __name__ == "__main__":
    main()
