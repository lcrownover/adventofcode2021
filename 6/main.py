#!/usr/bin/env python3


class School:
    def __init__(self, fish):
        self.map = {k: 0 for k in range(0, 9)}
        for i in fish:
            self.map[int(i)] += 1

    def count(self):
        return sum([i for i in self.map.values()])

    def process_day(self):
        num_to_spawn = self.map[0]
        for age in self.map.keys():
            if age == 0:
                self.map[age] = 0
            else:
                if self.map[age] > 0:
                    self.map[age - 1] += self.map[age]
                    self.map[age] = 0
        self.map[8] = num_to_spawn
        self.map[6] += num_to_spawn

    def process_days(self, days):
        for _ in range(days):
            self.process_day()


import sys

with open(sys.argv[1], "r") as f:
    inputs = [line.strip() for line in f.readlines() if line.strip()]

school = School([int(f) for f in inputs[0].split(",")])

school.process_days(256)
print(school.count())
