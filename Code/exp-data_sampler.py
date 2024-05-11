'''
 
Ayomide Laguda 01/25/24

This Python code selects a random column from each cell's expression data and generates a new csv file containing the sampled timesteps.

'''
import pandas as pd
import glob
import random as rm
import sys

output_directory = sys.argv[1]

# Find all files with names starting with 'ExpressionData' in the specified directory
Exp_data = glob.glob(output_directory + "/ExpData/ExpressionData*.csv")
Exp_data.sort()

# Initialize DataFrames to store sampled data
df2 = pd.DataFrame()
df_rand = pd.DataFrame()

df2_nxt = pd.DataFrame()
df_rand_nxt = pd.DataFrame()

df2_last = pd.DataFrame()
df_last = pd.DataFrame()

for file in Exp_data:
    # Read the CSV file into a DataFrame, setting the first column as index
    df = pd.read_csv(file, index_col=0)
    
    # Choose a random column from the DataFrame, excluding the last column
    random_column = rm.choice(df.columns[:-1])

    # Get the index of the randomly chosen column
    rc_index = df.columns.get_loc(random_column)
    
    # Get the column next to the randomly chosen one
    random_column_nxt = df.columns[rc_index + 1]
    
    # Choose a random column from index 900 to the second last column
    last_column = rm.choice(df.columns[900:-1])
    
    # Concatenate the randomly chosen column to the respective DataFrame
    df2 = pd.concat([df2, df[random_column]], axis=1)
    df_rand = df2.copy()
    
    # Concatenate the column next to the randomly chosen one to the respective DataFrame
    df2_nxt = pd.concat([df2_nxt, df[random_column_nxt]], axis=1)
    df_rand_nxt = df2_nxt.copy()

    # Concatenate the randomly chosen column from index 900 to the last column to the respective DataFrame
    df2_last = pd.concat([df2_last, df[last_column]], axis=1)
    df_last = df2_last.copy()

# Save the sampled DataFrames to CSV files
df_rand.to_csv(output_directory + "/ExpData/sampled_ExpData.csv")
df_rand_nxt.to_csv(output_directory + "/ExpData/(t+1)_sampled_ExpData.csv")
df_last.to_csv(output_directory + "/ExpData/(>900)_sampled_ExpData.csv")
