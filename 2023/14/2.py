data = [list(l) for l in open("input", "r").read().split("\n") if l]

def tilt(data, dx, dy):
    for y in range(len(data))[::-dy or 1]:
        for x in range(len(data[0]))[::-dx or 1]:
            if data[y][x] == "O":
                y1, x1 = y + dy, x + dx
                while 0 <= x1 < len(data[0]) and 0 <= y1 < len(data) and data[y1][x1] == '.':
                    data[y1][x1], data[y1-dy][x1-dx] = "O", '.'
                    y1, x1 = y1 + dy, x1 + dx

def cycle(data):
    for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        tilt(data, dx, dy)

state2offset, offset2state = {}, {}
for x in range(1000000000):
    cycle(data)
    state = tuple(tuple(r) for r in data)
    if state in state2offset:
        windata = offset2state[state2offset[state] + (1000000000 - x - 1) % (x - state2offset[state])]
        print(sum((el == 'O') * (len(windata) - y) for y, row in enumerate(windata) for el in row))
        break
    state2offset[state] = x
    offset2state[x] = state
