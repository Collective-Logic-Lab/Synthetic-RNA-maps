import pandas as pd
from sklearn.manifold import TSNE
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

def vis(df, df_2, p, directory):
    '''
    
    Transforms the sampled expression data into a pdf that shows the movement of cells.
    
    Args:
    
    df (DataFrame): DataFrame representing sampled expression data.
    df_2 (DataFrame): DataFrame representing sampled expression data at the next time step.
    p (int): Perplexity parameter for t-SNE.
    directory (str): Path to save the generated files.
    
    Returns:
    
    None
    
    '''
    # Perform t-SNE transformation on the transpose of the first DataFrame
    tsne = TSNE(n_components=2,perplexity=p).fit_transform(df.T.values)
    tdf = pd.DataFrame(tsne, columns=['t-SNE 1', 't-SNE 2'],index=df.columns)

    # Perform t-SNE transformation on the transpose of the second DataFrame
    tsne_nxt = TSNE(n_components=2,perplexity=p).fit_transform(df_2.T.values)
    tdf_nxt = pd.DataFrame(tsne_nxt, columns=['t-SNE 1', 't-SNE 2'],index=df_2.columns)

    # Save the t-SNE transformed data to a CSV file
    tdf.to_csv(directory + '/ExpData/tsne.csv')

    # Plot t-SNE visualization
    fig, ax = plt.subplots(1,1,figsize=(5,5))
    ax.scatter(tsne[:,0], tsne[:,1], c = [float(col.split('_')[1]) for col in df.columns])


    # 
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    # Save the plot as a PNG file
    ax.axis('on')
    plt.tight_layout()
    plt.savefig(directory + '/CellAttractor.png')

def my_vis(df, df_2, directory):
    '''

    This is Ayomide's way of visualizing the sampled data using averages.

    It's main purpose is to check if the original tsne visualization is working.

    This visualization only works when we already know which genes are the target genes.

    '''
    avg_1=[]
    avg_2=[]
    nxt_avg_1=[]
    nxt_avg_2=[]

    # Calculate averages of the two attractors (11000 and 00111)
    for column in df.columns:
        column_avg_1 = df[column].iloc[:2].mean()

        column_avg_2 = df[column].iloc[-3:].mean()

        avg_1.append(column_avg_1)
        avg_2.append(column_avg_2)

    # Create a DataFrame from the calculated averages
    tdf = pd.DataFrame({'x1':avg_1,'x2':avg_2}, index=df.columns)
    tdf.to_csv(directory + '/ExpData/my_projection.csv')

    # Do the same process for the dataframe with the next time-steps
    for column in df_2.columns:
        column_avg_1 = df_2[column].iloc[:2].mean()

        column_avg_2 = df_2[column].iloc[-3:].mean()

        nxt_avg_1.append(column_avg_1)
        nxt_avg_2.append(column_avg_2)

    tdf_2 = pd.DataFrame({'x1':nxt_avg_1,'x2':nxt_avg_2}, index=df_2.columns)

    # Plot visualization using scatter plot and arrows
    fig, ax = plt.subplots(1,1,figsize=(5,5))
    ax.scatter(avg_1, avg_2, c = [float(col.split('_')[1]) for col in df.columns])

    for i in range(len(avg_1)):
        plt.arrow(x=avg_1[i], y=avg_2[i], dx=(nxt_avg_1[i] - avg_1[i]), dy=(nxt_avg_2[i] - avg_2[i]), alpha=0.5, width=.005)
    
    plt.tight_layout()
    plt.savefig(directory + '/MY_CellAttractor.png')

output_directory = sys.argv[1]

# Read sampled expression data from CSV files into DataFrames
df=pd.read_csv(output_directory + '/ExpData/sampled_ExpData.csv', index_col=0)

df_2=pd.read_csv(output_directory + '/ExpData/(t+1)_sampled_ExpData.csv', index_col=0)

df_last=pd.read_csv(output_directory + '/ExpData/(>900)_sampled_ExpData.csv', index_col=0)

# Visualize cell movement using t-SNE
vis(df, df_2, 32, output_directory)

# Visualize cell movement using averages
my_vis(df, df_2, output_directory)
