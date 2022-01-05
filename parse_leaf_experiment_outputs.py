
import sys
import numpy as np

total_rounds = 1000
clients_per_round = 5

# fileprefix = '/Users/amrutham/Desktop/LEAF_Results/FEMNIST-OAM-Layer6/FEMNIST-OAM-Layer6-2000-rounds/FEMNIST_Layer6_0.0001/'
fileprefix = sys.argv[1]

accuracy_file = fileprefix+"accuracy.out"
metrics_sys_file = fileprefix+"metrics_sys.csv"
summary_output_file = open(fileprefix+"summary_output.txt", "w")

######################################
# Parsing accuracy.out file 
######################################
train_accuracy = []
train_loss = []
test_accuracy = []
test_loss = []
with open(accuracy_file) as fp:
    line = fp.readline()
    while line:
        if "train_accuracy" in line:            
            parsed_value = line.split(",")[0].split(": ")[1]
            train_accuracy.append(parsed_value)
        elif "train_loss" in line:
            parsed_value = line.split(",")[0].split(": ")[1]
            train_loss.append(parsed_value)
        elif "test_accuracy" in line:
            parsed_value = line.split(",")[0].split(": ")[1]
            test_accuracy.append(parsed_value)
        elif "test_loss" in line:
            parsed_value = line.split(",")[0].split(": ")[1]
            test_loss.append(parsed_value)
        line = fp.readline()

# Print test_accuracy
summary_output_file.write("==============\n")
summary_output_file.write("Test_Accuracy\n")
summary_output_file.write("==============\n")
for val in test_accuracy:
    summary_output_file.write(val+"\n")
summary_output_file.write("==============\n\n")

# Print test_loss
summary_output_file.write("==============\n")
summary_output_file.write("Test_Loss\n")
summary_output_file.write("==============\n")
for val in test_loss:
    summary_output_file.write(val+"\n")
summary_output_file.write("==============\n\n")

# Print train_accuracy
summary_output_file.write("==============\n")
summary_output_file.write("Train_Accuracy\n")
summary_output_file.write("==============\n")
for val in train_accuracy:
    summary_output_file.write(val+"\n")
summary_output_file.write("==============\n\n")

# Print train_loss
summary_output_file.write("==============\n")
summary_output_file.write("Train_Loss\n")
summary_output_file.write("==============\n")
for val in train_loss:
    summary_output_file.write(val+"\n")
summary_output_file.write("==============\n\n")




######################################
# Parsing metrics_sys.csv file 
######################################
before_nonzeros_count = []
after_nonzeros_count = []
received_nonzeros_count = []
train_time_count = []
compression_rate = []
if sum(1 for line in open(metrics_sys_file)) == total_rounds*clients_per_round:
    before_nonzeros_count_per_round = np.zeros((total_rounds, clients_per_round))
    after_nonzeros_count_per_round = np.zeros((total_rounds, clients_per_round))
    received_nonzeros_count_per_round = np.zeros((total_rounds, clients_per_round))
    train_time_count_per_round = np.zeros((total_rounds, clients_per_round))
    with open(metrics_sys_file) as fp:
        line = fp.readline()
        client_count = 0
        while line:
            if client_count == 5:
                client_count = 0                                
            round_number = int(line.split(",")[1])-1
            before = int(line.split(",")[5])
            after = int(line.split(",")[6])
            train_time = int(line.split(",")[7])
            received = int(line.split(",")[8])
            before_nonzeros_count_per_round[round_number][client_count] = before
            after_nonzeros_count_per_round[round_number][client_count] = after
            received_nonzeros_count_per_round[round_number][client_count] = after
            train_time_count_per_round[round_number][client_count] = train_time
            client_count = client_count + 1
            line = fp.readline()
    before_nonzeros_count = np.sum(before_nonzeros_count_per_round, axis=1)
    after_nonzeros_count = np.sum(after_nonzeros_count_per_round, axis=1)
    received_nonzeros_count = np.sum(received_nonzeros_count_per_round, axis=1)
    train_time_count = np.sum(train_time_count_per_round, axis=1)
    temp = []
    temp_sum = 0
    for idx, val in enumerate(before_nonzeros_count):
        temp_sum = temp_sum + val
        if (idx+1)%20 == 0:
            temp.append(temp_sum)
            temp_sum = 0
    before_nonzeros_count = temp
    temp = []
    temp_sum = 0
    for idx, val in enumerate(after_nonzeros_count):
        temp_sum = temp_sum + val
        if (idx+1)%20 == 0:
            temp.append(temp_sum)
            temp_sum = 0
    after_nonzeros_count = temp
    temp = []
    temp_sum = 0
    for idx, val in enumerate(received_nonzeros_count):
        temp_sum = temp_sum + val
        if (idx+1)%20 == 0:
            temp.append(temp_sum)
            temp_sum = 0
    received_nonzeros_count = temp
    temp = []
    temp_sum = 0
    for idx, val in enumerate(train_time_count):
        temp_sum = temp_sum + val
        if (idx+1)%20 == 0:
            temp.append(temp_sum)
            temp_sum = 0
    train_time_count = temp
    compression_rate = [((before-after)/before) for before, after in zip(before_nonzeros_count, after_nonzeros_count)]
else:
    print("MISCONFIGURATION (OR) PARSING LOGIC PROBLEM (OR) FILE FORMAT ISSUE")
    exit

# before_nonzeros_count
summary_output_file.write("==============\n")
summary_output_file.write("Before_Compression_Nonzeros_Counts\n")
summary_output_file.write("==============\n")
for val in before_nonzeros_count:
    summary_output_file.write(str(val)+"\n")
summary_output_file.write("==============\n\n")

# after_nonzeros_count
summary_output_file.write("==============\n")
summary_output_file.write("After_Compression_Nonzeros_Counts\n")
summary_output_file.write("==============\n")
for val in after_nonzeros_count:
    summary_output_file.write(str(val)+"\n")
summary_output_file.write("==============\n\n")

# received_nonzeros_count
summary_output_file.write("==============\n")
summary_output_file.write("Received_Nonzeros_Counts\n")
summary_output_file.write("==============\n")
for val in received_nonzeros_count:
    summary_output_file.write(str(val)+"\n")
summary_output_file.write("==============\n\n")

# train_time_count
summary_output_file.write("==============\n")
summary_output_file.write("Train_Time_In_Secs\n")
summary_output_file.write("==============\n")
for val in train_time_count:
    summary_output_file.write(str(val)+"\n")
summary_output_file.write("==============\n\n")

# compression_rate
summary_output_file.write("==============\n")
summary_output_file.write("Compression_Rate\n")
summary_output_file.write("==============\n")
for val in compression_rate:
    summary_output_file.write(str(val)+"\n")
summary_output_file.write("==============\n\n")

summary_output_file.close()
