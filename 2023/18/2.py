import re

data = open("input", "r").read()
dirmap = { "R": (1, 0), "L": (-1, 0), "D": (0, 1), "U": (0, -1) }
def addv(a, b): return (a[0] + b[0], a[1] + b[1])
def mulv(d, n): return (d[0] * n, d[1] * n)
def follow(dir, pos): return addv(dirmap[dir], pos)

area, edges, digger = 0, 0, (0, 0)
for dir, steps, color in re.findall("(.) (\\d+) [(]#(......)[)]", data):
    dir = {"0": "R", "1": "D", "2": "L", "3": "U"}[color[-1]]
    steps = int(color[:-1], 16)
    if dir == "D" or dir == "L": edges += int(steps)
    newdigger = addv(mulv(dirmap[dir], int(steps)), digger)
    area += (newdigger[0] - digger[0]) * newdigger[1]
    digger = newdigger

print(abs(area) + edges + 1)
