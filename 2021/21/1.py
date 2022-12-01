import re

def roll(player, dice):
    return (player + next(dice) + next(dice) + next(dice) - 1) % 10 + 1

dice = (i+1 for i in range(10000))
pls = [(int(p), 0) for p in re.findall("position: (.+)", open("input").read())]
while pls[1][1] < 1000:
    pls = (pls[1], (r := roll(pls[0][0], dice), pls[0][1]+r))

print((next(dice)-1)*pls[0][1])