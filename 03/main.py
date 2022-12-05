import string

char_array = string.ascii_letters.replace('', ' ').split()

def read_file(input):
    with open(input) as infile:
        return [line.rstrip() for line in infile]

def split_str_into_tuple(value):
    mid_point = int(len(value) / 2)
    return value[:mid_point], value[mid_point:]

def get_value(char):
    return char_array.index(char) + 1

def get_matching_chars(value1, value2):
    return set(value1).intersection(value2)

def main():
    lines = read_file('input.txt')

    total_matching = 0
    group_totals = 0

    groups = []
    group_index = 0

    for index, line in enumerate(lines):
        if index == 0:
            groups.append([line])
        elif index % 3 == 0:
            groups.append([line])
            group_index += 1
        else:
            groups[group_index].append(line)

        first_half, second_half = split_str_into_tuple(line)
        
        matching_chars = get_matching_chars(first_half, second_half)

        value = sum([get_value(char) for char in matching_chars]) if matching_chars else 0

        total_matching += value

    for group in groups:
        matching_chars = get_matching_chars(get_matching_chars(group[0], group[1]), group[2])

        value = sum([get_value(char) for char in matching_chars]) if matching_chars else 0

        group_totals += value

    print("Total matching: ", total_matching)

    print("Group total matching: ", group_totals)

if __name__ == '__main__':
    main()