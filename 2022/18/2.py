world = [[["AIR" for _ in range(31)] for _ in range(31)] for _ in range(31)]
data = open("input1", "r").read().split("\n")
total_area = 0
for x, y, z in [map(int, row.split(",")) for row in data if row]:
    world[x+5][y+5][z+5] = "STONE"
    assert 0 <= x <= 19
    assert 0 <= y <= 19
    assert 0 <= z <= 19

dirs = [
    (0, 0, -1),
    (0, 0, 1),
    (0, -1, 0),
    (0, 1, 0),
    (-1, 0, 0),
    (1, 0, 0),
]

def steam(x, y, z):
    stack = [(x, y, z)]
    while stack:
        x, y, z = stack.pop()
        if world[x][y][z] != "AIR":
            continue
        world[x][y][z] = "STEAM"
        if any(c == 0 or c == 30 for c in [x, y, z]):
            continue
        for dx, dy, dz in dirs:
            stack.append((x+dx, y+dy, z+dz))

steam(1, 1, 1)

for x in range(1, 30):
    for y in range(1, 30):
        for z in range(1, 30):
            if world[x][y][z] != "STONE":
                continue
            for dx, dy, dz in dirs:
                if world[x+dx][y+dy][z+dz] == "STEAM":
                    total_area += 1

print(total_area)
