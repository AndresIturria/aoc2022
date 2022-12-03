def get_value(letter):
    if letter.isupper():
        letter_value = ord(letter) - 38

    else:
        letter_value = ord(letter) - 96

    return letter_value


if __name__ == '__main__':

    # ------------------- Part 1 -----------------------
    with open("inputs/day3.txt") as f:
        answer = []
        for line in f:
            line_list = []
            line_list[:0] = line.strip()
            middle = int(len(line_list) / 2)
            first_compartment = line_list[:middle]
            second_compartment = line[middle:]

            repeated = []
            for letter in first_compartment:
                if (letter in second_compartment) and (letter not in repeated):
                    repeated.append(letter)
                    answer.append(letter)

        accumulator = 0
        for letter in answer:
            value = get_value(letter)
            accumulator += value

        print(accumulator)

        # ------------------- Part 2 -----------------------
        with open("inputs/day3.txt") as f:
            counter = 0
            group = []
            accumulator = 0
            for line in f:
                group.append(line.strip())
                counter += 1
                if counter == 3:
                    repeated = []
                    badge = ""
                    for letter in group[0]:
                        if letter in group[1]:
                            repeated.append(letter)
                    for letter in repeated:
                        if letter in group[2]:
                            badge = letter

                    accumulator += get_value(badge)
                    counter = 0
                    group = []

            print(accumulator)






