from itertools import cycle

data = open("input", "r").read().strip()


blocks = [
    (
        "  #### ",
    ),
    (
        "   #   ",
        "  ###  ",
        "   #   ",
    ),
    (
        "  ###  ",
        "    #  ",
        "    #  ",
    ),
    (
        "  #    ",
        "  #    ",
        "  #    ",
        "  #    ",
    ),
    (
        "  ##   ",
        "  ##   ",
    ),
]

blocks = [
    [(x, y) for y, row in enumerate(block) for x in range(len(row)) if row[x] == "#"] for block in blocks
]

tower = set([
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),  # floor
])

def shl(block, tower):
    if any(x <= 0 or (x - 1, y) in tower for x, y in block):
        return block
    return [(x - 1, y) for x, y in block]


def shr(block, tower):
    if any(x >= 6  or (x + 1, y) in tower for x, y in block):
        return block
    return [(x + 1, y) for x, y in block]


def shift(block, tower, character):
    return shl(block, tower) if character == "<" else shr(block, tower)


def lift(block, height):
    return [(x, y + height) for x, y in block]


def lower(block):
    return [(x, y - 1) for x, y in block]


def collides(block, tower):
    return any(b in tower for b in block)


def simulate(tower, block, wind):
    height = max(y for x, y in tower) + 4
    block = lift(block, height)
    # dump(tower | set(block))
    for i in range(10000):
        block = shift(block, tower, next(wind))
        block2 = lower(block)
        if collides(block2, tower):
            tower |= set(block)
            return
        block = block2

def dump(tower):
    height = max(y for x, y in tower) + 1
    for y in range(height)[::-1]:
        row = ""
        for x in range(7):
            if (x, y) in tower:
                row += "#"
            else:
                row += "."
        print(row)
    print()


dump(tower)
wind = cycle(data.__iter__())
blocks = cycle(blocks.__iter__())
for i in range(2022):
    simulate(tower, next(blocks), wind)
    # dump(tower)
height = max(y for x, y in tower)
print(height)
