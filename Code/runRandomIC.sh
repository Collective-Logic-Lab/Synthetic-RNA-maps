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

gene_network=$3

# Check if an argument is provided
if [ -z  "$1" ]; then
       	num_simulations=20
fi

if [ -z  "$2" ]; then
	test_name='--'
fi

if [ -z "$3" ]; then
	gene_network='cordicalArea.txt'
fi

# Sets some of the directories going to be used.
the_directory=/home/alaguda/Synthetic-RNA-maps/Code
bool_directory=/home/alaguda/BoolODE

mkdir -p $the_directory/output_${num_simulations}cells_${test_name}
output_directory=$the_directory/output_${num_simulations}cells_${test_name}

# Clears the files in the output directory
rm -r $output_directory/*
mkdir -p $output_directory/ExpData

cp -r $the_directory/singleic_ip $the_directory/singleic_ip_${num_simulations}cells_${test_name}
mkdir -p $the_directory/singleic_op_${num_simulations}cells_${test_name}

singleInputDirectory=$the_directory/singleic_ip_${num_simulations}cells_${test_name}
singleOutputDirectory=$the_directory/singleic_op_${num_simulations}cells_${test_name}

cd $singleInputDirectory
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

while [ $run_ID -lt $num_simulations ]
do
echo $run_ID
cd $singleInputDirectory
python3 generate_randominput.py $gene_network

mkdir -p $output_directory/ic$run_ID

cp $singleInputDirectory/rand_ICS.txt $output_directory/ic$run_ID

python3 $bool_directory/boolode.py --config $singleInputDirectory/SingleIC.yaml

mv $singleOutputDirectory/* $output_directory/ic$run_ID

cd $the_directory

python3 make_plot.py $output_directory/ic$run_ID/SingleIC/ExpressionData.csv $output_directory/ic$run_ID/figure$run_ID.png

cp $output_directory/ic$run_ID/SingleIC/ExpressionData.csv $output_directory/ExpData/ExpressionData$run_ID.csv

((run_ID++))
done

rm -r $singleInputDirectory
rm -r $singleOutputDirectory

python3 exp-data_sampler.py $output_directory

python3 visualize.py $output_directory
