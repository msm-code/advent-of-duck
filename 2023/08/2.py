import re

data = open("input", "r").read().split("\n")
cmd = ["LR".index(c) for c in data[0]]

world = {}
for l in data[2:]:
    if m := re.match("(.*) = [(](.*), (.*)[)]", l):
        world[m.group(1)] = (m.group(2), m.group(3))

def crt(a1, m1, a2, m2):
    inv_m1 = pow(m1, -1, m2)
    inv_m2 = pow(m2, -1, m1)
    return (a1 * m2 * inv_m2 + a2 * m1 * inv_m1) % (m1 * m2)

# find a cycle length (ensure we're on a cycle by skipping `skip` elements)
def solve_cycle(skip, pos):
    for i in range(skip):
        newdir = cmd[i % len(cmd)]
        pos = world[pos][newdir]
    visited = set()
    zvalues = []
    for i in range(1000000):
        cmdoffset = i % len(cmd)
        newdir = cmd[cmdoffset]
        pos = world[pos][newdir]
        if pos.endswith('Z'):
            zvalues.append(i + 1)
        if (cmdoffset, pos) in visited:
            return i, zvalues[0]
        visited.add((cmdoffset, pos))

poses = [p for p in world if p.endswith("A")]

skip = 0
while skip < len(world):
    skip += len(cmd)  # just to avoid modifying cmd

# crt for numbers of form (n*x), (n*y)
n = len(cmd)
clen, off = solve_cycle(skip, poses[0])
for p in poses[1:]:
    clen0, off0 = solve_cycle(skip, p)
    off = crt(off0, clen0 // n, off, clen)
    clen *= clen0 // n

print(skip+off)
