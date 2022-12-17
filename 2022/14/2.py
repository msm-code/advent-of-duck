data = open("input").read().split("\n")
data = [[[int(c) for c in el.split(",")] for el in row.split(" -> ") if el] for row in data if row]
world = [[' ' for x in range(1000)] for y in range(1000)]

def draw(world, left, right):
    x, y = left
    rx, ry = right
    while True:
        world[y][x] = '#'
        if rx > x:
            x += 1
        elif rx < x:
            x -= 1
        elif ry > y:
            y += 1
        elif ry < y:
            y -= 1
        elif (rx, ry) == (x, y):
            break

for path in data:
    for left, right in zip(path, path[1:]):
        draw(world, left, right)

floor = max(y for path in data for x, y in path) + 2
draw(world, (0, floor), (999, floor))

def drop(sy, sx):
    x, y = sx, sy
    while True:
        if y > floor:
            assert False
        if world[y+1][x] == ' ':
            y += 1
        elif world[y+1][x-1] == ' ':
            y += 1
            x -= 1
        elif world[y+1][x+1] == ' ':
            y += 1
            x += 1
        else:
            world[y][x] = 'o'
            return (x, y) != (sx, sy)

count = 1
while drop(0, 500):
    count += 1

print(count)
