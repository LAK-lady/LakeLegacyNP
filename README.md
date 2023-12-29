# Overview
The purpose of this site is to provide the code and data used to quantify the impact of internal legacy P load on cyanobacteria bloom severity in a lake and map areas upstream of the lake with potential legacy P stores. 

The code and data contained herein are provided as supplemnetal material associated with the following article: 
Knose, L.A.; Cole, D.; Martin-Hernandez, E.; Vaneeckhaute, C.; Ruiz-Mercado, G.J.; Gonzalez, M.A.; Zavala, V.M. (in prep) "Data logistics framework for determining the effect of internal legacy phosphorus on the predictability of cyanobacteria harmful 
algal blooms in freshwater lakes." _TBD_  

# Authorship
This GitHub was generated and maintained by Dr. Lauren Knose, an ORISE Fellow with the U.S. Environmental Protection Agency Office of Research and Development. Dr. Knose is the author of the R code and programs. David Cole, PhD Student at the University of Wisconsin, is the author of the Python code and programs. 

# Contents:
There are two main frameworks contained in this Git-hub site. The first is a data and model framework for quantifying external P loads, internal legacy P loads, and source attributed impact on cyanobacteria bloom severity using R language (version 4.2.2). The second is a data and model framework for mapping potential legacy P stores in upstream sub-watersheds (HUC 12) of Lake Mendota, WI (USA) and estimating the total P load per contributing area across sub-watersheds using Python language.

## 1. R Model Framework
R language was used to mine and process the data and quantify the impact of total P loads on cyanobacteria bloom severity, attributed to source (external load vs internal legacy load). All programs written in R language used in this project are provided in the R_framework folder. All R models are written as R Markdown files (.Rmd). The specific order in which R programs should be run to achieve the same results as shown in the manuscript is as follows:
  1. TotalP_external_atmdep.Rmd - calculates external total P loads from atmospheric deposition
  2. TotalP_external_inflows.Rmd - calculates external total P loads from inflows (streams)
  3. TotalP_external_all.Rmd - calculates the sum of external total P loads (streams + atmospheric deposition)
  4. EpiVolume.Rmd - calculates the change in volume of the epilimnion  using temperature profiles
  5. TotalP_water.Rmd - calculates the total P concentration in the epilimnion, total P concentration in the hypolimnion, and ratio of total P in hypolimnion to epilimnion (as alternative indicator of internal P load)
  6. TotalP_internal.Rmd - calculates internal total P loads (or alternatively the ratio of totalP_hypo:totalP_epi)
  7. cyanoHAB_severity.Rmd - calculates cyanoHAB severity (as Chl-a and cyanobacteria relative biovolume)
  8. Model_inputs.Rmd - prepares the data as input for impact modeling (defines predictor and response variables)
  9. Impact_model.Rmd - performs the statstical modeling for impact analysis on cyanoHAB severity by source (external vs internal) and outputs the partitioned sum of squares for each predictor term 

## 2. Python Model Framework
Python language was used to mine and process the data, map potential legacy P stores in upstream sub-watersheds, and quantify total P load per contributing area across sub-watersheds. All programs written in Python language used in this project are provided in Python_framework folder. All R models are written as R Markdown files (.Rmd). The specific order in which R programs should be run to achieve the same results, as shown in the manuscript, is as follows:
  1. Optimized_hotspot_analysis.py
  2. HydroGraph_functios.py
  3. watershed_analysis.ipynb

## 2. Original Data 
The original (raw) data used in this project was downloaded from online public repositories
and saved in the Original_data folder. 

## 3. Cleaned Data
Any original data that was reformatted, cleaned for quality control, or derived from
a model is saved in the Cleaned_data folder. 

## 4. Products 
Any products, including printouts (as html or pdf), tables, and figures used 
to generate products for the manuscript is saved in the Products folder.
