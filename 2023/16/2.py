world = open("input", "r").read().strip().split("\n")

dirmap = { "E": (1, 0), "W": (-1, 0), "S": (0, 1), "N": (0, -1) }
def addv(a, b): return (a[0] + b[0], a[1] + b[1])
def inworld(pos): return 0 <= pos[0] < len(world[0]) and 0 <= pos[1] < len(world)
def follow(dir, pos): return addv(dirmap[dir], pos)

def search(world, startpos):
    queue, visited = [startpos], set([startpos])
    while queue:
        dir, pos = queue.pop()
        elm = world[pos[1]][pos[0]]
        if elm == '.': newdirs = [dir]
        elif elm == '/': newdirs = { "E": ["N"], "N": ["E"], "S": ["W"], "W": ["S"] }[dir]
        elif elm == '\\': newdirs = { "E": ["S"], "N": ["W"], "S": ["E"], "W": ["N"] }[dir]
        elif elm == '-': newdirs = { "E": ["E"], "N": ["E", "W"], "S": ["E", "W"], "W": ["W"] }[dir]
        elif elm == '|': newdirs = { "E": ["S", "N"], "N": ["N"], "S": ["S"], "W": ["S", "N"] }[dir]
        else: assert False
        for newdir in newdirs:
            newpos = follow(newdir, pos)
            if (newdir, newpos) in visited or not inworld(newpos): continue
            visited.add((newdir, newpos))
            queue.append((newdir, newpos))
    return visited

starts = (
    [("S", (x, 0)) for x in range(len(world[0]))] +
    [("N", (x, len(world) - 1)) for x in range(len(world[0]))] +
    [("E", (0, y)) for y in range(len(world))] +
    [("W", (len(world[0])-1, y)) for y in range(len(world))]
)
print(max(len(set(y for (x, y) in search(world, start))) for start in starts))
