from collections import defaultdict
elves = set()
data = open("input").read()
for y, l in enumerate(data.split("\n")):
    for x, e in enumerate(l):
        if e == "#":
            elves.add((y, x))

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

PRIORITIES = [
    [(-1, 0), (-1, -1), (-1, 1)],
    [(1, 0), (1, -1), (1, 1)],
    [(0, -1), (1, -1), (-1, -1)],
    [(0, 1), (1, 1), (-1, 1)],
]
def plan(elf, world):
    if not any(vadd(pos, elf) in world for pset in PRIORITIES for pos in pset):
        return None
    for priorityset in PRIORITIES:
        if all(vadd(pos, elf) not in world for pos in priorityset):
            return vadd(priorityset[0], elf)

for round in range(10000):
    planned = defaultdict(int)
    elf_plans = {}
    anymove = False
    for elf in elves:
        p = plan(elf, elves)
        elf_plans[elf] = p
        if p is not None:
            anymove = True
            planned[p] += 1
    if not anymove:
        break
    elves2 = set()
    for elf in elves:
        p = elf_plans[elf]
        if p is not None and planned[p] == 1:
            elves2.add(p)
        else:
            elves2.add(elf)
    elves = elves2
    PRIORITIES = PRIORITIES[1:] + [PRIORITIES[0]]

print(round+1)
