def fully_contains(part1, part2):
    part1_int = [int(x) for x in part1]
    part2_int = [int(x) for x in part2]
    if (part1_int[0] <= part2_int[0] and part1_int[1] >= part2_int[1]) or (part2_int[0] <= part1_int[0] and part2_int[1] >= part1_int[1]):
        return 1
    else:
        return 0


def overlap(part1, part2):
    part1_int = [int(x) for x in part1]
    part2_int = [int(x) for x in part2]
    range1 = range(part1_int[0], part1_int[1] + 1)
    range2 = range(part2_int[0], part2_int[1] + 1)
    if (part2_int[0] in range1 or part2_int[1] in range1) or (part1_int[0] in range2 or part1_int[1] in range2):
        return 1
    else:
        return 0


if __name__ == '__main__':

    # ------------------- Part 1 -----------------------
    with open("inputs/day4.txt") as f:
        accumulator = 0
        for line in f:
            line_lst = line.strip().split(",")
            part1 = line_lst[0].split("-")
            part2 = line_lst[1].split("-")
            accumulator += fully_contains(part1, part2)
        print(accumulator)

    # ------------------- Part 2 -----------------------
    with open("inputs/day4.txt") as f:
        accumulator = 0
        for line in f:
            line_lst = line.strip().split(",")
            part1 = line_lst[0].split("-")
            part2 = line_lst[1].split("-")
            accumulator += overlap(part1, part2)
        print(accumulator)
