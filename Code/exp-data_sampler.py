'''
 
Ayomide Laguda 01/25/24

This Python code selects a random column from each cell's expression data and generates a new csv file containing the sampled timesteps.

'''
import pandas as pd
import glob
import random as rm

the_directory='/home/alaguda/Synthetic-RNA-maps/Code'

Exp_data = glob.glob(the_directory + "/MPL_singleic_op/ExpData/ExpressionData*.csv")
Exp_data.sort()

df2 = pd.DataFrame()
df_rand = pd.DataFrame()

df2_nxt = pd.DataFrame()
df_rand_nxt = pd.DataFrame()

df2_last = pd.DataFrame()
df_last = pd.DataFrame()

for file in Exp_data:
    df = pd.read_csv(file, index_col=0)
        
    random_column = rm.choice(df.columns[:-1])
    rc_index = df.columns.get_loc(random_column)
                        
    random_column_nxt = df.columns[rc_index + 1]

    last_column = rm.choice(df.columns[900:-1])
                                
    df2 = pd.concat([df2, df[random_column]], axis=1)
    df_rand = df2.copy()
                                            
    df2_nxt = pd.concat([df2_nxt, df[random_column_nxt]], axis=1)
    df_rand_nxt = df2_nxt.copy()

    df2_last = pd.concat([df2_last, df[last_column]], axis=1)
    df_last = df2_last.copy()

df_rand.to_csv(the_directory + "/MPL_singleic_op/ExpData/sampled_ExpData.csv")
df_rand_nxt.to_csv(the_directory + "/MPL_singleic_op/ExpData/(t+1)_sampled_ExpData.csv")
df_last.to_csv(the_directory + "/MPL_singleic_op/ExpData/(>900)_sampled_ExpData.csv")
