if __name__ == '__main__':

    # ------------------- Part 1 -----------------------
    with open("inputs/day2.txt") as f:
        accumulated_score = 0
        for line in f:
            results = line.split()

            # A=rock, B=Paper, C=Scissors
            if results[0] == "A" and results[1] == "X":
                accumulated_score += 4
            if results[0] == "A" and results[1] == "Y":
                accumulated_score += 8
            if results[0] == "A" and results[1] == "Z":
                accumulated_score += 3
            if results[0] == "B" and results[1] == "X":
                accumulated_score += 1
            if results[0] == "B" and results[1] == "Y":
                accumulated_score += 5
            if results[0] == "B" and results[1] == "Z":
                accumulated_score += 9
            if results[0] == "C" and results[1] == "X":
                accumulated_score += 7
            if results[0] == "C" and results[1] == "Y":
                accumulated_score += 2
            if results[0] == "C" and results[1] == "Z":
                accumulated_score += 6

        print(accumulated_score)

        # ------------------- Part 2 -----------------------

    with open("inputs/day2.txt") as f:
        accumulated_score = 0
        for line in f:
            results = line.split()

            # A=rock, B=Paper, C=Scissors - X=lose, Y=tie, z=win
            if results[0] == "A" and results[1] == "X":
                accumulated_score += 3
            if results[0] == "A" and results[1] == "Y":
                accumulated_score += 4
            if results[0] == "A" and results[1] == "Z":
                accumulated_score += 8
            if results[0] == "B" and results[1] == "X":
                accumulated_score += 1
            if results[0] == "B" and results[1] == "Y":
                accumulated_score += 5
            if results[0] == "B" and results[1] == "Z":
                accumulated_score += 9
            if results[0] == "C" and results[1] == "X":
                accumulated_score += 2
            if results[0] == "C" and results[1] == "Y":
                accumulated_score += 6
            if results[0] == "C" and results[1] == "Z":
                accumulated_score += 7

        print(accumulated_score)


