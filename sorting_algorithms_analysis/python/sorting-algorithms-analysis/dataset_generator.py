import random

dataset_count = input("Datasets to generate:")
dataset_range = int(input("How many numbers in each dataset?:"))

dataset_list = []
for dataset_id in range(1, int(dataset_count) + 1):
    dataset_directory = "DataSet/"

    dataset_unsorted_name = dataset_directory + "dataSet" + str(dataset_id) + ".txt"
    dataset_sorted_name = dataset_directory + "dataSet" + str(dataset_id) + "_sorted.txt"
    dataset_reverse_sorted_name = dataset_directory + "dataSet" + str(dataset_id) + "_reverse.txt"

    # generating and writing unsorted dataset
    with open(dataset_unsorted_name, mode='w') as dataset_file:
        for i in range(dataset_range):
            random_number = random.randint(1, 100000)
            dataset_file.write("%s\n" % random_number)
            dataset_list.append(random_number)

    #  generating and writing sorted dataset
    dataset_list.sort()
    with open(dataset_sorted_name, 'w') as dataset_sorted_file:
        for number in dataset_list:
            dataset_sorted_file.write("%s\n" % number)

    #  generating and writing reverse sorted dataset
    dataset_list.sort(reverse=True)
    with open(dataset_reverse_sorted_name, 'w') as dataset_reverse_sorted_file:
        for number in dataset_list:
            dataset_reverse_sorted_file.write("%s\n" % number)

