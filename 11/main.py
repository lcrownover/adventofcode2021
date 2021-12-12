def display(grid):
    for row in grid:
        r = [f"{int(i):02d}" for i in row]
        print(r)
    print("\n")

def increase_all_by(number, grid):
    out = []
    for row in grid:
        out.append([int(i) + number for i in row])
    return out


def safe_increase_by(number, x, y, grid):
    if 0 <= y < len(grid):
        if 0 <= x < len(grid[0]):
            grid[y][x] += number
            print(f"increasing  {x},{y}")


def process_flash(x, y, grid):
    print(f"processing [{x},{y}] {grid[y][x]}")
    grid = grid.copy()
    safe_increase_by(1, x - 1, y - 1, grid)  # top left
    safe_increase_by(1, x, y - 1, grid)  # top middle
    safe_increase_by(1, x + 1, y - 1, grid)  # top right
    safe_increase_by(1, x - 1, y, grid)  # middle left
    safe_increase_by(1, x, y, grid)  # middle
    safe_increase_by(1, x + 1, y, grid)  # middle right
    safe_increase_by(1, x - 1, y + 1, grid)  # bottom left
    safe_increase_by(1, x, y + 1, grid)  # bottom
    safe_increase_by(1, x + 1, y + 1, grid)  # bottom right
    return grid


def flash(grid):
    grid = grid.copy()
    for y, row in enumerate(grid):
        for x, elem in enumerate(row):
            if int(elem) > 9:
                grid = process_flash(x, y, grid)
    return grid

def count_and_reset(grid, count):
    c = 0
    grid = grid.copy()
    for y, row in enumerate(grid):
        for x, elem in enumerate(row):
            if elem >= 10:
                c += 1
                grid[y][x] = 0
    return grid, c + count

def banner(steps):
    print("#"*40)
    print(" "*10 + f" Starting Step: {steps+1}")
    print("#"*40)


def first(grid):
    steps = 0
    count = 0
    while steps < 10:
        banner(steps)
        display(grid)
        grid = increase_all_by(1, grid)
        print("after increase:")
        display(grid)
        grid = flash(grid)
        print("after flash:")
        display(grid)
        grid, count = count_and_reset(grid, count)
        print("after count and reset:")
        display(grid)
        steps += 1
        print(f"finished step: {steps}")
        print(f"count: {count}")
        display(grid)
    return count


# def second(grid):
# return grid

# f = "10/test_inputs.txt"
# f = "10/inputs.txt"
import sys

with open(sys.argv[1], "r") as f:
    grid = [list(line.strip()) for line in f.readlines() if line.strip()]

print(first(grid))

# print(second(lines))
