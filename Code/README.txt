runRandomIC.sh

This shell script combines many Python programs to execute a selection of tasks ranging from gene network processing to cell movement visualization.  The script runs simulations, using BoolODE to simulate single-cell RNA sequencing data.  The simulation is started from many random initial conditions, and simulated data are output as CSV files.

Linked Python Scripts:

- `exp-data_sampler.py`: Python script to sample expression data for further analysis.
- `make_plot.py`: Python script to generate gene-plots for each simulation from expression data.
- `visualize.py`: Python script to visualize cell movement.
- `network_modifier.py`: Python script to modify network format.

Usage:

To run the shell script, open a terminal and navigate to the directory containing 'runRandomIC.sh'. Then, execute the script with the following command:

./runRandomIC.sh [num_simulations] [test_name] [gene_network_file]

	num_simulations: Number of simulations to run (default: 20).
	test_name: Name of the test for the output (default: '--').
	gene_network_file: Path to the gene network file (default: 'cordicalArea.txt').

Dependencies:

Python 3.x
BoolODE library (originally from https://murali-group.github.io/Beeline/BoolODE.html; forked version here: https://github.com/Collective-Logic-Lab/BoolODE)

Notes:

The output will be stored in the 'output_[num_simulations]cells_[test_name]' directory.

If the gene_network_file is already in the singleic_ip directory, the command only needs the name of the file. If the network is in a folder in singleic_ip then add the folder name then the file name like "Apopstosis\expressions.txt"

SUPERCOMPUTER command:

sbatch run_slurm_job.sh [num_simulations] [test_name] [gene_network_file]
