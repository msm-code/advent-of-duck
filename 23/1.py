state = (
    (None,) * 7,
    (("C", "B"), ("B", "D"), ("D", "A"), ("A", "C")),
)

win = (
    (None,) * 7,
    (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")),
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
        if rooms[r] == (None, None):
            newstate = move(state, h, r, 1)
            yield newstate, (steps+2) * pricemap[elm]
            return
        if rooms[r] == (None, elm):
            newstate = move(state, h, r, 0)
            yield newstate, (steps+1) * pricemap[elm]
            return
    for h, elm in enumerate(hallway):
        for r in range(4):
            if elm is not None:
                continue
            steps = steps_to_room(hallway, h, r)
            if steps is None:
                continue
            if rooms[r][1] is not None and rooms[r][0] is None:
                if ord(rooms[r][1]) - ord('A') != r:
                    newstate = move(state, h, r, 1)
                    yield newstate, (steps+2) * pricemap[rooms[r][1]]
            elif rooms[r][1] is not None and rooms[r][0] is not None:
                if ord(rooms[r][1]) - ord('A') != r or ord(rooms[r][0]) - ord('A') != r:
                    newstate = move(state, h, r, 0)
                    yield newstate, (steps+1) * pricemap[rooms[r][0]]

def dfs(state, best, cost):
    if cost >= best:
        return best
    if state == win:
        return cost
    for i, (newstate, price) in enumerate(allowed_moves(state)):
        best = min(best, dfs(newstate, best, cost + price))
    return best

print('best', dfs(state, 100000000000, 0))
