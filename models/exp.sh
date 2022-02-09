#!/usr/bin/env sh

set -e

DIR="/home/vsarkhel/Projects/fedtest/leaf-k"
MODELS_DIR="$DIR/models"
RESULTS_DIR="$DIR/results/exp85"

# randk_10
EXPERIMENT="randk_10"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.10/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# randk_20
#EXPERIMENT="randk_20"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.20/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# randk_30
EXPERIMENT="randk_30"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.30/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# randk_40
EXPERIMENT="randk_40"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.40/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# randk_50
EXPERIMENT="randk_50"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.50/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# randk_60
EXPERIMENT="randk_60"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.60/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# randk_70
EXPERIMENT="randk_70"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.70/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# randk_80
EXPERIMENT="randk_80"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.80/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

# randk_90
EXPERIMENT="randk_90"
echo "cd $MODELS_DIR"
sed "s/space_savings = 0.10/space_savings = 0.90/" client.py.template > client.py
unbuffer time python3 main.py --clients-per-round 5 -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
mkdir -pv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/accuracy.out "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_sys.csv "$RESULTS_DIR/$EXPERIMENT/"
mv -v metrics/metrics_stat.csv "$RESULTS_DIR/$EXPERIMENT/"
cp -rv client.py "$RESULTS_DIR/$EXPERIMENT/"

