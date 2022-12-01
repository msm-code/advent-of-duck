data = [[None if c == '.' else c for c in e] for e in open("input").read().split("\n") if e]

def clean(data):
    w, h = len(data[0]), len(data)
    charmap = {'s': 'v', 'e': '>', 'x': None}
    for y in range(h):
        for x in range(w):
            if data[y][x] in charmap:
                data[y][x] = charmap[data[y][x]]

def update(data):
    w, h = len(data[0]), len(data)
    subs = 0
    for x in range(w):
        for y in range(h):
            if data[y][x] == '>' and data[y][(x+1) % w] is None:
                data[y][(x+1) % w] = 'e'
                data[y][x] = 'x'
                subs += 1

    clean(data)
    for y in range(h):
        for x in range(w):
            if data[y][x] == 'v' and data[(y+1) % h][x] is None:
                data[(y+1) % h][x] = 's'
                data[y][x] = 'x'
                subs += 1

    clean(data)
    return subs == 0

for i in range(1000000):
    stopped = update(data)
    if stopped:
        print(i + 1)
        break
