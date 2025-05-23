import warnings
import pandas as pd
import numpy as np
import geopandas as gpd
import pandas as pd
from tqdm import tqdm
from HydroGraph_functions import *
import os

warnings.filterwarnings('ignore')

path = os.getcwd()

print("Loading in Data")

# Load in the shape file for Wisconsin
WI    = gpd.GeoDataFrame.from_file(path + "/../WI/WI.shp")

# Load in the shape files for WBD, NHDFlowlines, and NHDWatgebodies for HUC2 watershed 04
HUC84   = gpd.GeoDataFrame.from_file(path + "/Watersheds/Watershed4/WBDHU8.shp")
HUC104  = gpd.GeoDataFrame.from_file(path + "/Watersheds/Watershed4/WBDHU10.shp")
HUC124  = gpd.GeoDataFrame.from_file(path + "/Watersheds/Watershed4/WBDHU12.shp")
lakes4  = gpd.GeoDataFrame.from_file(path + "/Watersheds/Watershed4/NHDWaterbody.shp")
rivers4 = gpd.GeoDataFrame.from_file(path + "/Watersheds/Watershed4/NHDFlowline.shp")
catch4  = gpd.GeoDataFrame.from_file(path + "/Watersheds/Watershed4/Catchment.shp")

# Load in the shape files for WBD, NHDFlowlines, and NHDWatgebodies for HUC2 watershed 07
HUC87   = gpd.GeoDataFrame.from_file(path + "/Watersheds/Watershed7/WBDHU8.shp")
HUC107  = gpd.GeoDataFrame.from_file(path + "/Watersheds/Watershed7/WBDHU10.shp")
HUC127  = gpd.GeoDataFrame.from_file(path + "/Watersheds/Watershed7/WBDHU12.shp")
lakes7  = gpd.GeoDataFrame.from_file(path + "/Watersheds/Watershed7/NHDWaterbody.shp")
rivers7 = gpd.GeoDataFrame.from_file(path + "/Watersheds/Watershed7/NHDFlowline.shp")
catch7  = gpd.GeoDataFrame.from_file(path + "/Watersheds/Watershed7/Catchment.shp")

# Add HUC2 code to lakes and rivers; this will be used to remove any objects outside of their HUCs later
lakes4['huc2']  = 4
rivers4['huc2'] = 4
catch4['huc2'] = 4

lakes7['huc2']  = 7
rivers7['huc2'] = 7
catch7['huc2'] = 7

print("Setting same EPSG code")


# Set the EPSG code to be the same for all shapefiles. This ensures better accuracy when calling "overlay" later
WI = WI.to_crs("EPSG:4326")

HUC84   = HUC84.to_crs("EPSG:4326")
HUC104  = HUC104.to_crs("EPSG:4326")
HUC124  = HUC124.to_crs("EPSG:4326")
lakes4  = lakes4.to_crs("EPSG:4326")
rivers4 = rivers4.to_crs("EPSG:4326")
catch4  = catch4.to_crs("EPSG:4326")

HUC87   = HUC87.to_crs("EPSG:4326")
HUC107  = HUC107.to_crs("EPSG:4326")
HUC127  = HUC127.to_crs("EPSG:4326")
lakes7  = lakes7.to_crs("EPSG:4326")
rivers7 = rivers7.to_crs("EPSG:4326")
catch7  = catch7.to_crs("EPSG:4326")

# Remove the Great Lakes
lakes4 = lakes4[(lakes4.COMID != 904140243) & (lakes4.COMID != 904140248)].copy()
lakes7 = lakes7[(lakes7.COMID != 904140243) & (lakes7.COMID != 904140248)].copy()

# Remove swamps/marshes
lakes4 = lakes4[lakes4.FTYPE != "SwampMarsh"].copy()
lakes7 = lakes7[lakes7.FTYPE != "SwampMarsh"].copy()

# Reset index
lakes4 = lakes4.reset_index(drop=True)
lakes7 = lakes7.reset_index(drop=True)

# Add a huc indicator column
HUC84, HUC104, HUC124 = add_huc_col_to_hucs(HUC84.copy(), HUC104.copy(), HUC124.copy())
HUC87, HUC107, HUC127 = add_huc_col_to_hucs(HUC87.copy(), HUC107.copy(), HUC127.copy())

HUC8_all   = pd.concat([HUC84, HUC87])
HUC10_all  = pd.concat([HUC104, HUC107])
HUC12_all  = pd.concat([HUC124, HUC127])

HUC8_all  = HUC8_all.reset_index(drop=True)
HUC10_all = HUC10_all.reset_index(drop=True)
HUC12_all = HUC12_all.reset_index(drop=True)

print("Getting WI HUCs")

HUC8  = gpd.overlay(HUC8_all, WI, how="intersection")
HUC8  = HUC8[HUC8_all.columns].copy(deep = True)
print("Done with HUC8")
HUC10 = gpd.overlay(HUC10_all, WI, how="intersection")
HUC10 = HUC10[HUC10_all.columns].copy(deep = True)
print("Done with HUC10")
HUC12 = gpd.overlay(HUC12_all, WI, how="intersection")
HUC12 = HUC12[HUC12_all.columns].copy(deep = True)
print("Done with HUC12")

lakes_all  = pd.concat([lakes4, lakes7])
rivers_all = pd.concat([rivers4, rivers7])
catch_all  = pd.concat([catch4, catch7])

lakes_all  = lakes_all.reset_index(drop=True)
rivers_all = rivers_all.reset_index(drop=True)
catch_all  = catch_all.reset_index(drop=True)

print("Getting WI lakes and rivers")

lakes  = gpd.overlay(lakes_all, WI, how="intersection")
lakes  = lakes[lakes_all.columns].copy(deep = True)
print("Done with lakes")
rivers = gpd.overlay(rivers_all, WI, how="intersection")
rivers = rivers[rivers_all.columns].copy(deep = True)
print("Done with rivers")
catch = gpd.overlay(catch_all, WI, how = "intersection")
catch = catch[catch_all.columns].copy(deep = True)
print("Done with catchments")

print("Adding HUCs to lakes")

# Add the HUC8, HUC10, and HUC12 unit codes to the lakes and rivers
# These are determined by what HUC the centroid of the lake lies in
lakes = add_HUC8(lakes.copy(), HUC8.copy())
lakes = add_HUC10(lakes.copy(), HUC10.copy())
lakes = add_HUC12(lakes.copy(), HUC12.copy())

print("Adding HUCs to rivers")

rivers = add_HUC8(rivers.copy(), HUC8.copy())
rivers = add_HUC10(rivers.copy(), HUC10.copy())
rivers = add_HUC12(rivers.copy(), HUC12.copy())

print("Adding HUCs to catchments")
catch = add_HUC8(catch.copy(), HUC8.copy())
catch = add_HUC10(catch.copy(), HUC10.copy())
catch = add_HUC12(catch.copy(), HUC12.copy())

print("Saving Data")

HUC8.to_pickle(path + "/WIHUC8.df")
HUC10.to_pickle(path + "/WIHUC10.df")
HUC12.to_pickle(path + "/WIHUC12.df")
lakes.to_pickle(path + "/WILakes.df")
rivers.to_pickle(path + "/WIRivers.df")
catch.to_pickle(path + "/WICatch.df")

print("Done forming base dataframes")