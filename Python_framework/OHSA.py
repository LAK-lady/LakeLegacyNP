#Optimized hot spot analysis program

arcpy.stats.OptimizedHotSpotAnalysis(Total_P_mapped_Project, # Input_Features= stream total P concentrations mapped to monitoring sites 
Total_P_hotspot_optimized, #Output_Features= Moran's I value for each monitoring site
{Total_P_Yahara_streams_csv_ResultMeasureValue}, #Analysis_Field=Total_P_Yahara_streams_csv_ResultMeasureValue
{COUNT_INCIDENTS_WITHIN_FISHNET_POLYGONS}, #Incident_Data_Aggregation_Method
{Bounding_Polygons_Defining_Where_Incidents_Are_Possible}, 
{Polygons_For_Aggregating_Incidents_Into_Counts}, 
{Density_Surface}, {Cell_Size}, {Distance_Band})

