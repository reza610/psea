# PSEA
Participant set enrichment analysis

## Summary
The goal if PSEA is to link binary attributes to values attributes via samples. In this way we may be able to find value  attributes that cause the binary attributes.

In our example, we analyze gene expression data from 254 individuals with Down syndrome, along with their associated medical conditions. Our objective is to identify genes that, when highly expressed, may influence the likelihood of specific medical conditions.  However, it's important to note that, similar to correlation analysis, a connection between a gene and a condition does not imply causation. NES is the Normalized Erichiment score. A negative NES indcates high levels of that value are seen when the binary attribute is true. A postive NES indcates low levels of that value are seen when the binary attribute is true. 

![alt text](https://github.com/Dowell-Lab/psea/blob/main/src/images/results_example_NES.png "results example")



## PSEA inputs and outputs
PSEA is a tool that takes two csv files as input. Both csvs have the same samples, but one csv has a biarary attirubute for each sample and one has a value attibutes for each sample. The output is a csv with statically signigant linkages between the biarary attirbutes and the value columns. 

### Input files
Both input csv files must have a comman samplename column. 
In our case that common samplename is "Patient".

### 
One of the csv files needs to have in it bianary attributes. In our case the bianrary attributes are the disease/disorder of the patients called comorbdititys. 
![alt text](https://github.com/Dowell-Lab/psea/blob/main/src/images/binary_attributes_df.png "binary attributes csv")

### Value file

One of the files must have columns that can be ranked by the values within the column. In the example case the value file has genes and the expression level of those genes in each Patient. 

![alt text](https://github.com/Dowell-Lab/psea/blob/main/src/images/value_df.png "Value csv")


