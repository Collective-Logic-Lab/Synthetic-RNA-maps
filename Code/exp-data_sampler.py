'''
 
Ayomide Laguda 01/25/24

This Python code selects a random column from each cell's expression data and generates a new csv file containing the sampled timesteps.

'''
import pandas as pd
import glob
import random as rm

Exp_data = glob.glob("/home/ay/Documents/SINGLE/MPL_singleic_op/ExpData/ExpressionData*.csv")
Exp_data.sort()

df2 = pd.DataFrame()
df_rand = pd.DataFrame()

for file in Exp_data:
	df = pd.read_csv(file, index_col=0)
	random_column = rm.choice(df.columns)
	df2 = pd.concat([df2, df[random_column]], axis=1)
	df_rand = df2.copy()

df_rand.to_csv("/home/ay/Documents/SINGLE/MPL_singleic_op/ExpData/sampled_ExpData.csv")
