import fileinput
import math
import pandas as pd
import numpy as np

relation = ""
attributes = {}

# Calculates the entropy
# dataframe= rows that should be taken into accoutn
# result name of the column name of the output (ex. play)
def calculate_entropy(dataframe, result):
    occurrences = count_occurrences(dataframe, result)
    total_elements=dataframe.shape[0]
    result = 0
    for occurrence in occurrences:
        element=occurrences[occurrence]
        result = result - (element / total_elements * math.log2(element / total_elements))
    #print("Entropy: {0}".format(result))
    return result


# Calculates the entropy of the given possible child
# dataframe: full dataframe
# headers without including the outputs
# outputs name of the column with the possible outputs (ex: play)
def calculate_entropy_TX(dataframe, p, outputs):
    total_rows = dataframe.shape[0]
    result=0
    filtered_rows = dataframe[p].value_counts().to_dict()
    for option in filtered_rows:
        #filter rows where equal to first possibility (p) and call calculate_entropy
        aux_entropy = calculate_entropy(dataframe[dataframe[p] == option], outputs)
        aux_row_count = dataframe[dataframe[p] == option].shape[0]
        result = result+(aux_row_count/total_rows*aux_entropy)
    #print("Entropy {0}: {1}".format(option, result))
    return result

# Calculates the information gain
#
def calculate_information_gain(dataframe, p, outputs, current_entropy):
    entropy_tx = calculate_entropy_TX(dataframe, p, outputs)
    return current_entropy-entropy_tx

# Stores in a dictionary how many times each value of the result occurs in the given part of the dataframe
# Output example {"yes":9, "no":4}
def count_occurrences(dataframe, result):
    possible_attributes = attributes[result]
    occurrences = []
    total_count = dataframe[result].value_counts()
    return total_count.to_dict()



def format_header(header):
    name = header.replace("@attribute", "").split('{')[0].replace(" ", "")
    possible_values = header.replace("\n", "").replace("}", "").replace(" ", "").split('{')[1].split(',')
    # add to dictionary
    attributes[name] = possible_values


def format_data(data):
    matrix_data = []
    for i in range(0, len(data)):
        # add to row to matrix_data
        matrix_data.append(data[i].replace("\n", "").split(","))
    # transform matrix to numpy matrix
    np_matrix_data = np.matrix(matrix_data)
    # create dataframe from numpy matrix
    dataframe = pd.DataFrame(np_matrix_data)
    # add column names form the attributes dictionary
    dataframe.columns = attributes.keys()
    return dataframe


def generate_tree_model(dataframe, attributes):
    # ...
    return


def main():
    # example input
    file_input = fileinput.input()
    lines = []
    for x in file_input:
        if x[0] != '%':
            lines.append(x)

    input_len = len(lines)
    data_index = 0
    for i in range(0, input_len):
        header = lines[i].split(" ")[0]

        if "@attribute" in header:
                format_header(lines[i])
        elif "@data" in header:
            data_index = i
            break
    # print("attributes dictionary:")
    # print(attributes)
    dataframe = format_data(lines[data_index + 1:input_len])
    print("\nfull dataframe:")
    print(dataframe)


    headers = list(dataframe.columns.values) # get the headers (ex. outlook temperature humidity  windy play)
    result = headers[-1] # get the last value of the headers (ex. play)
    current_entropy = calculate_entropy(dataframe, result)

    #calculate Information gain of each possible child
    for possibility in headers[:-1]:
        information_gain = calculate_information_gain(dataframe, possibility, result, current_entropy)
        print("Information gain: {0}".format(information_gain))



if __name__ == "__main__":
    main()
