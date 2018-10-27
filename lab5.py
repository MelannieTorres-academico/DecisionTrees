import fileinput
import math
import numpy as np
import pandas as pd

relation = ""
attributes = {}

def calculate_entropy(occurrences, total_elements):
    result = 0
    for element in occurrences:
        result = result - (element / total_elements * math.log2(element / total_elements))
    print("Entropy: {0}".format(result))


def count_occurrences(dataframe, attribute):
    occurrences = []
    for option in attribute:
        total_count = 0
        for d in dataframe:
            total_count = total_count+d.count(option)
        print("{0}: {1}".format(option, total_count))
        occurrences.append(total_count)
    print(occurrences)
    return occurrences


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
    print("attributes dictionary:")
    print(attributes)
    dataframe = format_data(lines[data_index + 1:input_len])
    print("\nfull dataframe:")
    print(dataframe)

    # Counts the occurrences and calculates entropy of the dataframe
    '''
    for key in attributes.keys():
        occurrences = countOccurrences(full_data, attributes[key])
        calculateEntropy(occurrences, len(full_data))
    '''


if __name__ == "__main__":
    main()
