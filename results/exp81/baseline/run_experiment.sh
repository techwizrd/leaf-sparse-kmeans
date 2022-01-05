#!/usr/bin/env bash

# This file is mostly for documentation. It's not a functioning script.

EXPERIMENT_NAME="baseline"
PROJ_ROOT=""
MODELS_FOLDER="$PROJ_ROOT/models/"
OUTPUT_PATH="$PROJ_ROOT/results/$EXPERIMENT_NAME"


# Clean up old metrics
#rm -rvf metrics/metrics_stat.csv
#rm -rvf metrics/metrics_sys.csv

# Copy client.py to models folder
#cp -rv client.py

# Run experiment
python main.py \
	-dataset femnist \
	-model cnn \
	-lr 0.001

# Copy results
cp -rvf metrics/metrics_stat.csv $EXP_PATH/metrics_stat.csv
cp -rvf metrics/metrics_sys.csv $EXP_PATH/metrics_sys.csv

# Produce plots
