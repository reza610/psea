import argparse
import numpy as np
import pandas as pd
import psea_organization
import make_rankable_file
import psea_core
from multiprocessing import Pool


def several_rank_and_cores(df):
	print (df)	
	#now I need to adapt make_rankable_file.run_merge run off a dataframe

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run psea on a set of values and binary attributes')
    parser.add_argument('-baf', '--bianary_attribute_file')
    parser.add_argument('-vf', '--values_file')
    parser.add_argument('-sn', '--sample_name')
    parser.add_argument('-od', '--outdir')
    parser.add_argument('-p', '--processes', default=4)
    parser.add_argument('-ivf', '--ignore_values_file', default=False)
    parser.add_argument('-ibaf', '--ignore_bianary_attribute_file', default=False)
    args = parser.parse_args()
    bianary_attribute_file = args.bianary_attribute_file
    values_file = args.values_file
    outdir = args.outdir
    sample_name = args.sample_name
    master_org_filename = psea_organization.run_org(outdir,sample_name,values_file, bianary_attribute_file)
    master_org_df = pd.read_csv(master_org_filename, index_col=0)
    if args.ignore_bianary_attribute_file!=False:
        print ("need to add a filter")
    if args.ignore_values_file!=False:
        print ("need to add a filter")
    n_processes = args.processes
    df_list = np.array_split(master_org_df, n_processes) # split the dataframe into 161 separate tables
    with Pool(processes=n_processes) as p:
        print(p.map(several_rank_and_cores, df_list))

