def read_file(input):
    with open(input) as infile:
        return [line.rstrip() for line in infile]

def split_line(line):
    return line.split(",")

def get_bounds(value):
    return value.split("-")

def get_comparable_range(values):
    values = [int(value) for value in values]
    return list(range(values[0], values[1] + 1))

def check_in_range(values, comparison, operator=all):
    comparable_range = get_comparable_range(comparison)
    return operator([int(value) in comparable_range for value in values])

def main():
    lines = read_file('input.txt')

    total_fully_in_range = 0

    total_overlap = 0

    for line in lines:
        ranges = split_line(line)

        bounds = []
        for value_range in ranges:
            bounds.append(get_bounds(value_range))
        
        first_in_range = check_in_range(bounds[0], bounds[1])
        second_in_range = check_in_range(bounds[1], bounds[0])

        if first_in_range or second_in_range:
            total_fully_in_range += 1

        first_overlap = check_in_range(bounds[0], bounds[1], operator=any)
        second_overlap = check_in_range(bounds[1], bounds[0], operator=any)

        if first_overlap or second_overlap:
            total_overlap += 1

    print("Total: ", total_fully_in_range)
    print("Total overlap: ", total_overlap)


if __name__ == '__main__':
    main()