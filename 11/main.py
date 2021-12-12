class Board:
    def __init__(self, grid):
        self.count = 0
        self.steps = 0
        self.grid = self.parse(grid)

    @classmethod
    def parse(cls, grid: list[list[int]]):
        out = []
        for row in grid:
            r = []
            for elem in row:
                r.append(int(elem))
            out.append(r)
        return out


    def display(self):
        for row in self.grid:
            r = [f"{int(i):02d}" for i in row]
            print(r)
        print("\n")

    def increase_all_by(self, number):
        for y, row in enumerate(self.grid):
            for x, _ in enumerate(row):
                self.safe_increase_by(1, x, y)

    def safe_increase_by(self, number: int, x: int, y: int):
        if 0 <= y < len(self.grid):
            if 0 <= x < len(self.grid[0]):
                self.grid[y][x] += number
                # print(f"increasing  {x},{y}")

    def process_flash(self, x: int, y: int):
        print(f"processing [{x},{y}] {self.grid[y][x]}")
        self.safe_increase_by(1, x - 1, y - 1)  # top left
        self.safe_increase_by(1, x, y - 1)  # top middle
        self.safe_increase_by(1, x + 1, y - 1)  # top right
        self.safe_increase_by(1, x - 1, y)  # middle left
        self.safe_increase_by(1, x, y)  # middle
        self.safe_increase_by(1, x + 1, y)  # middle right
        self.safe_increase_by(1, x - 1, y + 1)  # bottom left
        self.safe_increase_by(1, x, y + 1)  # bottom
        self.safe_increase_by(1, x + 1, y + 1)  # bottom right

    def flash(self):
        for y, row in enumerate(self.grid):
            for x, elem in enumerate(row):
                if int(elem) > 9:
                    self.process_flash(x, y)

    def count_and_reset(self):
        for y, row in enumerate(self.grid):
            for x, elem in enumerate(row):
                if int(elem) >= 10:
                    self.count += 1
                    self.grid[y][x] = 0

    def step(self):
        banner(self.steps)
        self.display()
        self.increase_all_by(1)
        print("after increase:")
        self.display()
        self.flash()
        print("after flash:")
        self.display()
        self.count_and_reset()
        print("after count and reset:")
        self.display()
        self.steps += 1
        print(f"finished step: {self.steps}")
        print(f"count: {self.count}")
        self.display()


def banner(steps):
    print("#" * 40)
    print(" " * 10 + f" Starting Step: {steps+1}")
    print("#" * 40)


def first(grid):
    board = Board(grid)
    for _ in range(10):
        board.step()


# def second(grid):
# return grid

f = "11/test_inputs.txt"
# f = "11/smaller_test.txt"
# f = "11/inputs.txt"

with open(f, "r") as f:
# import sys
# with open(sys.argv[1], "r") as f:
    grid = [list(line.strip()) for line in f.readlines() if line.strip()]

print(first(grid))

# print(second(lines))
