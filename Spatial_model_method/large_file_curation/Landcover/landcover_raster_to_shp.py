import rasterio 
import rasterio.warp
import rasterio.features
from rasterio.features import shapes
import os
from shapely.geometry import shape
import geopandas as gpd

path = os.getcwd()

print("RUNNING RASTER")
with rasterio.Env():
    with rasterio.open("wiscland2_level1.tif") as src:
        mask = src.dataset_mask()
        image = src.read(1)
        results = ( {"properties": {"raster_val": v}, 'geometry': s} for i, (s, v) in enumerate( shapes(image, mask=mask, transform = src.transform)))


geoms = list(results)
print(geoms[0])

print("CONVERTING TO GDF")
gdf = gpd.GeoDataFrame.from_features(geoms)
print("Formed GeoDataFrame")
gdf = gdf.set_crs("EPSG:3071")
gdf = gdf.to_crs("EPSG:4326")
gdf.to_pickle(path + "/raster_to_gdf.df")
