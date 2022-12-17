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


def cleanup(tower):
    height = max(y for x, y in tower) + 4
    return set((x, y) for (x, y) in tower if y > height - 100)

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


wind = cycle(data.__iter__())
blockcycle = cycle(blocks.__iter__())
xakep = len(data) * len(blocks)

# I could get this fully automatically but meh
# steps, tower_height
CYCLE_START = 2522750, 4111236
CYCLE_REPEAT = 20182000, 32325672
# CYCLE_START = 1800, 3034
# CYCLE_REPEAT = 3200, 5154
CYCLE_STEPS = CYCLE_REPEAT[0] - CYCLE_START[0]
CYCLE_HEIGHT = CYCLE_REPEAT[1] - CYCLE_START[1]

STEP_CHECK = 1000000000000
STEPS_TO_DO = STEP_CHECK - CYCLE_START[0]
CYCLES_TO_DO = STEPS_TO_DO // CYCLE_STEPS
STEPS_TO_DO %= CYCLE_STEPS
print(CYCLES_TO_DO, STEPS_TO_DO)

for i in range(CYCLE_START[0]):
    simulate(tower, next(blockcycle), wind)
    if i % 30 == 0:
        tower = cleanup(tower)

for i in range(STEPS_TO_DO):
    simulate(tower, next(blockcycle), wind)
    if i % 30 == 0:
        tower = cleanup(tower)
height = max(y for x, y in tower)
print(CYCLES_TO_DO, CYCLE_HEIGHT)
print(height + CYCLES_TO_DO * CYCLE_HEIGHT)
exit()

lasth = 0
for x in range(1000):
    for i in range(xakep):
        simulate(tower, next(blockcycle), wind)
        if i % 30 == 0:
            tower = cleanup(tower)
    height = max(y for x, y in tower)
    print(x * xakep, height - lasth, height)
    lasth = height
