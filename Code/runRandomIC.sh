#!/bin/bash

<<Comment

This shell scipt is the brain of all the operations.

It starts from the input gene network file and ends at the visualization of the movement of the cells.

Comment

# Initialize the run_ID variable.
run_ID=0

# Initialize number of simulations.
num_simulations=$1

# Name of test for the output
test_name=$2

# Path to the gene network file
gene_network=$3

# Check if the number of simulations is provided, default to 20 if not
if [ -z  "$1" ]; then
       	num_simulations=20
fi

# Check if the test name is provided, default to '--' if not
if [ -z  "$2" ]; then
	test_name='--'
fi

# Check if the gene network file is provided, default to 'cordicalArea.txt' if not
if [ -z "$3" ]; then
	gene_network='cordicalArea.txt'
fi

# Sets some of the directories going to be used.
the_directory=/home/avpetrov/Synthetic-RNA-Maps/Code
bool_directory=/home/avpetrov/BoolODE

# Create output directory based on the number of simulations and test name
mkdir -p $the_directory/output_${num_simulations}cells_${test_name}
output_directory=$the_directory/output_${num_simulations}cells_${test_name}

# Clears the files in the output directory
rm -r $output_directory/*
mkdir -p $output_directory/ExpData

# Create directories for single input and output
cp -r $the_directory/singleic_ip $the_directory/singleic_ip_${num_simulations}cells_${test_name}
mkdir -p $the_directory/singleic_op_${num_simulations}cells_${test_name}

singleInputDirectory=$the_directory/singleic_ip_${num_simulations}cells_${test_name}
singleOutputDirectory=$the_directory/singleic_op_${num_simulations}cells_${test_name}

cd $singleInputDirectory

# Modify gene network and create YAML configuration file
gene_network=$(python3 network_modifier.py "$gene_network")

cat << EOF > $singleInputDirectory/SingleIC.yaml
global_settings:
  model_dir: "$singleInputDirectory"
  output_dir: "$singleOutputDirectory"
  do_simulations: True
  do_post_processing: False
  modeltype: 'heaviside'

jobs:
  - name: "SingleIC"
    model_definition: "$gene_network"
    model_initial_conditions: "rand_ICS.txt"
    simulation_time: 1
    num_cells: 1
    do_parallel: True
    integration_step_size: 0.001

post_processing:
  Dropouts:
    - dropout: False
      nCells: 1000
EOF

# Run simulations for specified number of times
while [ $run_ID -lt $num_simulations ]
do
echo $run_ID
# Generate random input
python3 generate_randominput.py $gene_network

mkdir -p $output_directory/ic$run_ID

# Copy random initial conditions to output directory
cp $singleInputDirectory/rand_ICS.txt $output_directory/ic$run_ID

 ((run_ID++))
done

# Run BoolODE simulations
python3 $bool_directory/boolode.py --config $singleInputDirectory/SingleIC.yaml

# Move simulation outputs to the output directory
mv $singleOutputDirectory/* $output_directory/ic$run_ID

# Move back to the main directory
cd $the_directory

# Generate gene plots for each simulation/cell
python3 make_plot.py $output_directory/ic$run_ID/SingleIC/ExpressionData.csv $output_directory/ic$run_ID/figure$run_ID.png

# Copy expression data to the total ExpData directory
cp $output_directory/ic$run_ID/SingleIC/ExpressionData.csv $output_directory/ExpData/ExpressionData$run_ID.csv

((run_ID++))
done

# Remove temporary single input and output directories
rm -r $singleInputDirectory
rm -r $singleOutputDirectory

# Sample expression data
python3 exp-data_sampler.py $output_directory

# Visualize cell movement
python3 visualize.py $output_directory
