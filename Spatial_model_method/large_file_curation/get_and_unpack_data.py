import wget
import os
import zipfile
import py7zr
import shutil

path = os.getcwd()

# Download the landcover data: https://p.widencdn.net/lkfpeb/wiscland2_landcover

landcover_url = "https://p.widencdn.net/lkfpeb/wiscland2_landcover"
wget.download(landcover_url, out = path)

landcover_path = path + "/Landcover/"

with zipfile.ZipFile("wiscland2_landcover.zip", 'r') as zipObj:
    zipObj.extract("wiscland2/wiscland2_dataset/level1.zip", path = path)

with zipfile.ZipFile(path + "/wiscland2/wiscland2_dataset/level1.zip", 'r') as zipObj:
    zipObj.extract("level1/wiscland2_level1.tif", path = landcover_path)

os.rename(landcover_path + "level1/wiscland2_level1.tif", landcover_path + "wiscland2_level1.tif")

os.remove(path + "/wiscland2_landcover.zip")
shutil.rmtree(landcover_path + "level1")

# Download HydrologicUnits Data
HU_url = "https://dciimages.countyofdane.com/WaterResources/HydrologicUnits.zip"
wget.download(HU_url, out = path)

county_path = path + "/DaneCountyData/"

with zipfile.ZipFile("HydrologicUnits.zip", 'r') as zipObj:
    zipObj.extract("HydrologicUnits.shx", path = county_path)
    zipObj.extract("HydrologicUnits.cpg", path = county_path)
    zipObj.extract("HydrologicUnits.dbf", path = county_path)
    zipObj.extract("HydrologicUnits.prj", path = county_path)
    zipObj.extract("HydrologicUnits.sbn", path = county_path)
    zipObj.extract("HydrologicUnits.shp", path = county_path)


os.remove(path + "/HydrologicUnits.zip")

ID_url = "https://dciimages.countyofdane.com/WaterResources/InternallyDrained.zip"
wget.download(ID_url, out = path)

county_path = path + "/DaneCountyData/"

with zipfile.ZipFile("InternallyDrained.zip", 'r') as zipObj:
    zipObj.extract("InternallyDrained.shx", path = county_path)
    zipObj.extract("InternallyDrained.cpg", path = county_path)
    zipObj.extract("InternallyDrained.dbf", path = county_path)
    zipObj.extract("InternallyDrained.prj", path = county_path)
    zipObj.extract("InternallyDrained.sbn", path = county_path)
    zipObj.extract("InternallyDrained.shp", path = county_path)

os.remove(path + "/InternallyDrained.zip")

# Download HUC04 NHDPlusV2 data

watershed4_url = "https://dmap-data-commons-ow.s3.amazonaws.com/NHDPlusV21/Data/NHDPlusGL/NHDPlusV21_GL_04_NHDSnapshot_08.7z"
wget.download(watershed4_url, out = path)

# Extract data from .7z file

watershed4_path = path + "/Watersheds/Watershed4/"
with py7zr.SevenZipFile("NHDPlusV21_GL_04_NHDSnapshot_08.7z", 'r') as z:
    z.extractall(path)

# Move data to proper folder, and then delete the unnecessary unpacked data and the .7z file

NHDPlus4_path = path + "/NHDPlusGL/NHDPlus04/NHDSnapshot/Hydrography/"

shutil.move(NHDPlus4_path + "NHDFlowline.shp", watershed4_path)
shutil.move(NHDPlus4_path + "NHDFlowline.shp.xml", watershed4_path)
shutil.move(NHDPlus4_path + "NHDFlowline.dbf", watershed4_path)
shutil.move(NHDPlus4_path + "NHDFlowline.prj", watershed4_path)
shutil.move(NHDPlus4_path + "NHDFlowline.shx", watershed4_path)
shutil.move(NHDPlus4_path + "NHDWaterbody.shp", watershed4_path)
shutil.move(NHDPlus4_path + "NHDWaterbody.dbf", watershed4_path)
shutil.move(NHDPlus4_path + "NHDWaterbody.prj", watershed4_path)
shutil.move(NHDPlus4_path + "NHDWaterbody.shx", watershed4_path)

shutil.rmtree(path + "/NHDPlusGL")
os.remove(path + "/NHDPlusV21_GL_04_NHDSnapshot_08.7z")

# Download HUC07 NHDPlusV2 data

watershed7_url = "https://dmap-data-commons-ow.s3.amazonaws.com/NHDPlusV21/Data/NHDPlusMS/NHDPlus07/NHDPlusV21_MS_07_NHDSnapshot_08.7z"
wget.download(watershed7_url, out = path)

# Extract data from .7z file

watershed7_path = path + "/Watersheds/Watershed7/"
with py7zr.SevenZipFile("NHDPlusV21_MS_07_NHDSnapshot_08.7z", 'r') as z:
    z.extractall(path)
    
# Move data to proper folder, and then delete the unnecessary unpacked data and the .7z file
    
NHDPlus7_path = path + "/NHDPlusMS/NHDPlus07/NHDSnapshot/Hydrography/"

shutil.move(NHDPlus7_path + "NHDFlowline.shp", watershed7_path)
shutil.move(NHDPlus7_path + "NHDFlowline.dbf", watershed7_path)
shutil.move(NHDPlus7_path + "NHDFlowline.prj", watershed7_path)
shutil.move(NHDPlus7_path + "NHDFlowline.shx", watershed7_path)
shutil.move(NHDPlus7_path + "NHDWaterbody.shp", watershed7_path)
shutil.move(NHDPlus7_path + "NHDWaterbody.dbf", watershed7_path)
shutil.move(NHDPlus7_path + "NHDWaterbody.prj", watershed7_path)
shutil.move(NHDPlus7_path + "NHDWaterbody.shx", watershed7_path)

shutil.rmtree(path + "/NHDPlusMS")
os.remove(path + "/NHDPlusV21_MS_07_NHDSnapshot_08.7z")


# Download the Watershed Boundary Dataset for HUC04

wbd4_url = "https://prd-tnm.s3.amazonaws.com/StagedProducts/Hydrography/WBD/HU2/Shape/WBD_04_HU2_Shape.zip"
wget.download(wbd4_url, out = path)

# Unpack the dataset, move the necessary files, and remove the remaining files and zip file

watershed4_path = path + "/Watersheds/Watershed4/"

with zipfile.ZipFile("WBD_04_HU2_Shape.zip", 'r') as zipObj:
    zipObj.extractall(path = path)

shutil.move(path + "/Shape/WBDHU8.dbf", watershed4_path)
shutil.move(path + "/Shape/WBDHU8.prj", watershed4_path)
shutil.move(path + "/Shape/WBDHU8.shp", watershed4_path)
shutil.move(path + "/Shape/WBDHU8.shx", watershed4_path)
shutil.move(path + "/Shape/WBDHU10.dbf", watershed4_path)
shutil.move(path + "/Shape/WBDHU10.prj", watershed4_path)
shutil.move(path + "/Shape/WBDHU10.shp", watershed4_path)
shutil.move(path + "/Shape/WBDHU10.shx", watershed4_path)
shutil.move(path + "/Shape/WBDHU12.dbf", watershed4_path)
shutil.move(path + "/Shape/WBDHU12.prj", watershed4_path)
shutil.move(path + "/Shape/WBDHU12.shp", watershed4_path)
shutil.move(path + "/Shape/WBDHU12.shx", watershed4_path)
    
os.remove(path + "/WBD_04_HU2_Shape.zip")
os.remove(path + "/WBD_04_HU2_Shape.jpg")
os.remove(path + "/WBD_04_HU2_Shape.xml")
shutil.rmtree(path + "/Shape")

# Download the Watershed Boundary Dataset for HUC07

wbd7_url = "https://prd-tnm.s3.amazonaws.com/StagedProducts/Hydrography/WBD/HU2/Shape/WBD_07_HU2_Shape.zip"
wget.download(wbd7_url, out = path)

# Unpack the dataset, move the necessary files, and remove the remaining files and zip file

watershed7_path = path + "/Watersheds/Watershed7/"

with zipfile.ZipFile("WBD_07_HU2_Shape.zip", 'r') as zipObj:
    zipObj.extractall(path = path)

shutil.move(path + "/Shape/WBDHU8.dbf", watershed7_path)
shutil.move(path + "/Shape/WBDHU8.prj", watershed7_path)
shutil.move(path + "/Shape/WBDHU8.shp", watershed7_path)
shutil.move(path + "/Shape/WBDHU8.shx", watershed7_path)
shutil.move(path + "/Shape/WBDHU10.dbf", watershed7_path)
shutil.move(path + "/Shape/WBDHU10.prj", watershed7_path)
shutil.move(path + "/Shape/WBDHU10.shp", watershed7_path)
shutil.move(path + "/Shape/WBDHU10.shx", watershed7_path)
shutil.move(path + "/Shape/WBDHU12.dbf", watershed7_path)
shutil.move(path + "/Shape/WBDHU12.prj", watershed7_path)
shutil.move(path + "/Shape/WBDHU12.shp", watershed7_path)
shutil.move(path + "/Shape/WBDHU12.shx", watershed7_path)

os.remove(path + "/WBD_07_HU2_Shape.zip")
os.remove(path + "/WBD_07_HU2_Shape.jpg")
os.remove(path + "/WBD_07_HU2_Shape.xml")
shutil.rmtree(path + "/Shape")


# Download Catchment Data for HUC4
catchment4_url = "https://dmap-data-commons-ow.s3.amazonaws.com/NHDPlusV21/Data/NHDPlusGL/NHDPlusV21_GL_04_NHDPlusCatchment_05.7z"
wget.download(catchment4_url, out = path)

# Extract data from .7z file

watershed4_path = path + "/Watersheds/Watershed4/"
with py7zr.SevenZipFile("NHDPlusV21_GL_04_NHDPlusCatchment_05.7z", 'r') as z:
    z.extractall(path)

# Move data to proper folder, and then delete the unnecessary unpacked data and the .7z file

NHDPlus4_path = path + "/NHDPlusGL/NHDPlus04/NHDPlusCatchment/"

shutil.move(NHDPlus4_path + "Catchment.shp", watershed4_path)
shutil.move(NHDPlus4_path + "Catchment.dbf", watershed4_path)
shutil.move(NHDPlus4_path + "Catchment.prj", watershed4_path)
shutil.move(NHDPlus4_path + "Catchment.shx", watershed4_path)

shutil.rmtree(path + "/NHDPlusGL")
os.remove(path + "/NHDPlusV21_GL_04_NHDPlusCatchment_05.7z")


# Download Catchment Data for HUC7
catchment7_url = "https://dmap-data-commons-ow.s3.amazonaws.com/NHDPlusV21/Data/NHDPlusMS/NHDPlus07/NHDPlusV21_MS_07_NHDPlusCatchment_01.7z"
wget.download(catchment7_url, out = path)

# Extract data from .7z file

watershed7_path = path + "/Watersheds/Watershed7/"
with py7zr.SevenZipFile("NHDPlusV21_MS_07_NHDPlusCatchment_01.7z", 'r') as z:
    z.extractall(path)

# Move data to proper folder, and then delete the unnecessary unpacked data and the .7z file

NHDPlus7_path = path + "/NHDPlusMS/NHDPlus07/NHDPlusCatchment/"

shutil.move(NHDPlus7_path + "Catchment.shp", watershed7_path)
shutil.move(NHDPlus7_path + "Catchment.dbf", watershed7_path)
shutil.move(NHDPlus7_path + "Catchment.prj", watershed7_path)
shutil.move(NHDPlus7_path + "Catchment.shx", watershed7_path)

shutil.rmtree(path + "/NHDPlusMS")
os.remove(path + "/NHDPlusV21_MS_07_NHDPlusCatchment_01.7z")
