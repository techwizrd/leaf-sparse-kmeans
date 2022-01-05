#!/usr/bin/env python3

import glob
import numpy as np
import os
import sys

total_rounds = 1000
clients_per_round = 5
aggregate_rounds = 20
expected_rows = int(total_rounds/aggregate_rounds)

fileprefix = sys.argv[1]
sf_list = glob.glob(f'{fileprefix}/*/summary_output.txt', recursive=True)


def get_exp_name(sf_file):
    return sf_file[len(fileprefix):-len('/summary_output.txt')]


exp_names = sorted([get_exp_name(sf_file) for sf_file in sf_list])
out_headers = ','.join(exp_names)
print(f'Experiments: {exp_names}')

test_accuracy = []
test_loss = []
train_accuracy = []
train_loss = []
before_compression_nonzeros_counts = []
after_compression_nonzeros_counts = []
received_nonzeros_counts = []
train_time_in_secs = []
compression_rate = []
dummy_element = [0.00]
test_accuracy.append(dummy_element)
test_loss.append(dummy_element)
train_accuracy.append(dummy_element)
train_loss.append(dummy_element)
for _ in range(expected_rows):
    test_accuracy.append(dummy_element)
    test_loss.append(dummy_element)
    train_accuracy.append(dummy_element)
    train_loss.append(dummy_element)
    before_compression_nonzeros_counts.append(dummy_element)
    after_compression_nonzeros_counts.append(dummy_element)
    received_nonzeros_counts.append(dummy_element)
    train_time_in_secs.append(dummy_element)
    compression_rate.append(dummy_element)

for summary_output_file in sf_list:
    print(f'Reading {summary_output_file}')
    test_accuracy_sf = []
    test_loss_sf = []
    train_accuracy_sf = []
    train_loss_sf = []
    before_compression_nonzeros_counts_sf = []
    after_compression_nonzeros_counts_sf = []
    received_nonzeros_counts_sf = []
    train_time_in_secs_sf = []
    compression_rate_sf = []
    current_metric_sf = ""
    with open(summary_output_file) as fp:
        line = fp.readline()
        while line:
            if "Test_Accuracy" in line:
                current_metric = "Test_Accuracy"
            elif "Test_Loss" in line:
                current_metric = "Test_Loss"
            elif "Train_Accuracy" in line:
                current_metric = "Train_Accuracy"
            elif "Train_Loss" in line:
                current_metric = "Train_Loss"
            elif "Before_Compression_Nonzeros_Counts" in line:
                current_metric = "Before_Compression_Nonzeros_Counts"
            elif "After_Compression_Nonzeros_Counts" in line:
                current_metric = "After_Compression_Nonzeros_Counts"
            elif "Received_Nonzeros_Counts" in line:
                current_metric = "Received_Nonzeros_Counts"
            elif "Train_Time_In_Secs" in line:
                current_metric = "Train_Time_In_Secs"
            elif "Compression_Rate" in line:
                current_metric = "Compression_Rate"
            line = line.replace("\n", "")
            if line and ("=" not in line) and not line.lower().islower():
                line = float(line)
                if current_metric == "Test_Accuracy":
                    test_accuracy_sf.append([line])
                elif current_metric == "Test_Loss":
                    test_loss_sf.append([line])
                elif current_metric == "Train_Accuracy":
                    train_accuracy_sf.append([line])
                elif current_metric == "Train_Loss":
                    train_loss_sf.append([line])
                elif current_metric == "Before_Compression_Nonzeros_Counts":
                    before_compression_nonzeros_counts_sf.append([line])
                elif current_metric == "After_Compression_Nonzeros_Counts":
                    after_compression_nonzeros_counts_sf.append([line])
                elif current_metric == "Received_Nonzeros_Counts":
                    received_nonzeros_counts_sf.append([line])
                elif current_metric == "Train_Time_In_Secs":
                    train_time_in_secs_sf.append([line])
                elif current_metric == "Compression_Rate":
                    compression_rate_sf.append([line])
            line = fp.readline()
    test_accuracy_temp = test_accuracy
    test_accuracy = np.append(test_accuracy_temp, test_accuracy_sf, axis=1)
    test_loss_temp = test_loss
    test_loss = np.append(test_loss_temp, test_loss_sf, axis=1)
    train_accuracy_temp = train_accuracy
    train_accuracy = np.append(train_accuracy_temp, train_accuracy_sf, axis=1)
    train_loss_temp = train_loss
    train_loss = np.append(train_loss_temp, train_loss_sf, axis=1)
    before_compression_nonzeros_counts_temp = before_compression_nonzeros_counts
    before_compression_nonzeros_counts = np.append(before_compression_nonzeros_counts_temp, before_compression_nonzeros_counts_sf, axis=1)
    after_compression_nonzeros_counts_temp = after_compression_nonzeros_counts
    after_compression_nonzeros_counts = np.append(after_compression_nonzeros_counts_temp, after_compression_nonzeros_counts_sf, axis=1)
    received_nonzeros_counts_temp = received_nonzeros_counts
    received_nonzeros_counts = np.append(received_nonzeros_counts_temp, received_nonzeros_counts_sf, axis=1)
    train_time_in_secs_temp = train_time_in_secs
    train_time_in_secs = np.append(train_time_in_secs_temp, train_time_in_secs_sf, axis=1)
    compression_rate_temp = compression_rate
    compression_rate = np.append(compression_rate_temp, compression_rate_sf, axis=1)

summary_of_summaries_output_file_prefix = f'{sys.argv[1]}/summary_results/'
os.makedirs(summary_of_summaries_output_file_prefix, exist_ok=True)
print(f'Writing summaries to {summary_of_summaries_output_file_prefix}')
np.savetxt(summary_of_summaries_output_file_prefix+"test_accuracy.csv", test_accuracy, fmt='%.10f', delimiter=",", header=out_headers, comments='')
np.savetxt(summary_of_summaries_output_file_prefix+"test_loss.csv", test_loss, fmt='%.10f', delimiter=",", header=out_headers, comments='')
np.savetxt(summary_of_summaries_output_file_prefix+"train_accuracy.csv", train_accuracy, fmt='%.10f', delimiter=",", header=out_headers, comments='')
np.savetxt(summary_of_summaries_output_file_prefix+"train_loss.csv", train_loss, fmt='%.10f', delimiter=",", header=out_headers, comments='')
np.savetxt(summary_of_summaries_output_file_prefix+"before_compression_nonzeros_counts.csv", before_compression_nonzeros_counts, fmt='%i', delimiter=",", header=out_headers, comments='')
np.savetxt(summary_of_summaries_output_file_prefix+"after_compression_nonzeros_counts.csv", after_compression_nonzeros_counts, fmt='%i', delimiter=",", header=out_headers, comments='')
np.savetxt(summary_of_summaries_output_file_prefix+"received_nonzeros_counts.csv", received_nonzeros_counts, fmt='%i', delimiter=",", header=out_headers, comments='')
np.savetxt(summary_of_summaries_output_file_prefix+"train_time_in_secs.csv", train_time_in_secs, fmt='%i', delimiter=",", header=out_headers, comments='')
np.savetxt(summary_of_summaries_output_file_prefix+"compression_rate.csv", compression_rate, fmt='%.10f', delimiter=",", header=out_headers, comments='')
