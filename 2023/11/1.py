data = [l for l in open("input", "r").read().split("\n") if l]
galaxies, xs, ys = list(), set(), set()
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '#':
            galaxies.append((x, y))
            xs.add(x)
            ys.add(y)
total = 0
for i, (ax, ay) in enumerate(galaxies):
    for (bx, by) in galaxies[i+1:]:
        dist = abs(bx - ax) + abs(by - ay)
        for ex in range(min(ax, bx), max(ax, bx)):
            if ex not in xs: dist += 1
        for ey in range(min(ay, by), max(ay, by)):
            if ey not in ys: dist += 1
        total += dist
print(total)
