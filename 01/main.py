def read_file(path):
    with open(path) as infile:
        return [line.rstrip() for line in infile]

def main():
    lines = read_file('input.txt')

    elf_cumm = 0
    elf_totals = []

    for line in lines:
        if line != "":
            elf_cumm += int(line)
        else:
            elf_totals.append(elf_cumm)
            
            elf_cumm = 0

    totals = sorted(elf_totals, reverse=True)

    print("Top: ", totals[0])
    print("Top 3 total: ", sum(totals[:3]))

if __name__ == '__main__':
    main()