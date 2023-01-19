class Buffer:
    def __init__(self, maxSize):
        self.buffer = []
        self.maxSize = maxSize

    def add(self, item):
        if len(self.buffer) < self.maxSize:
            self.buffer.append(item)
        else:
            self.buffer.pop(0)
            self.buffer.append(item)

    def check(self):
        set_check = set(self.buffer)
        if buffer.maxSize == len(self.buffer):
            return len(set_check) == len(self.buffer)

        else:
            return False


if __name__ == '__main__':

    # ------------------- Part 1 -----------------------

    with open("inputs/day6.txt") as f:
        for line in f:
            buffer = Buffer(4)
            char_counter = 0

            for char in line:
                char_counter += 1
                buffer.add(char)
                if buffer.check():
                    break

            print(char_counter)

    # ------------------- Part 2 -----------------------
    with open("inputs/day6.txt") as f:
        for line in f:
            buffer = Buffer(14)
            char_counter = 0

            for char in line:
                char_counter += 1
                buffer.add(char)
                if buffer.check():
                    break

            print(char_counter)






