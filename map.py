import sys, os
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import datasets
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt

def draw_map(routeLog, coordsList, dest):
    world = gpd.read_file(datasets.get_path('naturalearth_lowres'))

    points = [{"name": log["ip"], "geometry": Point(coords["lat"], coords["lon"])}
                                     for log, coords in zip(routeLog, coordsList)]
    gdf_points  = GeoDataFrame(points, crs="EPSG:4326")

    ax = world.plot(figsize=(10,10))

    gdf_points.plot(ax=ax, color="red", markersize=50)

    plt.title(dest)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    for idx, row in gdf_points.iterrows():
        plt.annotate(row['name'], xy=(row['geometry'].x, row['geometry'].y), xytext=(3, 3), textcoords='offset points')

    plt.show()