def read_file(file_name):
    with open(file_name) as infile:
        return infile.read()

def find_marker(data, sequence_size=0):
    comparison_size = sequence_size - 1

    for index, char in enumerate(data):
        if index < comparison_size:
            continue

        chars = list(set(data[index-comparison_size:index]))

        if char not in chars and len(chars) == comparison_size:
            return index + 1

def main():
    data = read_file('input.txt')

    marker_index = find_marker(data, sequence_size=4)
    updated_marker_index = find_marker(data, sequence_size=14)

    print("Position of first non-repeated character in 4 char sequence:", marker_index)
    print("Position of first non-repeated character in 14 char sequence:", updated_marker_index)

if __name__ == '__main__':
    main()