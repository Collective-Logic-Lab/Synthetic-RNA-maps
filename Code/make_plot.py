import pandas as pd
import matplotlib.pyplot as plt
import sys
def plot_expressions(filename,destination):
	'''
	Transforms gene expression data of a cell over time into a line graph pdf.
	
	Args:
	
	Accepts the csv file containing the cell's gene expression data.
	
	Returns:
	
	Returns a pdf with a line graph showing the expression of each gene.
	
	'''
	df=pd.read_csv(filename, index_col=0).transpose()
	df.plot()
	plt.savefig(destination)	
if __name__== "__main__":
    if len(sys.argv) == 3:
        plot_expressions(sys.argv[1],sys.argv[2])
    else:
        print("ERROR: The desired usage is python make_plot.py input_file output_file !!!")
