import re

data = open("input", "r").read().split("\n")
cmd = ["LR".index(c) for c in data[0]]

world = {}
for l in data[2:]:
    if m := re.match("(.*) = [(](.*), (.*)[)]", l):
        world[m.group(1)] = (m.group(2), m.group(3))

pos = 'AAA'
for i in range(99999999999):
    newdir = cmd[i % len(cmd)]
    pos = world[pos][newdir]
    if pos == 'ZZZ': break
print(i + 1)
