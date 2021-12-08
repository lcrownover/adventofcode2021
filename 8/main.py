def first(lines):
    count = 0
    for line in lines:
        outnums = [w.strip() for w in line.split("|")[1].split(" ") if w.strip()]
        for n in outnums:
            if len(n) in [2,4,3,7]:
                count += 1
    return count


def second(lines):
    map = {}
    codes = sorted(["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"], key=len)
    placed = []
    c = 0
    cur = 0
    while len(codes) > 0:
        code = codes[cur]
        print(f"{map=}")
        print(f"{codes=}")
        print(f"{placed=}")
        print(f"processing code: {code}")
        print()
        if len(code) == 2: # number 1
            l = list(code)
            map[1],map[2] = l[0],l[1]
            placed.extend(l)
            codes.remove(code)
            cur = 0
        if len(code) == 3: # number 7
            l = [l for l in list(code) if l not in placed]
            print(l)
            map[6] = l[0]
            placed.extend(l)
            codes.remove(code)
            cur = 0
        if len(code) == 4: # number 4
            l = [l for l in list(code) if l not in placed]
            map[5],map[7] = l[0],l[1]
            placed.extend(l)
            codes.remove(code)
            cur = 0
        if len(code) == 7: # number 8
            l = [l for l in list(code) if l not in placed]
            map[3],map[4] = l[0],l[1]
            placed.extend(l)
            codes.remove(code)
            cur = 0

        cur += 1

        # at this point, the only one we know for sure is map[6], which is the top of 7
        c += 1
        if c > 20: break









import sys

with open(sys.argv[1], "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

# print(first(lines))

print(second(lines))
