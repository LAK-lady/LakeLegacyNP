# Time series data

### load dependent packages ###
library(dplyr)
library(reshape2)
library(ggplot2)
library(sf)

### cyanobacteria cell density ###
phyto<-read.csv(file="Cleaned_data/HarshaLake_phytoplankton.csv")

EMB_cyanos<- phyto %>%
  mutate(sampledate=as.Date(CollectionDate,
                            format="%m/%d/%Y",
                            origin="1899-12-30")) %>% #tells R field contains dates
  filter(SiteID=="EMB", #filter for buoy site data
         Division=="Cyanobacteria"|Division==" Cyanobacteria ") %>% #filter for cyanobacteria 
  group_by(sampledate, Depth_ft) %>% #group all observations by sample date
  summarize(cyano_relabund=sum(SampleSpecificCellRelativeAbundance_Perc), #add all observations of cyanobacteria biovolumes together for each sample date
            CD_cellsmL=sum(TaxaSpecificCellDensity_cellsmL)) %>% #adds all the cyanobacteria cells/mL together for each sample date
  filter(cyano_relabund<=100) %>% #remove any invalid records (>100%  not valid entry)
  ungroup() %>%
  mutate(Yr=as.numeric(format(sampledate, "%Y")), #renames field
         daynum=as.numeric(format(sampledate, "%j"))) #adds field with day
write.csv(EMB_cyanos, file="Cleaned_data/HarshaLake_EMB_cyanos.csv")

cyano_ts<- ggplot(EMB_cyanos,aes(x=daynum, y=CD_cellsmL))+
  geom_point()+ # observations as points
  facet_wrap(~Yr)+ # separate data by year
  theme_classic()+ # black and white
  geom_smooth()+ # add loess regression curve (moving average)
  ylim(0, NA)+ # limit Y > 0
  labs(x="Day of year", y="Cyanobacteria (cells/mL)", title="EMB") +
  annotate('rect', fill='gray60', alpha=.2, #creates a shadow box 
           xmin=-Inf, xmax=152, ymin=0, ymax=Inf) +#shadow box highlights CyanoHAB season
  annotate('rect', fill='gray60', alpha=.2, #creates a shadow box 
           xmin=288, xmax=Inf, ymin=0, ymax=Inf)  #shadow box highlights CyanoHAB season
cyano_ts


### toxin data ###
toxins<- read.csv(file= "Original_data/ODOH_HarshaLake_toxinresults_2011to2024.csv")
head(toxins)
attach(toxins)
toxins<- dcast(toxins, Sample_date+Site+Method+Units+Qualifier+Sample_type~Analyte, 
                value.var="Value") %>%
  mutate(sampledate=as.Date(Sample_date, format="%m/%d/%Y",
                            original="1899-12-30"),
         Yr=as.numeric(format(sampledate, "%Y")), #renames field
         daynum=as.numeric(format(sampledate, "%j"))) %>%
  rename(Microcystin_ugL= Microcystin,
         SiteID=Site)
tox_ts<- ggplot(toxins)+
  geom_point(aes(x=daynum, y=Microcystin_ugL, col=Yr))+
  facet_wrap(~SiteID) + 
  theme_classic()+
  # geom_smooth()+
  labs(x="Day of year", y="Microcystin (ug/L)", col="Year") +
  annotate('rect', fill='gray60', alpha=.2, #creates a shadow box 
           xmin=-Inf, xmax=152, ymin=0, ymax=Inf) +#shadow box highlights CyanoHAB season
  annotate('rect', fill='gray60', alpha=.2, #creates a shadow box 
           xmin=288, xmax=Inf, ymin=0, ymax=Inf)  #shadow box highlights CyanoHAB season
tox_ts


### external nutrient loads ###
extLoads<- read.csv(file= "Original_data/HarshaLake_SWAT_loads_2000to2018.csv")
head(extLoads)
attach(extLoads)
extLoads<- extLoads %>%
  mutate(sampledate=as.Date(Date, format="%m/%d/%Y",
                            original="1899-12-30"),
         Yr=as.numeric(format(sampledate, "%Y")), #renames field
         daynum=as.numeric(format(sampledate, "%j"))) %>%
  rename(allTN_kg= TOTN_kg_All,
         allTP_kg= TOTP_kg_All)
write.csv(extLoads, file="Cleaned_data/HarshaLake_streamLoads.csv")
extTNLoads_ts<- ggplot(extLoads,aes(x=daynum, y=allTN_kg, col=Yr))+
  geom_point()+
  theme_classic()+
  geom_smooth(col="black")+
  labs(x="Day of year", y="Total N Loads (kg)", col="Year") +
  annotate('rect', fill='gray60', alpha=.2, #creates a shadow box 
           xmin=-Inf, xmax=152, ymin=0, ymax=Inf) +#shadow box highlights CyanoHAB season
  annotate('rect', fill='gray60', alpha=.2, #creates a shadow box 
           xmin=288, xmax=Inf, ymin=0, ymax=Inf)  #shadow box highlights CyanoHAB season
extTNLoads_ts
extTPLoads_ts<- ggplot(extLoads,aes(x=daynum, y=allTP_kg, col=Yr))+
  geom_point()+
  theme_classic()+
  geom_smooth(col="black")+
  labs(x="Day of year", y="Total P Loads (kg)", col="Year") +
  annotate('rect', fill='gray60', alpha=.2, #creates a shadow box 
           xmin=-Inf, xmax=152, ymin=0, ymax=Inf) +#shadow box highlights CyanoHAB season
  annotate('rect', fill='gray60', alpha=.2, #creates a shadow box 
           xmin=288, xmax=Inf, ymin=0, ymax=Inf)  #shadow box highlights CyanoHAB season
extTPLoads_ts


### bathymetry ###
download.file("https://gis.ohiodnr.gov/geodata/Clermont/eastfork_10ftcontours.zip", destfile = "Original_data/eastfork_10ftcontours.zip")
unzip("Original_data/eastfork_10ftcontours.zip", junkpaths=FALSE)
HL_sf<- read_sf("Original_data/eastfork_10ftcontours.shp")
par(mar=c(0,0,0,0))
ggplot(HL_sf)+
  geom_sf(aes(col=Contour)) + 
  scale_color_gradient(high="red", low="darkblue") +
  labs(col="Contour (ft below surface)")
nrow(HL_sf)
head(HL_sf)
sort(unique(HL_sf$Contour))


### define uniform intervals ###
Yr_bin<- c(2013,2015, 2017)

### define the observation frequency ###
daynum_bins<- seq(from=152, #define date start of CyanoHAB season
                  to=288, #define date end of CyanoHAB season
                  by=7) #creates a sequence every 7 days 
daynum_bins #prints the expected observation dates of data

### create data frame with expected observations ###
cyanoHAB_bins<- data.frame(Yr_bin=rep(Yr_bin, each=20), #repeat Yr for every daynum 
                           daynum_bin=rep(daynum_bins, times=3)) #repeat daynum for every year

### binning observed dates into expected dates ###
Chla_CD <- Chla_CD  %>%
  filter(daynum>= 145 & daynum<= 295) %>% #filter for cyanoHAB season +- 7 days
  mutate(daynum_bin=
           ifelse(daynum<(daynum_bins[2]-3.5), #if observation is <= bin 2 min
                  daynum_bins[1], #yes returns bin 1
                  ifelse(daynum>=(daynum_bins[2]-3.5)&daynum<(daynum_bins[3]-3.5),
                         #if observation is > bin 2 min and <= bin 3 min
                         daynum_bins[2], #yes returns bin 2
                         ifelse(daynum>=(daynum_bins[3]-3.5)&daynum<(daynum_bins[4]-3.5),
                                #if observation is > bin 3 min and <= bin 4 min
                                daynum_bins[3], #yes returns bin 3
                                ifelse(daynum>=(daynum_bins[4]-7)&daynum<(daynum_bins[5]-7),
                                       #if observation is > bin 4 min and <= bin 5 min 
                                       daynum_bins[4], #yes returns bin 4
                                       daynum_bins[5],
                                       
                                       
                                       
                                       )))))#no returns bin 5

Chla_CD<- Chla_CD %>% 
  filter(!duplicated(cbind(Yr, daynum_bin), fromLast = TRUE))  #remove first duplicate


