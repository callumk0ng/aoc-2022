def read_file(input):
    with open(input) as infile:
        return [line.rstrip() for line in infile]

def main():
    lines = read_file('input.txt')

    values = [line.split(" ") for line in lines]

    game_1_total = 0
    game_2_total = 0
        
    for game in values:
        my_value = lookup(game[1])

        result = lookup_result(game[1])

        game_1_total += calculate_result(my_value, lookup(game[0]))
        game_1_total += my_value

        game_2_total += result
        game_2_total += calculate_option(result, lookup(game[0]))

    print("Part 1: ", game_1_total)
    print("Part 2: ", game_2_total)

def lookup(value):
    return {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3 
    }[value]

def lookup_result(value):
    return {
        "X": 0,
        "Y": 3,
        "Z": 6
    }[value]

def calculate_option(result, value):
    if result == 3:
        return value
    
    if value == 1:
        return 3 if result == 0 else 2
    elif value == 2:
        return 1 if result == 0 else 3
    else:
        return 2 if result == 0 else 1

def calculate_result(value1, value2):
    if value1 == value2:
        return 3
    elif (
        (value1 == 3 and value2 == 2) or
        (value1 == 2 and value2 == 1) or
        (value1 == 1 and value2 == 3) 
    ):
        return 6
    else:
        return 0

if __name__ == '__main__':
    main()