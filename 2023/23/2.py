import sys
sys.setrecursionlimit(10000000)
data = open("input").read().strip().split("\n")
DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def addv(a, b): return (a[0] + b[0], a[1] + b[1])

graph = {}
graph[(1, 0)] = [(1, (1, 1))]
graph[(len(data) - 2, len(data) - 1)] = [(1, (len(data) - 2, len(data) - 2))]

for y in range(1, len(data) - 1):
    for x in range(1, len(data) - 1):
        if data[y][x] == '#': continue
        edges = []
        for dir in DIRS:
            pos2 = addv((x, y), dir)
            if data[pos2[1]][pos2[0]] == '#': continue
            edges.append((1, pos2))
        graph[(x, y)] = edges

for key in list(graph.keys()):  # relaxing
    edges = graph[key]
    if len(edges) == 2:
        (el0, e0), (el1, e1) = edges[0], edges[1]
        graph[e0] = [e for e in graph[e0] if e[1] != key] + [(el0 + el1, e1)]
        graph[e1] = [e for e in graph[e1] if e[1] != key] + [(el0 + el1, e0)]

def longest(seen, pos):
    if pos[1] == len(data) - 1: return 0  # end condition 
    best = -1000000  # the smallest number possible
    seen.add(pos)
    for edgelen, pos2 in graph[pos]:
        if pos2 in seen: continue
        if data[pos2[1]][pos2[0]] == '#': continue
        best = max(best, longest(seen, pos2) + edgelen)
    seen.remove(pos)
    return best

print(longest(set(), (1, 0)))
