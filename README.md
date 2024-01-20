# Overview
The purpose of this site is to provide the code and data used to quantify the impact of the internal load (legacy P load from lake sediments) on cyanHAB severity in a lake and map areas upstream of the lake with potential legacy P stores. The framework includes an impact model method and a mapping model method described below.  

The code and data contained herein are provided as supplemental material associated with the following article: 
Knose, L.A.; Cole, D.; Martin-Hernandez, E.; Vaneeckhaute, C.; Ruiz-Mercado, G.J.; Gonzalez, M.A.; Zavala, V.M. (in prep) "Framework for determining impact of legacy nutrient loading from lake sediments (the internal load) on cyanobacteria harmful algal blooms severity in freshwater lake." _TBD_  

# Authorship
This GitHub was generated and maintained by Dr. Lauren Knose, an ORISE Fellow with the U.S. Environmental Protection Agency Office of Research and Development. Dr. Knose is the author of the impact model method. David Cole, PhD Student at the University of Wisconsin, is the author of the mapping model method. When using or referencing information from this repository, please use the citation above.

# Contents:
There are two methods contained in this Git-hub site. The first is the impact model method for quantifying external load, internal load, and source attributed impact on cyanoHAB severity. This method was written using R language (version 4.2.2). The second is the mapping model method for mapping potential legacy P stores in upstream sub-watersheds of Lake Mendota, WI (USA) and estimates the total P load per contributing area across sub-watersheds. This method was written using Python language (version 3.8.5) and GeoPandas (version 0.8.2).

## 1. Impact_model_method
The impact model method is a series of sequential programs (represented with yellow boxes) that take original source data (represented with blue ovals), performs quality control checks and re-formats the data as new data files (represented as green ovals) for input into the impact model. All programs used in this method are provided in the Impact_model_method folder. All code is written ins R Markdown format (.Rmd). The specific order in which R programs should be run to achieve the same results as shown in the manuscript is as follows:
  1. cyanoHAB_severity.Rmd - calculates cyanoHAB severity (as Chl-a and cyanobacteria density)
  2. TotalP_external_atmdep.Rmd - calculates external total P loads from atmospheric deposition
  3. TotalP_external_inflows.Rmd - calculates external total P loads from inflows (streams)
  4. TotalP_external_all.Rmd - calculates the sum of external total P loads (streams + atmospheric deposition)
  5. EpiVolume.Rmd - calculates the change in volume of the epilimnion  using temperature profiles
  6. TotalP_water.Rmd - calculates the total P concentration in the epilimnion, total P concentration in the hypolimnion, and ratio of total P in hypolimnion to epilimnion (as alternative indicator of internal P load)
  7. TotalP_internal.Rmd - calculates internal total P loads (or alternatively the ratio of totalP_hypo:totalP_epi)
  8. Model_inputs.Rmd - prepares the data as input for impact modeling (defines predictor and response variables)
  9. Impact_model.Rmd - performs the statistical modeling for impact analysis on cyanoHAB severity by source (external vs internal) and outputs the partitioned sum of squares for each predictor term 

## 2. Mapping_model_framework
Python language was used to mine and process the data, map potential legacy P stores in upstream sub-watersheds, and quantify total P load per contributing area across sub-watersheds. All programs written in Python language used in this project are provided in Python_framework folder. All programs used in this method are provided in the Mapping_model_method folder. All code is written in Python (.py or .ipynb). The specific order in which programs should be run to achieve the same results as shown in the manuscript is as follows:
  1. HydroGraph_functios.py - performs the network mapping of sub-watersheds upstream of the inflows to the lake
  2. watershed_analysis.ipynb - calculates the P export per contributing area for each of the upstream sub-watersheds
  3. OHSA.py - performs the optimized hot spot analysis for determining statistically clustered stream monitoring sites with consistently high P concentrations

## 2. Original Data 
The original (raw) data used in this project was downloaded from online public repositories
and saved in the Original_data folder. 

## 3. Cleaned Data
Any original data that was reformatted, cleaned for quality control, or derived from
a model is saved in the Cleaned_data folder. 

## 4. Products 
Any products, including printouts (as html or pdf), tables, and figures used 
to generate products for the manuscript is saved in the Products folder.
