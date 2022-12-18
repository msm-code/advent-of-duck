world = [[[False for _ in range(31)] for _ in range(31)] for _ in range(31)]
data = open("input1", "r").read().split("\n")
total_area = 0
for x, y, z in [map(int, row.split(",")) for row in data if row]:
    world[x+5][y+5][z+5] = True
    assert 0 <= x <= 19
    assert 0 <= y <= 19
    assert 0 <= z <= 19
    total_area += 6

for x in range(1, 30):
    for y in range(1, 30):
        for z in range(1, 30):
            if not world[x][y][z]:
                continue
            dirs = [
                (0, 0, -1),
                (0, 0, 1),
                (0, -1, 0),
                (0, 1, 0),
                (-1, 0, 0),
                (1, 0, 0),
            ]
            for dx, dy, dz in dirs:
                if world[x+dx][y+dy][z+dz]:
                    total_area -= 1

print(total_area)
