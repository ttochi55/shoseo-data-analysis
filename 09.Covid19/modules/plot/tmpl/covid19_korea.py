import os
import sys
import numpy as np
import pandas as pd
import time
import json
import re

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


def main(df, column='', figsize=(15, 15)):
    baseshp = './data/gisdeveloper.co.kr/SIG_202005/SIG.shp'
    basemap = gpd.GeoDataFrame.from_file(baseshp, encoding='euc-kr')

    gdf = basemap.merge(df, on='SIG_CD')
    gdf.crs = {'init': "epsg:5179"}

    fig = plt.figure(figsize=figsize)
    fig.suptitle('대한민국', fontsize=20)

    ax = plt.subplot(1, 1, 1)
    ax.set_axis_off()

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)

    gdf.plot(column=column, ax=ax, legend=True,
             cax=cax, cmap='OrRd', edgecolor='k', linewidth=.1)

    # layershp = './data/shp/CTPRVN_202005/CTPRVN.shp'
    # layergdf = gpd.GeoDataFrame.from_file(layershp, encoding='euc-kr')
    # layergdf.crs = "epsg:5179"
    # layergdf.geometry.boundary.plot(ax=ax, color=None, edgecolor='w', linewidth=1)

    plt.show()


if __name__ == "__main__":
    main()
