#!/usr/bin/env sh

set -e

DIR="/home/vsarkhel/Projects/fedtest/leaf-k"
MODELS_DIR="$DIR/models"
RESULTS_DIR="$DIR/results/exp85"

# stc_10
EXPERIMENT="stc_10"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.10/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# stc_20
EXPERIMENT="stc_20"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.20/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# stc_30
EXPERIMENT="stc_30"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.30/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# stc_40
EXPERIMENT="stc_40"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.40/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# stc_50
EXPERIMENT="stc_50"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.50/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# stc_60
EXPERIMENT="stc_60"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.60/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# stc_70
EXPERIMENT="stc_70"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.70/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# stc_80
EXPERIMENT="stc_80"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.80/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# stc_90
EXPERIMENT="stc_90"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.90/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

