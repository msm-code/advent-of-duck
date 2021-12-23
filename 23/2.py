state = (
    (None,) * 7,
    (("C", "D", "D", "B"), ("B", "C", "B", "D"), ("D", "B", "A", "A"), ("A", "A", "C", "C")),
)

win = (
    (None,) * 7,
    (("A", "A", "A", "A"), ("B", "B", "B", "B"), ("C", "C", "C", "C"), ("D", "D", "D", "D")),
)

def steps_to_room(hallway, hndx, rndx):
    steps = -1 if hndx in [0, 6] else 0
    hndx, rndx = hndx * 2, (rndx*2) + 3
    while True:
        if hndx == rndx:
            return steps
        hndx = hndx + (1 if rndx > hndx else -1)
        steps += 1
        if hndx % 2 == 0 and hallway[hndx//2] is not None:
            return None

pricemap = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}

def move(state, hndx, rndx, level):
    hallway, rooms = state
    helm, relm = hallway[hndx], rooms[rndx][level]
    newh = hallway[:hndx] + (relm,) + hallway[hndx+1:]
    newroom = rooms[rndx][:level] + (helm,) + rooms[rndx][level+1:]
    newr = rooms[:rndx] + (newroom,) + rooms[rndx+1:]
    return newh, newr

def allowed_moves(state):
    hallway, rooms = state

    for h, elm in enumerate(hallway):
        if elm is None:
            continue
        r = ord(elm) - ord('A')
        steps = steps_to_room(hallway, h, r)
        if steps is None:
            continue
        for i in range(len(rooms[r])):
            if all(x is None for x in rooms[r][:i+1]):
                if all(x == elm for x in rooms[r][i+1:]):
                    yield move(state, h, r, i), (steps+1+i) * pricemap[elm]
                    return
    for h, elm in enumerate(hallway):
        for r in range(4):
            if elm is not None:
                continue
            steps = steps_to_room(hallway, h, r)
            if steps is None:
                continue
            for i in range(len(rooms[r])):
                if all(x is None for x in rooms[r][:i]) and all(x is not None for x in rooms[r][i:]):
                    if any(ord(x) - ord('A') != r for x in rooms[r][i:]):
                        yield move(state, h, r, i), (steps+1+i) * pricemap[rooms[r][i]]

def dfs(state, best, cost):
    if cost >= best:
        return best
    if state == win:
        return cost
    for i, (newstate, price) in enumerate(allowed_moves(state)):
        best = min(best, dfs(newstate, best, cost + price))
    return best

print('best', dfs(state, 100000000000, 0))