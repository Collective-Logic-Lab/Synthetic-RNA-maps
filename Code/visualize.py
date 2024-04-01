import pandas as pd
from sklearn.manifold import TSNE
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def vis(df, df_2, p, directory):
    '''
    
    Transforms the sampled expression data into a pdf that shows the movement of cells.
    
    Args:
    
    Takes the dataframe to be changed and the perplexity of the generated pdf image.
    
    Returns:
    
    Creates a tsne file that transposes the original df but only has two columns (excluding the index column).
    
    Creates a pdf file containing the visualization.
    
    '''
    tsne = TSNE(n_components=2,perplexity=p).fit_transform(df.T.values)
    tdf = pd.DataFrame(tsne, columns=['t-SNE 1', 't-SNE 2'],index=df.columns)

    tsne_nxt = TSNE(n_components=2,perplexity=p).fit_transform(df_2.T.values)
    tdf_nxt = pd.DataFrame(tsne_nxt, columns=['t-SNE 1', 't-SNE 2'],index=df_2.columns)


    tdf.to_csv(directory + '/MPL_singleic_op/ExpData/tsne.csv')
    fig, ax = plt.subplots(1,1,figsize=(5,5))
    ax.scatter(tsne[:,0], tsne[:,1], c = [float(col.split('_')[1]) for col in df.columns])

#    for i in range(len(tsne)):
#        plt.arrow(x=tsne[:,0][i], y=tsne[:,1][i], dx=(tsne_nxt[:,0][i] - tsne[:,0][i]), dy=(tsne_nxt[:,1][i] - tsne[:,1][i]), width=.04)

    ax.axis('off')
    plt.tight_layout()
    plt.savefig(directory + '/MPL_singleic_op/CellAttractor.png')

def my_vis(df, df_2, p, directory):
    '''

    This is Ayomide's way of visualizing the sampled data using averages.

    It's main purpose is to check if the original tsne visualization is working.

    This visualization only works when we already know which genes are the target genes.

    '''
    avg_1=[]
    avg_2=[]
    nxt_avg_1=[]
    nxt_avg_2=[]

    for column in df.columns:
        column_avg_1 = df[column].iloc[:2].mean()

        column_avg_2 = df[column].iloc[-3:].mean()

        avg_1.append(column_avg_1)
        avg_2.append(column_avg_2)

    tdf = pd.DataFrame({'x1':avg_1,'x2':avg_2}, index=df.columns)
    tdf.to_csv(directory + '/MPL_singleic_op/ExpData/my_projection.csv')

    for column in df_2.columns:
        column_avg_1 = df_2[column].iloc[:2].mean()

        column_avg_2 = df_2[column].iloc[-3:].mean()

        nxt_avg_1.append(column_avg_1)
        nxt_avg_2.append(column_avg_2)

    tdf_2 = pd.DataFrame({'x1':nxt_avg_1,'x2':nxt_avg_2}, index=df_2.columns)


    fig, ax = plt.subplots(1,1,figsize=(5,5))
    ax.scatter(avg_1, avg_2, c = [float(col.split('_')[1]) for col in df.columns])

    for i in range(len(avg_1)):
        plt.arrow(x=avg_1[i], y=avg_2[i], dx=(nxt_avg_1[i] - avg_1[i]), dy=(nxt_avg_2[i] - avg_2[i]), width=.02)
    
    plt.tight_layout()
    plt.savefig(directory + '/MPL_singleic_op/MY_CellAttractor.png')


the_directory='/home/alaguda/Synthetic-RNA-maps/Code'
    
df=pd.read_csv(the_directory + '/MPL_singleic_op/ExpData/sampled_ExpData.csv', index_col=0)

df_2=pd.read_csv(the_directory + '/MPL_singleic_op/ExpData/(t+1)_sampled_ExpData.csv', index_col=0)

df_last=pd.read_csv(the_directory + '/MPL_singleic_op/ExpData/(>900)_sampled_ExpData.csv', index_col=0)

vis(df, df_2, 50, the_directory)
my_vis(df, df_2, 50, the_directory)
