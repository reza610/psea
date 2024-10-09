import pandas as pd
import os

def run_filtering(patient_comorbid_threshold, 
                  min_comorbids_percent, 
                  max_comorbids_percent, 
                  individual_expression_threshold, 
                  min_mean_expression, 
                  values_file, 
                  binary_attribute_file, 
                  sample_name, 
                  include_values_file, 
                  include_binary_attribute_file):
    
    """
    
    This function reads in the cormorbidity designation and gene expression data files, 
    and filters them based on user defined inputs. It then outputs lists of filtered Genes and Comorbidities that can be used for PSEA. 
    It requires the following arguments: 
    
    - patient_comorbid_threshold = Threshold for minimum number of comorbidities a patient should have to be included. 

    - min_comorbids_percent = Threshold for the minimum percent prevolence of a comorbidity to retain that comorbidity. 
    
    - max_comorbids_percent = Threshold for the maximum percent prevolence of a comorbidity to retain that comorbidity.
    
    - individual_expression_threshold = the lowest expression value an individual has 
    across all their genes before that individual is thrown out.
    
    - min_mean_expression = Threshold for minimum gene expression level to retain a gene.
    
    - values_file = the file with patient IDs, gene names, and gene expression values.
    
    - binary_attribute_file = the file with patient IDs and comorbidity designations.
    
    - sample_name = the title of the column that has the patient IDs or sample names in the comorbidity and gene expression files.
    
    - include_values_file = Name/location of file to contain filtered list of gene names.
    
    - include_binary_attribute_file = Name/location of file to contain filtered list of cormorbidities.
    
    """
    
    ##comorbidity csv filtering##
    
    # get working dir and read in the CSV file
    #sample_name = 'Patient'
    # binary_attribute_file = '../testdata/comorbid_file.csv'
    file_path = binary_attribute_file
    df = pd.read_csv(file_path, index_col=0)
    
    # number samples
    total_samples = df.shape[0]
    
    # Filter out patients without comorbidities
    # patient_comorbid_threshold = 1
    filtered_df = df[df.drop(columns=[sample_name]).sum(axis=1) >= patient_comorbid_threshold]
    
    # drop sample_names column
    df_noname = filtered_df.drop(columns=[sample_name])
    
    # Calculate percent occurence of comorbidities
    n_comorbid = df_noname.sum(axis=0).to_frame()
    n_comorbid.columns =["n"]
    n_comorbid["binary_attribute"] = n_comorbid.index
    n_comorbid["percent"] =  n_comorbid["n"]/total_samples

    # Filter based on user input min and max comorbid occurence
    #max_comorbids_percent = 0.9
    #min_comorbids_percent = 0.1
    n_comorbid = n_comorbid[n_comorbid["percent"]<max_comorbids_percent]
    n_comorbid = n_comorbid[n_comorbid["percent"]>min_comorbids_percent]
    
    # name the output file and save it based on include_binary_attribute_file argument input
    #include_binary_attribute_file = '../testdata/include_binary_attribute_long.csv'
    outdir = include_binary_attribute_file
    n_comorbid[["binary_attribute"]].to_csv(outdir, header=False, index=False)
    
    ##gene expression csv filtering##
    
    # get working dir and read in the CSV file for gene expression data
    # values_file = '../testdata/value_expression.csv'
    file_path = values_file
    df = pd.read_csv(file_path, index_col=0)
    print(file_path)
    
    # drop samples column
    expression_df_nosamples = df.drop(columns=[sample_name])
    
    # Remove individuals (rows) where all gene expression values are below the threshold
    #individual_expression_threshold = 10
    individual_mask = expression_df_nosamples.apply(lambda row: (row >= individual_expression_threshold).any(), axis=1)
    # Filter the DataFrame using the individual_mask
    expression_df_nosamples = expression_df_nosamples[individual_mask]
    
    # get mean expression, turn into pandas dataframe
    # min_mean_expression = 0.1
    meansdf=expression_df_nosamples.mean(axis=0).to_frame()
    meansdf.columns = ["mean_value"]
    meansdf["valuename"]= meansdf.index
    
    # filter based on mean expression
    meansdf_include = meansdf[meansdf["mean_value"]>min_mean_expression]
    
    # save output file based on include_values_file argument input
    #include_values_file = "../testdata/include_values_long.csv"
    outdir = include_values_file
    meansdf_include[["valuename"]].to_csv(oudir, header=False, index=False)
    
    ####Some ideas going forward:
    # Need to add more error handling
    