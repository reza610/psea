# PSEA
Participant set enrichment analysis

PSEA is a tool that takes two csv files as input and output a dataframe that shows potiential linkages for the columns in the two csv files. 

Both input csv files must have a comman samplename column. 
In our case that common samplename is "Patient".

One of the csv files needs to have in it bianary attributes. In our case the bianrary attributes are the disease/disorder of the patients called comorbdititys. 

One of the files must have columns that can be ranked by the values within them. In the example case the value file has genes and the expression level of those genes in each Patient. 
