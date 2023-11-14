# Overview
The purpose of this site is to provide the code and data used to quantify the impact of internal legacy P load on cyanobacteria bloom severity in a lake and map areas upstream of the lake with potential legacy P stores. 

The code and data contained herein are provided as supplemnetal material associated with the following article: 
Knose, L.A.; Cole, D.; Martin-Hernandez, E.; Vaneeckhaute, C.; Ruiz-Mercado, G.J.; Gonzalez, M.A.; Zavala, V.M. (in prep) "Data logistics framework for determining the effect of internal legacy phosphorus on the predictability of cyanobacteria harmful 
algal blooms in freshwater lakes." _TBD_  

# Authorship
This GitHub was generated and maintained by Dr. Lauren Knose, an ORISE Fellow with the U.S. Environmental Protection Agency Office of Research and Development. Dr. Knose is the author of the R code and programs. David Cole, PhD Student at the University of Wisconsin, is the author of the Python code and programs. 

# Contents:
There are two main frameworks contained in this Git-hub site. The first is a data and model framework for quantifying external P loads, internal legacy P loads, and source attributed impact on cyanobacteria bloom severity using R language (version 4.2.2). The second is a data and model framework for mapping potential legacy P stores in upstream sub-watersheds (HUC 12) of Lake Mendota, WI (USA) and estimating the total P load per contributing area across sub-watersheds.

## 1. R Model Framework
R language was used to mine and process the data and quantify the impact of total P loads on cyanobacteria bloom severity, attributed to source (external load vs internal legacy load). All programs written in R language used in this project are provided in the R_framework folder. All R models are written as R Markdown files (.Rmd). The specific order in which R programs should be run to achieve the same results, as shown in the manuscript, is as follows:
1a. Mendota_P_external_atmdep.Rmd - calculates the external P loading from atm
1b. Mendota_Pexternal_inflow.Rmd - calculates the external P loading from streams
1c. Mendota_P_ext_all.Rmd - combines the external P loading from streams and atm
1d. Mendota_Volume.Rmd - calculates the volume of the lake layers using temperature profiles
1e. Mendota_P_internal_all.Rmd - calculates the internal loading of P using mass balance and alternatively, the ratio of total P in hypolimnion to epilimnion
1f. Mendota_Algae.Rmd - calculates the Chl-a and cyanobacteria relative biovolume as response variables
1g. Mendota_modeling.Rmd - performs the statstical modeling for impact analysis and outputs the partitioned sum of squares for each predictor term 

## 2. Python Model Framework
Python language was used to mine and process the data, map potential legacy P stores in upstream sub-watersheds, and quantify total P load per contributing area across sub-watersheds. All programs written in Python language used in this project are provided in Python_framework folder. All R models are written as R Markdown files (.Rmd). The specific order in which R programs should be run to achieve the same results, as shown in the manuscript, is as follows:
1a. 

## 2. Original Data 
The original (raw) data used in this project was downloaded from online public repositories
and saved in the Original_data folder. 

## 3. Cleaned Data
Any original data that was reformatted, cleaned for quality control, or derived from
a model is saved in the Cleaned_data folder. 

## 4. Products 
Any products, including printouts (as html or pdf), tables, and figures, and code used 
to generate products for the manuscript is saved in the Products folder.
