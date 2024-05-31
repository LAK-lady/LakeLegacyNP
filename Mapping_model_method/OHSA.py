# 4. Optimized hot spot analysis program - alternative spatial mapping model

## Step 1. import dependent packages and set environment settings

print("Import system modules...")
import arcpy, os, sys #needed for mapping in ArcGIS, must have ArcGIS licensed software on local computer
import request, zipfile #needed to download zip files from url
from io import BytesIO #needearcd to extract files from zip file
import pandas #needed to filter data
import csv #needed to read csv files
print("System modules imported.")

print("Setting environment and properties...")
cwd = os.getcwd() #retrieves current working directory
print(cwd)
folder_path = "C:\ARCGIS" #specify folder path BEFORE running code
os.chdir(folder_path) #change the working directory to the folder you choose
print(cwd) #verify current working directory 

print("creating a local file geodatabase as workspace...")
arcpy.management.CreateFileGDB("C:/ARCGIS/Legacy_Nutrient_OSHA.gdb, #out_folder_path = folder where the file geodatabase will be created
                               out_name, {out_version})
arcpy.env.workspace = "C:\ARCGIS\Legacy_Nutrient_OSHA.gdb" 
print("workspace set.")

arcpy.env.overwriteOutput = True #sets the property to overwrite existing output, by default
print("Environment properties set.")

## Step 2. load dependent data and reformat as needed:

print("downloading NHD zipfiles...")
NHD_url1=https://dmap-data-commons-ow.s3.amazonaws.com/NHDPlusV21/Data/NHDPlusMS/NHDPlus07/NHDPlusV21_MS_07_NHDSnapshotFGDB_08.7z # data source = U.S. Environmental Protection Agency, National Hydrography Dataset Version 2
req1 = requests.get(NHD_url1) #retrieves the zip file using url
filename = url.split('/')[-1] #retrieves the file name from the url
with open (filename, 'wb') as output_file: #writes the file to the local file system
    output_file.write(req1.content)
zipfile= zipfile.ZipFile(BytesIO(req1.content))
zipfile.extractall('C:\ARCGIS\Legacy_Nutrient_OSHA.gdb') #extract all data to geodatabase

NHD_url2=https://dmap-data-commons-ow.s3.amazonaws.com/NHDPlusV21/Data/NHDPlusMS/NHDPlus07/NHDPlusV21_MS_07_WBDSnapshot_03.7z
req2 = requests.get(NHD_url2) #retrieves the zip file using url
filename = url.split('/')[-1] #retrieves the file name from the url
with open (filename, 'wb') as output_file: #writes the file to the local file system
    output_file.write(req2.content)
zipfile= zipfile.ZipFile(BytesIO(req2.content))
zipfile.extractall('C:\ARCGIS\Legacy_Nutrient_OSHA.gdb') #extract all data to geodatabase
print("NHD files unzipped to gdb.")


stream_totalP.csv #data source = Wisconsin Department of Natural Resources
resultphyschem.csv #data source = U.S. Geological Survey, National Water Dashboard
station.csv #National Water Quality Monitoring Council, Water Quality Data Portal

## Step 3. Specify region of interest and project all features to same projection:

dataSrc = gpd.read_file('WBD_Subwatershed.shp')
dataSrc[dataSrc['HUC_10']=="0709000206" | == "0709000205"].to_file('HUC10_bound.shp') #filters the data for Lake Mendota and Headwaters (region of interest)

dataSrc = gpd.read_file('NHDWaterbody.shp')
dataSrc[dataSrc['COMID']== "13293262"].to_file('HUC10_bound.shp') #filters the data for Lake Mendota 

NHDFLowline.shp['geometry'].to_crs(epsg=6609) #change coordinate reference system to NAD 1983 (2011) Wisconsin TM (US feet) projection
NHDWaterbody.shp['geometry'].to_crs(epsg=6609)#change coordinate reference system to NAD 1983 (2011) Wisconsin TM (US feet) projection
NHDWaterbody.shp['geometry'].to_crs(epsg=6609)#change coordinate reference system to NAD 1983 (2011) Wisconsin TM (US feet) projection

NHDFlowline #clips streams to HUC 10 

## Step 4a) Merge stream P data files: 

left= stream_totalP.csv #data source = Wisconsin Department of Natural Resources
right= resultphyschem.csv #data source = U.S. Geological Survey, National Water Dashboard
pd.merge(left, right, on="MonitoringLocationIdentifier")

Stream_TotalP_cleaned.csv #output data file

## Step 4b) Map the stream P data to the site data:

print("merging the stream total P data and stream monitoring site data...")
left=station.csv #location of monitoring stations
right=Stream_TotalP_cleaned.csv #stream total P concentration measurements
pd.merge(left, right, on="MonitoringLocationIdentifier") #creates a one to many join (i.e., many stream P observations for a single monitoring station)
print("data files merged.")

print("creating new feature class...")
rcpy.management.CreateFeatureclass("C:\ARCGIS\Legacy_Nutrient_OSHA.gdb", #out_path = where to house the new feature class
                                   "Stream_TotalP_mapped.shp", #out_name = the name of the new feature class
                                   )

## Step 4c) Run the Optimized Hotspot Analysis tool:

ohsa = arcpy.stats.OptimizedHotSpotAnalysis("Stream_TotalP_mapped.shp", # Input_Features= stream total P concentrations mapped to monitoring sites 
                                            "OHS_TotalP_output.shp", #Output_Features= Moran's I value for each monitoring site
                                            "Total_P_Yahara_streams_csv_ResultMeasureValue", #Analysis_Field=Total_P_Yahara_streams_csv_ResultMeasureValue
                                            "COUNT_INCIDENTS_WITHIN_FISHNET_POLYGONS", #Incident_Data_Aggregation_Method
                                            {Bounding_Polygons_Defining_Where_Incidents_Are_Possible}, #keep defaults settings
                                            {Polygons_For_Aggregating_Incidents_Into_Counts}, #keep defaults settings
                                            {Density_Surface}, #keep defaults settings
                                            {Cell_Size}, #keep defaults settings
                                            {DISTANCE_BAND}) #keep defaults settings


## Print out error message if they occur:
except arcpy.ExecuteError:
    # If any error occurred when running the tool, print the messages
    print(arcpy.GetMessages()
