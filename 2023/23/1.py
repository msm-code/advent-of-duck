import sys
sys.setrecursionlimit(10000000)
data = open("input").read().strip().split("\n")

DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
DIRMAP = { ">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1) }
def addv(a, b): return (a[0] + b[0], a[1] + b[1])
def longest(seen, pos):
    if pos[1] == len(data) - 1: return 0  # end condition 
    tile = data[pos[1]][pos[0]]
    best = 0
    seen.add(pos)
    for dir in DIRS:
        pos2 = addv(pos, dir)
        if pos2 in seen: continue
        if data[pos2[1]][pos2[0]] == '#': continue
        if tile in DIRMAP and DIRMAP[tile] != dir: continue
        best = max(best, longest(seen, pos2))
    seen.remove(pos)
    return best + 1

seen = {(1, 0)}
print(longest(seen, (1, 1)) + 1)
