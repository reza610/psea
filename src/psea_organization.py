import pandas as pd
import argparse
import time



def run_org(outdir,sample_name,values_file, bianary_attribute_file):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    outfilename=outdir+"organization_"+timestr+".df"
    bianary_attribute_df = pd.read_csv(bianary_attribute_file,index_col=0)
    values_df = pd.read_csv(values_file, index_col=0)
    allvalues = values_df.columns
    allbiararyattr = bianary_attribute_df.columns
    print (allvalues)
    print (allbiararyattr)
    #tododf = "notdone"
    #tododf.to_csv(outfilename) 
    return outfilename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run psea on a single set of values and binary attributes')
    parser.add_argument('-baf', '--bianary_attribute_file')
    parser.add_argument('-vf', '--values_file')
    parser.add_argument('-sn', '--sample_name')
    parser.add_argument('-od', '--outdir')
    args = parser.parse_args()
    bianary_attribute_file = args.bianary_attribute_file
    values_file = args.values_file
    outdir = args.outdir
    sample_name = args.sample_name
    run_org(outdir,sample_name,values_file, bianary_attribute_file)

