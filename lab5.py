import fileinput
import math
relation = ""
attributes = {}
full_data=[]


def calculateEntropy(occurrences, total_elements):
    result=0
    for element in occurrences:
         result=result-(element/total_elements*math.log2(element/total_elements))
    print("Entropy: {0}".format(result))

def countOccurrences(dataset, attribute):
    occurrences = []
    for option in attribute:
        total_count=0
        for d in dataset:
            total_count=total_count+d.count(option)
        print("{0}: {1}".format(option, total_count))
        occurrences.append(total_count)
    print(occurrences)
    return occurrences


def format_header(header):
    name = header.replace("@attribute","").split('{')[0].replace(" ", "")
    possible_values = header.replace("\n","").replace("}","").replace(" ", "").split('{')[1].split(',')
    #add to dictionary
    attributes[name]=possible_values



def format_data(data):
    for i in range (0, len(data)):
        #add to full_data
        full_data.append(data[i].replace("\n", "").split(","))


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
    format_data(lines[data_index + 1:input_len])
    # print("full dictionary:")
    # print(full_data)

    # Counts the occurrences and calculates entropy of the dataset
    for key in attributes.keys():
        occurrences = countOccurrences(full_data, attributes[key])
        calculateEntropy(occurrences, len(full_data))

if __name__ == "__main__":
    main()
