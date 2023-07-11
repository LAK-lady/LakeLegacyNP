# LakeLegacyNP
This project is focused on quantifying legacy internal P loading versus external
P loading to a lake basin and determine the relative contribution of each on 
CyanoHAB severity.

# Authorship:
This GitHub was generated and maintained by Dr. Lauren Knose, ORISE Fellow with the
U.S. Environmental Protection Agency Office of Research and Development. Dr. 
Knose is the author of the R code and programs. David Cole, PhD Student at the
University of Wisconsin, is the author of the Python code and programs. To cite 
this work, please use the following citation. 

Knose, L., Cole, D., Ruiz-Mercado, D.; Gonzalez, M.; Martin-Hernandez, E.; 
Zavala, V. *(manuscript in prep)*

# Contents:

## 1. Programs:
All programs, written in R or Python, used in this project are provided in this 
programs and code was written in R Markdown files (.Rmd). There is a specific 
order in which programs should be run to achieve the same results. The order of 
run for the programs is as follows:
a. Mendota_P_external_atmdep.Rmd - calculates the external P loading from atm
b. Mendota_Pexternal_inflow.Rmd - calculates the external P loading from streams
c. Mendota_P_ext_all.Rmd - combines the external P loading from streams and atm
d. Mendota_Volume.Rmd - calculates the volume of the lake layers
e. Mendota_P_internal_all.Rmd - calculates the internal loading of P
f. Mendota_Algae.Rmd - calculates the Chl-a and cyanobacteria relative biovolume
g. Mendota_modeling.Rmd - performs the statstical modeling for impact analysis


## 2. Original Data 
The original (raw) data used in this project is located in the Original_data 
folder. 

## 3. Cleaned Data
Any data that was reformatted, cleaned (QA/QC), and generated from raw data is
located in the Cleaned_data folder. 

## 4. Products 
Any printouts (html or pdf), tables, and figures generated from this project
are located in the Products folder. 
