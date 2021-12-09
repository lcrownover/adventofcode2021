def first(lines):
    low_points = []
    for y, line in enumerate(lines):
        for x, point in enumerate(list(line)):
            p = int(point)
            if x > 0:
                left = int(lines[y][x - 1])
                if not p < left:
                    continue
            if len(list(lines[y])) > x + 1:
                right = int(lines[y][x + 1])
                if not p < right:
                    continue
            if y > 0:
                up = int(lines[y - 1][x])
                if not p < up:
                    continue
            if len(lines) > y + 1:
                down = int(lines[y + 1][x])
                if not p < down:
                    continue
            low_points.append(p)
    return sum([int(p) + 1 for p in low_points])


def second(lines):
    return lines


import sys

with open(sys.argv[1], "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

print(first(lines))

# print(second(lines))
