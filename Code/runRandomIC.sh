#!/bin/bash

<<Comment

This shell scipt is the brain of all the operations.

It starts from the input gene network file and ends at the visualization of the movement of the cells.

Comment

# Initialize the run_ID variable.
run_ID=0

# Initialize number of simulations.
num_simulations=$1

# Name of gene_network for the output
gene_network=$2

# Check if an argument is provided
if [ -z  "$1" ]; then
       	num_simulations=20
fi

if [ -z  "$2" ]; then
	gene_network='Name-not-provided'
fi

# Sets some of the directories going to be used.
the_directory=/home/alaguda/Synthetic-RNA-maps/Code
bool_directory=/home/alaguda/BoolODE
output_directory=$the_directory/MPL_singleic_op

# Clears the files in the output directory
rm -r $output_directory/*
mkdir -p $output_directory/ExpData
while [ $run_ID -lt $num_simulations ]
do
echo $run_ID
cd $the_directory/singleic_ip
python3 generate_randominput.py cordicalArea.txt

cd $the_directory
python3 $bool_directory/boolode.py --config $the_directory/singleic_ip/SingleIC.yaml

mkdir -p $output_directory/ic$run_ID

cp $the_directory/singleic_ip/rand_ICS.txt $output_directory/ic$run_ID

mv $the_directory/singleic_op/* $output_directory/ic$run_ID

python3 make_plot.py $output_directory/ic$run_ID/SingleIC/ExpressionData.csv

mv $the_directory/figure.png $output_directory/ic$run_ID/figure$run_ID.png

cp $output_directory/ic$run_ID/SingleIC/ExpressionData.csv $output_directory/ExpData/ExpressionData$run_ID.csv

((run_ID++))
done

python3 exp-data_sampler.py

python3 visualize.py

cp -rf  MPL_singleic_op output_${num_simulations}cells_${gene_network}
