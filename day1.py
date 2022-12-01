if __name__ == '__main__':

    # ------------------- Part 1 -----------------------
    with open("inputs/day1.txt") as f:
        accumulator = 0
        elves = []
        for line in f:
            if line == "\n":
                elves.append(accumulator)
                accumulator = 0;

            else:
                accumulator += int(line)

    print(max(elves))
    # ---------------------- Part 2 ---------------------
    accumulator = 0
    for elf in range(3):
        accumulator += elves.pop(elves.index(max(elves)))

    print(accumulator)
