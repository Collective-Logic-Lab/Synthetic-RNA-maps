import pandas as pd
import matplotlib.pyplot as plt
import sys
def plot_expressions(filename,destination):
	'''
	Transforms gene expression data of a cell over time into a line graph pdf.
	
	Args:
	
	filename (str): Path to the CSV file containing the cell's gene expression data.
        destination (str): Path to save the generated PDF file.
	
	Returns:
	
	None
	
	'''
        # Read the CSV file into a DataFrame, transposing it to have genes as columns and time points as rows
	df=pd.read_csv(filename, index_col=0).transpose()
	df.plot()
	plt.savefig(destination)	
if __name__== "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) == 3:
        # Call the plot_expressions function with the input and output file paths provided as arguments
        plot_expressions(sys.argv[1],sys.argv[2])
    else:
        print("ERROR: The desired usage is python make_plot.py input_file output_file !!!")
