import re

def read_file(input):
    with open(input) as infile:
        return [line.rstrip() for line in infile]

def read_n_chars(line, char_size=4):
    result = []
    for i in range(0, len(line), char_size):
        data_to_read = line[i:i+char_size]
        result.append(data_to_read)
    return result

def switch_dimensions(multid_array):
    result = []

    for index, arr in enumerate(multid_array):
        if index == 0:
            for element in arr:
                result.append([element])
        else:
            for result_index, element in enumerate(arr):
                result[result_index].append(element)

    return result

def tidy_up_stacks(stacks):
    result = []
    for stack in stacks:
        matching_crate = [crate.replace('[', '').replace(']', '') for crate in stack if crate != ""]
        matching_crate.reverse()
        result.append(matching_crate)
    return result

def extract_instructions(instruction):
    return re.findall(r"\b\d+\b", instruction)

def move(stacks, total, from_stack, to_stack, reverse=True):
    # Move last n from stack
    from_index = int(from_stack) - 1
    to_index = int(to_stack) - 1
    total = int(total)

    crates_to_move = stacks[from_index][len(stacks[from_index]) - total:]
    if reverse:
        crates_to_move.reverse()

    stacks[from_index] = stacks[from_index][:-total]
    stacks[to_index] = stacks[to_index] + crates_to_move
    return stacks

def main():
    lines = read_file('input.txt')

    blocks = []
    instructions = []

    formation_read = False

    for line in lines:
        if not formation_read and line != "" and "1" not in line:
            blocks.append([char.strip() for char in read_n_chars(line)])
        else:
            formation_read = True

        if formation_read and "move" in line:
            instructions.append(extract_instructions(line))

    ordered_stacks = switch_dimensions(blocks)

    original_stacks = tidy_up_stacks(ordered_stacks)

    update_stacks = original_stacks.copy()

    for total_to_move, from_stack, target_stack in instructions:
        original_stacks = move(original_stacks, total_to_move, from_stack, target_stack)
        update_stacks = move(update_stacks, total_to_move, from_stack, target_stack, reverse=False)

    original_last_crates = []
    update_last_crates = []

    for stack in original_stacks:
        original_last_crates.append(stack[-1])

    for stack in update_stacks:
        update_last_crates.append(stack[-1])

    print("Original - Last letters: ", "".join(original_last_crates))
    print("Update - Last letters: ", "".join(update_last_crates))


if __name__ == '__main__':
    main()