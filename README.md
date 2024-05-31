# Overview
The purpose of this repository is to provide the code and data used to quantify the impact of the internal load (legacy P load from lake sediments) on cyanHAB severity in a lake and map areas upstream of the lake with potential legacy P stores. The framework includes an impact model method and a mapping model method described below. 

The code and data contained herein are provided as supplemental material associated with the following article: 

Title: The impact of legacy nutrient loading from lake sediments on cyanobacteria bloom severity
Lauren A. Knose1, David L. Cole2, Edgar Martín-Hernández3, Gerardo J. Ruiz-Mercado4,5*, Victor M. Zavala2, Michael A. Gonzalez4, Céline Vaneeckhaute6

1Research Participation Program, Oak Ridge Institute for Science and Education, Cincinnati, Ohio, United States
2Department of Chemical Engineering, University of Wisconsin, Madison, Wisconsin, United States
3Department of Mining and Materials Engineering, McGill University, Quebec, Canada
4Office of Research and Development, U.S. Environmental Protection Agency, Cincinnati, OH, United States 
5Chemical Engineering Graduate Program, Universidad del Atlántico, Puerto Colombia 080007, Colombia
6Department of Chemical Engineering, Université Laval, Québec City, Canada

Corresponding author: *Dr. Gerardo J. Ruiz-Mercado, 26 Martin Luther King Drive West, Cincinnati, OH 45220, ruiz-mercado.gerardo@epa.gov 

# Authorship
This repository was generated and maintained by Lauren Knose, PhD through an ORISE appointment with the U.S. EPA. Dr. Knose is the author of the impact model method. David Cole, PhD Student at the University of Wisconsin, is the author of the mapping model method. When using or referencing information from this repository, please use the citation above.

# Contents:
There are two model frameworks contained in this repository. The first is the impact model method for quantifying external loads, internal loads, and source attributed impact on cyanoHAB severity. This method was written using R language (version 4.2.2). The second is the mapping model method for mapping potential legacy P stores in upstream sub-watersheds and estimates the total P load per contributing area across sub-watersheds. The mapping method was written using Python language (version 3.8.5) and GeoPandas (version 0.8.2). The master (main) branch uses data from Lake Mendota, WI (USA) as the case study. Additional branches are named based on alternative case studies.

The impact model method is a series of sequential programs (represented with yellow boxes) that take original source data (represented with blue ovals), performs quality control checks and re-formats the data as new data files (represented as green ovals) for input into the impact model (SI-Figure 1). All programs used in this method are provided in the Impact_model_method folder. All code is written in R Markdown format (.Rmd). The specific order in which programs should be run to achieve the same results shown in the manuscript is as follows:

## 1. Impact_model_method
The impact model method is a series of sequential programs that take original source data, performs quality control checks and re-formats the data as new data files for input into the impact model. All programs used in this method are provided in the Impact_model_method folder. All code is written in R Markdown format (.Rmd). The specific order in which R programs should be run to achieve the same results as shown in the manuscript is as follows:
  1. cyanoHAB_seaosn.Rmd – defines the cyanoHAB season
  2. cyanoHAB_severity.Rmd - calculates cyanoHAB severity (as Chl-a and cyanobacteria density)
  3. Stream_data_merge.Rmd – merges the stream data from different sources into one data file
  4. TotalP_external_inflows.Rmd - calculates external total P loads from inflows (streams)
  5. TotalP_external_atmdep.Rmd - calculates external total P loads from atmospheric deposition
  6. TotalP_external_all.Rmd - calculates the sum of external total P loads (streams + atmospheric deposition)
  7. TotalP_water.Rmd - calculates the total P concentration in the epilimnion, total P concentration in the hypolimnion, and ratio of total P in hypolimnion to epilimnion (as alternative indicator of internal P load)
  8. TotalP_internal.Rmd - calculates internal total P loads (or alternatively the ratio of totalP_hypo:totalP_epi)
  9. Model_inputs.Rmd - prepares the data as input for impact modeling (defines predictor and response variables)
  10. Impact_model.Rmd - performs the statistical modeling for impact analysis on cyanoHAB severity by source (external vs internal) and outputs the partitioned sum of squares for each predictor term 

## 2. Mapping_model_method
The mapping model method is a series of sequential programs (represented with yellow boxes), written in Python language and run by the user, that take original source data (represented with blue ovals), performs quality control checks and re-formats the data as new data files (represented with green ovals) for input into the mapping model (SI-Figure 2). All programs used in this method are provided in the Mapping_model_method folder. All code is written in Python (.py or .ipynb). The specific order in which programs should be run to achieve the same results as shown in the manuscript is as follows:
  1. HydroGraphs.py - performs the network mapping of sub-watersheds upstream of the inflows
  2. build_Yahara_data.ipynb – attributes nutrient data to sub-watershed shapefiles
  3. watershed_analysis.ipynb - calculates the P export per contributing area for each of the upstream sub-watersheds
  4. OHSA.py - performs the optimized hot spot analysis for determining statistically clustered stream monitoring sites with consistently high P concentrations

## 2. Original Data 
The original (raw) data used in this project was downloaded from online public repositories and saved in the Original_data folder. The years of data included in this study were determined by the overlapping period when data was available for all variables, which occurred between 2013 and 2018 (SI-Table 1).  

## 3. Cleaned Data
Any original data that was reformatted, cleaned for quality control, or derived from a model is saved in the Cleaned_data folder. 

## 4. Products 
Any products, including printouts (as html or pdf), tables, and figures used to generate products for the manuscript is saved in the Products folder.
