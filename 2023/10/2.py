data = [l for l in open("input", "r").read().split("\n") if l]

start = None
for y, row in enumerate(data):
    if 'S' in row:
        start = (row.index('S'), y)
        break
assert start

# ok hear me out, this is what we're gonna do
# "NESW" == directions, and we define a map of pipes and how they behave
followmap = {
    "L": {"S": "E", "W": "N"},
    "J": {"S": "W", "E": "N"},
    "7": {"N": "W", "E": "S"},
    "F": {"N": "E", "W": "S"},
    "|": {"N": "N", "S": "S"},
    "-": {"E": "E", "W": "W"},
    ".": {}
}

dirmap = {
    "E": (1, 0),
    "W": (-1, 0),
    "S": (0, 1),
    "N": (0, -1),
}

maprecovery = {
    "EN": "F",
    "WN": "7",
    "EE": "-",
    # too lazy to add all options here
}

def addv(a, b):
    ax, ay = a
    bx, by = b
    return (ax + bx, ay + by)

def check(pos, initdir):
    dir, path = initdir, []
    while True:
        path.append(pos)
        pos = addv(pos, dirmap[dir])
        field = data[pos[1]][pos[0]]
        if field == 'S':
            return path, maprecovery[initdir+dir]
        if not (dir := followmap[field].get(dir)):
            return None

for dir in "NEWS":
    if result := check(start, dir):
        path, field = result
        break

assert path and field

data[start[1]] = data[start[1]][:start[0]] + field + data[start[1]][start[0]+1:]
path = set(path)

# ok my idea is: first clean up the junk, and then upscale to make comp easier
for y in range(len(data)):
    data[y] = list(data[y])
    for x in range(len(data[y])):
        if (x, y) not in path:
            data[y][x] = '.'

# 3x3 tiles
chonks = {
    "L": (" x ", " xx", "   "),
    "J": (" x ", "xx ", "   "),
    "7": ("   ", "xx ", " x "),
    "F": ("   ", " xx", " x "),
    "|": (" x ", " x ", " x "),
    "-": ("   ", "xxx", "   "),
    ".": ("   ", "   ", "   "),
}

chonkdata = [list("?" * len(data[0]) * 3) for y in range(len(data) * 3)]
# print(len(chonkdata), len(chonkdata[0]))
for y in range(len(data)):
    for x in range(len(data[y])):
        for yy in range(3):
            for xx in range(3):
                dx, dy = 3*x + xx, 3*y + yy
                chonkdata[dy][dx] = chonks[data[y][x]][yy][xx]

def floodfill(data):
    stack = [(0, 0)] # start from (0, 0) because it's guaranteed to be out
    while stack:
        pos = stack.pop()
        for dir in dirmap.values():
            newpos = addv(pos, dir)
            if (0 <= newpos[0] < len(data[0])) and (0 <= newpos[1] < len(data)): 
                if data[newpos[1]][newpos[0]] == ' ':
                    data[newpos[1]][newpos[0]] = '.'
                    stack.append(newpos)
floodfill(chonkdata)

# now just count empty squares
# note: look at the square centres only
empty = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if chonkdata[y*3+1][x*3+1] == ' ':
            empty += 1

print(empty)
