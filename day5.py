if __name__ == '__main__':

    # ------------------- Part 1 -----------------------
    stack1 = ["F", "C", "P", "G", "Q", "R"]
    stack2 = ["W", "T", "C", "P"]
    stack3 = ["B", "H", "P", "M", "C"]
    stack4 = ["L", "T", "Q", "S", "M", "P", "R"]
    stack5 = ["P", "H", "J", "Z", "V", "G", "N"]
    stack6 = ["D", "P", "J"]
    stack7 = ["L", "G", "P", "Z", "F", "J", "T", "R"]
    stack8 = ["N", "L", "H", "C", "F", "P", "T", "J"]
    stack9 = ["G", "V", "Z", "Q", "H", "T", "C", "W"]
    stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

    with open("inputs/day5.txt") as f:
        # Skips first 10 lines
        line_counter = 0
        for line in f:
            line_counter += 1
            if line_counter <= 10:
                continue

            line_split = line.strip().split()
            boxes_to_move = int(line_split[1])
            initial_stack = int(line_split[3]) - 1
            destination_stack = int(line_split[5]) - 1

            for i in range(boxes_to_move):
                moved_element = stacks[initial_stack].pop()
                stacks[destination_stack].append(moved_element)

        for stack in stacks:
            print(stack.pop())

    # ------------------- Part 2 -----------------------
    print("-----------------part2-----------------")
    stack1 = ["F", "C", "P", "G", "Q", "R"]
    stack2 = ["W", "T", "C", "P"]
    stack3 = ["B", "H", "P", "M", "C"]
    stack4 = ["L", "T", "Q", "S", "M", "P", "R"]
    stack5 = ["P", "H", "J", "Z", "V", "G", "N"]
    stack6 = ["D", "P", "J"]
    stack7 = ["L", "G", "P", "Z", "F", "J", "T", "R"]
    stack8 = ["N", "L", "H", "C", "F", "P", "T", "J"]
    stack9 = ["G", "V", "Z", "Q", "H", "T", "C", "W"]
    stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

    with open("inputs/day5.txt") as f:
        # Skips first 10 lines
        line_counter = 0
        for line in f:
            line_counter += 1
            if line_counter <= 10:
                continue

            line_split = line.strip().split()
            boxes_to_move = int(line_split[1])
            initial_stack = int(line_split[3]) - 1
            destination_stack = int(line_split[5]) - 1

            for i in range(boxes_to_move)[::-1]:
                element_index = len(stacks[initial_stack]) - (i + 1)
                moved_element = stacks[initial_stack].pop(element_index)
                stacks[destination_stack].append(moved_element)

        for stack in stacks:
            print(stack.pop())
