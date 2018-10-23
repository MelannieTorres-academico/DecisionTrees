import fileinput


def main():
    # example input
    file_input = fileinput.input()
    line = []
    for x in file_input:
        if x[0] != '%':
            line.append(x)


if __name__ == "__main__":
    main()