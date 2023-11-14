# Yahara Subwatershed P Export Analysis

This directory contains code for analyzing the phosphorus export of the Lake Mendota, WI watershed. It constructs upstream subwatersheds based on the [HydroGraphs](https://github.com/zavalab/ML/tree/master/HydroGraphs) framework, and uses data from USGS stream monitoring station to calculate the stream export for the years 2013-2021. This directory is structured as follows.

The main directory contains the following files:

 * `watershed_analysis.ipynb` - This notebook contains the primary code for performing the analysis. It loads data from the `yahara_data/` subdirectory, puts the data in the proper format, builds the upstream subwatersheds, and computes the yearly export
 * `HydroGraph_functions.py` - This file is from the HydroGraphs repository, and contains functions for working with the NHDPlusV2 data as graphs
 * `station_data.csv` - This file contains data retrieved from the water quality data portal [here](https://www.waterqualitydata.us/) by searching within Dane County, Wisconsin, in HUC 07090002, using "water" and "Water" as the sample media, and using stream as the site type. Station data was found using the "site data only" option under the advanced search. 
 * `stream_data.csv` - This file contains data retrieved directly from the USGS webiste for each station. Data had to be manually retrieved as tab-separated tables. We retrieved data from 6 sites: 'USGS-05427718', 'USGS-05427850', 'USGS-05427880', 'USGS-05427910','USGS-05427930', and 'USGS-05427948'.
 * `WItofroms.csv` - This file is from the HydroGraphs repository (originally from the NHDPlusV2 dataset) and contains the list of edges for representing (TOCOMID and FROMCOMID) for representing the river system as a graph.

The main directory also contains the following subdirectories:

### `WI`
This directory contains a shapefile of the state of Wisconsin. From the HydroGraphs repository

### `yahara_data`
This directory contains GeoDataFrames (as pickle files) for the geospatial data used in the analysis, including the HUC8, HUC10, and HUC12 watersheds, the catchments, the lakes and rivers, land cover data, and the county-specific data on internally drained basins in Dane County. This data can be created using scripts in the `large_file_curation` subdirectory

### `large_file_curation`
This directory contains scripts for creating the data in `yahara_data`. Much of this data comes from the NHDPlusV2 dataset and the Watershed Boundary Datasets. These datasets can be quite large, and so are not provided in this repository. Instead, python scripts are provided which can be used to download the data of interest. 

* `get_and_unpack_data.py` - This script downloads the different datasets required for the above analysis, unpacks the compressed data, and then deletes the compressed folders. This script is the first script to call in this directory

    * The data downloaded includes the [NHDPlusV2 datasets](https://www.epa.gov/waterdata/get-nhdplus-national-hydrography-dataset-plus-data), the [Watershed Boundary Datasets](https://apps.nationalmap.gov/downloader/#/), the [Wiscland2 landcover dataset](https://dnr.wisconsin.gov/maps/WISCLAND), and [county-specific data on internally drained basins and hydrologic units](https://gis-countyofdane.opendata.arcgis.com/pages/water-resources)
* `build_base_dataframes.py` - This script takes the NHDPlusV2 and Watershed Boundary Datasets and adds HUC8/10/12 identifiers. This is useful later for constructing the data in the `yahara_data` subdirectory. 
* `build_yahara_data.ipynb` - This notebook constructs the dataframes in the `yahara_data/` subdirectory.
* In addition there are also the following subdirectories: 
    
    * `DaneCountyData` - location where the county specific data on internally drained basins is unpacked. 
    * `Landcover` - location where the Wiscland2 dataset is unpacked. It also contains the script `landcover_raster_to_shp.py` for converting the raster file into a shapefile, and the script `landcover_assignments.py` which assigns catchment codes to all landcover polygons.
    * `Watersheds` - location where the NHDPlusV2 and Watershed Boundary Datasets are unpacked. 
