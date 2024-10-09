import argparse
from filter import run_filtering

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run filtering script with user-defined thresholds.")

    # Add arguments
    parser.add_argument('-pct', '--patient_comorbid_threshold', default=1, 
                        help='Threshold for minimum number of comorbidities a patient should have to be included.')
    parser.add_argument('-mincp', '--min_comorbids_percent', default=0.1, 
                        help='Threshold for the minimum percent prevolence of a comorbidity to retain that comorbidity.')
    parser.add_argument('-maxcp', '--max_comorbids_percent', default=0.9, 
                        help='Threshold for the maximum percent prevolence of a comorbidity to retain that comorbidity.')
    parser.add_argument('-mme', '--min_mean_expression', default=0.1, 
                        help='Threshold for minimum gene expression level to retain a gene.')
    parser.add_argument('-iet', '--individual_expression_threshold', default=10, 
                        help='Threshold for minimum overall gene expression level of an given individual for an individual to be retained.')
    parser.add_argument('-vf', '--values_file', type=str,
                        help='File with patient IDs, gene names, and expression values.')
    parser.add_argument('-baf', '--bianary_attribute_file', type=str,
                        help='File with patient IDs and comorbidity designations.')
    parser.add_argument('-sn', '--sample_name', type=str, default='Patient', 
                        help='The title of the column that includes the patient IDs/names.')
    parser.add_argument('-ivf', '--include_values_file', type=str,
                        help='Name/location of file to contain filtered list of gene names.')
    parser.add_argument('-ibaf', '--include_bianary_attribute_file', type=str, 
                        help='Name/location of file to contain filtered list of cormorbidities.')

    

    # Parse arguments from the command line
    args = parser.parse_args()
    
    # Call the filtering function with the provided arguments
    run_filtering(args.patient_comorbid_threshold, args.min_comorbids_percent, args.max_comorbids_percent, 
                  args.min_mean_expression, args.individual_expression_threshold,
                  args.values_file, args.bianary_attribute_file, args.sample_name, 
                  args.include_values_file, args.include_binary_attribute_file)

if __name__ == "__main__":
    main()


    
## next ##
# mnake the slurm script
