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

def addv(a, b):
    ax, ay = a
    bx, by = b
    return (ax + bx, ay + by)

def check(pos, dir):
    path = []
    while True:
        path.append(pos)
        pos = addv(pos, dirmap[dir])
        field = data[pos[1]][pos[0]]
        if field == 'S':
            return path
        if not (dir := followmap[field].get(dir)):
            return None

for dir in "NEWS":
    if path := check(start, dir):
        print(len(path) // 2)
        break
