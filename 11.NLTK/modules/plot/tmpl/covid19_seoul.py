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

# matplotlib: plotting with Python.
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager

import folium

# Set the matplotlib color cycle using a seaborn palette.
sns.set_palette('pastel')

# A module for finding, managing, and using fonts across platforms.
mpl.font_manager._rebuild()
sorted([f.name for f in mpl.font_manager.fontManager.ttflist if f.name.startswith('Malgun')])

# 폰트 설정
mpl.rc('font', family='Malgun Gothic')

# 유니코드에서  음수 부호설정
mpl.rc('axes', unicode_minus=False)

# Set Absolute Path
TMPL_PATH = os.path.dirname(os.path.abspath(__file__))
CTPRVN_PATH = os.path.join(
    TMPL_PATH, 'data', 'gisdeveloper.co.kr', 'CTPRVN_202005')
EMD_PATH = os.path.join(TMPL_PATH, 'data', 'gisdeveloper.co.kr', 'EMD_202005')
LI_PATH = os.path.join(TMPL_PATH, 'data', 'gisdeveloper.co.kr', 'LI_202005')
SIG_PATH = os.path.join(TMPL_PATH, 'data', 'gisdeveloper.co.kr', 'SIG_202005')


def main(df, **kwargs):
    baseshp = os.path.join(SIG_PATH, 'SIG.shp')
    basemap = gpd.GeoDataFrame.from_file(baseshp, encoding='euc-kr')

    gdf = basemap.merge(df, on='SIG_CD')

    # https://medium.com/@thlee33/헷갈리는-좌표계-155b4ed1aae
    # 도로명지도는 EPSG 5179(UTM-K)
    # GPS 데이터는 EPSG 4326
    # 지적도는 EPSG 5174일 가능성이 높음

    # 5181이나 5186으로 정의한 후 4326 등으로 변환하여 위치가 잘 맞으면 제대로 정의한 것임.
    # 만약 남북으로 100km 정도 안맞으면 5181(2000년대)–5186(2010년대 이후)간에 바꿔서 다시 정의하면 됨
    # 만약 5186(중부)으로 정의했는데 지도가 배경지도와 비교하여 동서축으로 떨어져 보인다면 5187(동부)임
    #gdf.crs = {'init': "epsg:5186"}

    # 구글지도, 브이월드 지도 등의 배경지도 위에 띄워봤는데 비스듬하게 3백여 미터 안맞는 경우는 EPSG 5174 등의 지역좌표계(베셀타원체)인 경우라고 보여짐.
    #gdf.crs = {'init': "epsg:5174"}

    # EPSG라는 산업표준 좌표계 코드는 4326이고, GPS 기본 좌표계이기도 함.
    gdf = gdf.to_crs(epsg=4326)
    geojson = gdf.to_json()

    # gdf.to_file('./assets/json/abc.geojson', driver='GeoJSON')

    # fig = plt.figure(figsize=figsize)
    # fig.suptitle('대한민국', fontsize=20)

    # ax = plt.subplot(1, 1, 1)
    # ax.set_axis_off()

    # divider = make_axes_locatable(ax)
    # cax = divider.append_axes("right", size="5%", pad=0.1)

    # ax = gdf.plot(column='인구수', legend=True, cmap='OrRd', edgecolor='k', linewidth=.1)

    # gdf.plot(column='인구수', ax=ax, legend=True,
    #          cmap='OrRd', edgecolor='k', linewidth=.1)

    # plt.show()

    m = folium.Map(
        location=[37.5502, 126.982],
        tiles='cartodbpositron',  # Stamen Toner, cartodbpositron
        zoom_start=11
    )

    # folium.GeoJson(geojson).add_to(m)
    folium.GeoJson(geojson).add_to(m)

    # 'black', ‘BuGn’, ‘BuPu’, ‘GnBu’, ‘OrRd’, ‘PuBu’, ‘PuBuGn’, ‘PuRd’, ‘RdPu’, ‘YlGn’, ‘YlGnBu’, ‘YlOrBr’, and ‘YlOrRd’.
    # m.choropleth(
    #     geo_data=gdf_json,
    #     data=gdf['인구수'],
    #     # key_on='feature.id',
    #     key_on='properties.SIG_KOR_NM',
    #     # key_on='properties.SIG_CD',
    #     columns=[gdf.index, gdf['인구수']],
    #     fill_color='YlGnBu',
    #     # fill_opacity=0,
    #     # line_opacity=0.2,
    #     # tooltip=folium.features.GeoJsonTooltip(
    #     #     fields=['시군구명','인구수'],
    #     #     aliases=['Neighborhood: ','Resident foreign population in %: '],
    #     #     style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
    #     # ),
    # )

    return m


def choropleth(df, column='', figsize=(15, 15)):
    baseshp = os.path.join(SIG_PATH, 'SIG.shp')
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
