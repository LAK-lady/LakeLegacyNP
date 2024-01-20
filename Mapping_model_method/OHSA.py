#Optimized hot spot analysis program

## Import system modules:
import arcpy

## Set property to overwrite existing output, by default:
arcpy.env.overwriteOutput = True

## Specify and set the local workspace:
workspace = r"C:\Users\LKNOSE\OneDrive - Environmental Protection Agency (EPA)\Profile\Documents\SSWR.405.2.2_LegacyNutrients\Analysis\Python\Yahara_Pexport" #spe
arcpy.env.workspace = r"C:\Users\LKNOSE\OneDrive - Environmental Protection Agency (EPA)\Profile\Documents\SSWR.405.2.2_LegacyNutrients\Analysis\Python\Yahara_Pexport"

ohsa = arcpy.stats.OptimizedHotSpotAnalysis("Total_P_mapped_Project", # Input_Features= stream total P concentrations mapped to monitoring sites 
"Total_P_hotspot_optimized", #Output_Features= Moran's I value for each monitoring site
"Total_P_Yahara_streams_csv_ResultMeasureValue", #Analysis_Field=Total_P_Yahara_streams_csv_ResultMeasureValue
"COUNT_INCIDENTS_WITHIN_FISHNET_POLYGONS", #Incident_Data_Aggregation_Method
{Bounding_Polygons_Defining_Where_Incidents_Are_Possible}, 
{Polygons_For_Aggregating_Incidents_Into_Counts}, 
{Density_Surface}, {Cell_Size}, {Distance_Band})

## Print out error message if they occur:
except arcpy.ExecuteError:
    # If any error occurred when running the tool, print the messages
    print(arcpy.GetMessages()
