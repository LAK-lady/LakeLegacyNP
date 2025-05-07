# Overview
The purpose of this repository is to provide the framework, code, and data used to 1) map upstream sub-watersheds discharging a disproportionate amount of phosphorus (P) per contributing area, and 2) quantify the impact of the internal load (legacy P load from lake sediments) and external load (fresh incoming load from land and air) on cyanobacteria harmful algal bloom (cyanHAB) severity in a freshwater lake. The framework includes an impact model method and a spatial model method described below. 

The code and data contained herein are provided as supplemental information (SI) associated with the following article: 

Title: The impact of legacy nutrient loading from lake sediments on cyanobacteria bloom severity. 
Author names and affiliations: Lauren A. Knose1, David L. Cole2, Edgar Martín-Hernández3,4, Victor M. Zavala2, Michael A. Gonzalez5, Céline Vaneeckhaute4, Gerardo J. Ruiz-Mercado5,6* 
1Research Participation Program, Oak Ridge Institute for Science and Education hosted by the U.S. Environmental Protection Agency, Cincinnati, Ohio, United States
2Department of Chemical Engineering, University of Wisconsin, Madison, Wisconsin, United States
3Department of Mining and Materials Engineering, McGill University, Quebec, Canada
4Department of Chemical Engineering, Université Laval, Québec City, Canada 
5Office of Research and Development, U.S. Environmental Protection Agency, Cincinnati, OH, United States 
6Chemical Engineering Graduate Program, Universidad del Atlántico, Puerto Colombia 080007, Colombia

Corresponding author: *Dr. Gerardo J. Ruiz-Mercado, 26 Martin Luther King Drive West, Cincinnati, OH 45220, ruiz-mercado.gerardo@epa.gov 

# Authorship
This repository was generated and maintained by Lauren Knose, PhD through an ORISE appointment with the U.S. EPA. Dr. Knose is the author of the impact model method. David Cole, PhD Student at the University of Wisconsin, is the author of the spatial model method. When using or referencing information from this repository, please use the citation above.

# Contents:
There are two model methods contained in this repository. The first is the spatial model method for mapping potential legacy P stores in upstream sub-watersheds and estimating the total P load per contributing area across sub-watersheds. The spatial method was written using Python language (version 3.8.5) and GeoPandas (version 0.8.2). The second is the impact model method for quantifying external loads, internal loads, and source attributed impact on cyanoHAB severity. This method was written using R Markdown (.Rmd) and R software (version 4.2.2). The master (main) branch uses data from Lake Mendota, WI (USA) as the primary case study. Additional branches are named based on additional case studies.

## 1. Spatial model method - The spatial model method (contained in the repository folder named “Mapping_model_method”) is a series of sequential programs (represented with yellow boxes), run by the user, that take original source data (represented with blue ovals), performs quality control checks and re-formats the data as new data files (represented with green ovals) for input into the mapping and analysis models (as shown in SI-Figure 1. Spatial_model_method.svg). The specific order in which programs should be run to achieve the same results as shown in the manuscript is as follows:
  1. HydroGraphs.py – calls the original geospatial layers and stream monitoring location data, processes the data and builds the network of sub-watersheds upstream of the inflows, then outputs new geospatial layers from the model.
  2. build_Yahara_data.ipynb –bounds the contributing area to the hydrologically connected boundaries to generate the total contributing area of each sub-watershed. 
  3. watershed_analysis.ipynb - attributes stream nutrient data to sub-watershed geospatial layers, calculates the P export per contributing area for each upstream sub-watershed, and outputs the new data as geospatial data layers with attribute tables. 
Notes about the code: HydroGraphs was originally written in Python language, therefore all data processing and analyses in the spatial model method were completed using Python language. 

## 2. Impact model method - The impact model method (contained in the repository folder named “Impact_model_method”) is a series of sequential programs (represented with yellow boxes), run by the user, that take original source data (represented with blue ovals), performs quality control checks and re-formats the data as new data files (represented as green ovals) for input into the analysis models (as shown in SI-Figure 2. Impact_model_method.svg). The specific order to run the programs to achieve the same results shown in the manuscript is as follows:
  0. Dependent_packages.Rmd – loads the dependent packages needed to run the following programs. These packages need to be installed before continuing to the next step. 
  1. cyanoHAB_season.Rmd – defines the cyanoHAB season.
  2. cyanoHAB_severity.Rmd - calculates cyanoHAB severity (as Chl-a and cyanobacteria density).
  3. Stream_data_merge.Rmd – merges the stream data from different sources into one data file.
  4. TotalP_external_inflows.Rmd - calculates external total P loads from inflows (streams).
  5. TotalP_external_atmdep.Rmd - calculates external total P loads from atmospheric deposition.
  6. TotalP_external_all.Rmd - calculates the sum of external total P loads (streams + atmospheric deposition).
  7. TotalP_water.Rmd - calculates the total P concentration in the epilimnion, total P concentration in the hypolimnion, and ratio of total P in hypolimnion to epilimnion (as alternative indicator of internal P load).
  8. TotalP_internal.Rmd - calculates internal total P loads (or alternatively the ratio of totalP_hypo:totalP_epi). The thermocline depth was computed using the “thermo.depth” function in the rLakeAnalyzer package.
  9. Model_inputs.Rmd - prepares the data as input for impact modeling (defines predictor and response variables).
  10. Impact_model.Rmd - performs the statistical modeling for impact analysis on cyanoHAB severity by source (external vs internal) and outputs the partitioned sum of squares for each predictor term.
Notes about the code: Commonly used protocols throughout the code include generating uniform date bins using the “seq” function from the R base package, linear interpolation using the “approx.” function from the stats package. 

# 2. Original Data 
The original (raw) data used in this project was downloaded from online public repositories and saved in the Original_data folder. The years of data included in this study were determined by the overlapping period when data was available for all variables, which occurred between 2013 and 2018 (SI-Table 1).  

# 3. Cleaned Data
Any original data that was reformatted, cleaned for quality control, or derived from a model is saved in the Cleaned_data folder. 

# 4. Products 
Any products, including printouts (as html or pdf), tables, and figures used to generate products for the manuscript is saved in the Products folder.
