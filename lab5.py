import fileinput
relation = ""
attribute = {}


def format_header(header):
    print(header)
    return


def format_data(data):
    print(data)
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
        if "@data" not in header:
            format_header(lines[i])
        else:
            data_index = i
            break

    format_data(lines[data_index + 1:input_len])


if __name__ == "__main__":
    main()
