import re
from collections import defaultdict

data = open("input").read()
rawbricks = re.findall("(\\d+),(\\d+),(\\d+)~(\\d+),(\\d+),(\\d+)", data)
bricks = []
for brick in rawbricks:
    brick = [int(b) for b in brick]
    x0, y0, z0, x1, y1, z1 = brick
    if x0 == x1 and y0 == y1:
        bricks.append([(x0, y0, z) for z in range(min(z0, z1), max(z0, z1)+1)])
    elif x0 == x1 and z0 == z1:
        bricks.append([(x0, y, z0) for y in range(min(y0, y1), max(y0, y1)+1)])
    elif y0 == y1 and z0 == z1:
        bricks.append([(x, y0, z0) for x in range(min(x0, x1), max(x0, x1)+1)])

occupied = set()
laybricks = []
while bricks:
    nextbrick = sorted(bricks, key=lambda brick: min(z for x, y, z in brick))[0]
    bricks.remove(nextbrick)
    while True:
        if any(z == 1 or (x, y, z - 1) in occupied for x, y, z in nextbrick):
            break
        nextbrick = [(x, y, z-1) for (x, y, z) in nextbrick]
    for coord in nextbrick:
        occupied.add(coord)
    laybricks.append(nextbrick)

lays_on = {i: [] for i in range(len(laybricks))}
for i, b0 in enumerate(laybricks):
    for j, b1 in enumerate(laybricks):
        if i == j: continue
        if any((x, y, z+1) not in b0 and (x, y, z+1) in b1 for x, y, z in b0):
            lays_on[j].append(i)

print(sum(1 for i in range(len(laybricks)) if [i] not in lays_on.values()))
