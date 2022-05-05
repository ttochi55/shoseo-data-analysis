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

# A Python script that converts a Shapefile, GeoJSON, or CSV to an equal area cartogram SVG or GeoJSON
# https://github.com/LokiTechnologies/EqualAreaCartogram
from eqcart import Cartogram

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


def world():
    countries = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
    ax = countries.plot(column="continent", legend=True,
                        categorical=True, figsize=(18, 9))
    ax.set_title("세계 지도")
    ax.set_axis_off()
    plt.show()


def ctp_sig(figsize=(15, 15)):
    ctp_shp = './data/shp/CTPRVN_202005/CTPRVN.shp'
    ctp_gdf = gpd.GeoDataFrame.from_file(ctp_shp, encoding='euc-kr')
    ctp_gdf.crs = "epsg:5179"

    sig_shp = './data/shp/SIG_202005/SIG.shp'
    sig_gdf = gpd.GeoDataFrame.from_file(sig_shp, encoding='euc-kr')
    sig_gdf.crs = "epsg:5179"

    fig = plt.figure(figsize=figsize)
    fig.suptitle('대한민국', fontsize=20)

    ax = plt.subplot(1, 1, 1)
    sig_gdf.plot(column='SIG_KOR_NM', ax=ax)
    ctp_gdf.geometry.boundary.plot(
        color=None, edgecolor='w', linewidth=1, ax=ax)
    ax.set_axis_off()

    plt.show()


# 시도: ['CTPRVN_CD', 'CTP_ENG_NM', 'CTP_KOR_NM', 'geometry']
def ctp(figsize=(15, 15)):
    shp = './data/shp/CTPRVN_202005/CTPRVN.shp'
    gdf = gpd.GeoDataFrame.from_file(shp, encoding='euc-kr')
    gdf.crs = "epsg:5179"

    ax = gdf.plot(column="CTP_KOR_NM", figsize=figsize)
    ax.set_title('대한민국', fontsize=20)
    ax.set_axis_off()

    plt.show()


# 시군구: ['SIG_CD', 'SIG_ENG_NM', 'SIG_KOR_NM', 'geometry']
def sig(figsize=(15, 15)):
    shp = './data/shp/SIG_202005/SIG.shp'
    gdf = gpd.GeoDataFrame.from_file(shp, encoding='euc-kr')
    gdf.crs = "epsg:5179"

    ax = gdf.plot(column="SIG_KOR_NM", figsize=figsize)
    ax.set_title('대한민국', fontsize=20)
    ax.set_axis_off()

    plt.show()


# 읍면동: ['EMD_CD', 'EMD_ENG_NM', 'EMD_KOR_NM', 'geometry']
def emd(figsize=(15, 15)):
    shp = './data/shp/EMD_202005/EMD.shp'
    gdf = gpd.GeoDataFrame.from_file(shp, encoding='euc-kr')
    gdf.crs = "epsg:5179"

    ax = gdf.plot(column="EMD_KOR_NM", figsize=figsize)
    ax.set_title('대한민국', fontsize=20)
    ax.set_axis_off()

    plt.show()


# 리: ['LI_CD', 'LI_ENG_NM', 'LI_KOR_NM', 'geometry']
def li(figsize=(15, 15)):
    shp = './data/shp/LI_202005/LI.shp'
    gdf = gpd.GeoDataFrame.from_file(shp, encoding='euc-kr')
    gdf.crs = "epsg:5179"

    ax = gdf.plot(column="LI_KOR_NM", figsize=figsize)
    ax.set_title('대한민국', fontsize=20)
    ax.set_axis_off()

    plt.show()


if __name__ == "__main__":
    main()
