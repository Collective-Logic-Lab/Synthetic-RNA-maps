#!/bin/bash

<<Comment

This shell scipt is the brain of all the operations.

It starts from the input gene network file and ends at the visualization of the movement of the cells.

Comment

# Initialize the run_ID variable.
run_ID=0

# Sets some of the directories going to be used.
the_directory=/home/ay/Documents/SINGLE
bool_directory=/home/ay/Downloads/BoolODE-master
output_directory=$the_directory/MPL_singleic_op

# Clears the files in the output directory
rm -r $output_directory/*
mkdir -p $output_directory/ExpData
while [ $run_ID -lt 100 ]
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

mv $the_directory/figure.pdf $output_directory/ic$run_ID/figure$run_ID.pdf

cp $output_directory/ic$run_ID/SingleIC/ExpressionData.csv $output_directory/ExpData/ExpressionData$run_ID.csv

((run_ID++))
done

cd $the_directory
python3 exp-data_sampler.py

cd $bool_directory
python3 visualize.py
