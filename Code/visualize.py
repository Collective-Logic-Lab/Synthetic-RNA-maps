import pandas as pd
from sklearn.manifold import TSNE
import matplotlib
import matplotlib.pyplot as plt

def vis(df, p):
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
    tdf.to_csv('/home/ay/Documents/SINGLE/MPL_singleic_op/ExpData/tsne.csv')
    fig, ax = plt.subplots(1,1,figsize=(5,5))
    ax.scatter(tsne[:,0], tsne[:,1], c = [float(col.split('_')[1]) for col in df.columns])
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('/home/ay/Documents/SINGLE/MPL_singleic_op/CellAttractor.pdf')

df=pd.read_csv('/home/ay/Documents/SINGLE/MPL_singleic_op/ExpData/sampled_ExpData.csv', index_col=0)
vis(df, 10)
