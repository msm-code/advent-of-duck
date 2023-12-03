#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p python3

data = open("input").read()
lines = [list(l) for l in data.split("\n") if l]
def gib(y, x): return 'x' if y < 0 or y >= len(lines) or x < 0 or x >= len(lines[y]) else lines[y][x]
def clear(y, x): lines[y][x] = 'y'
SYMBOLS = '=@%/&#*-+$'
total = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if gib(y, x) not in SYMBOLS: continue
        nums = []
        for yy in [y-1, y, y+1]:
            xx = x
            while gib(yy, xx - 1).isdigit() and xx > 0: xx -= 1
            while xx <= x + 1:
                acc = ''
                while gib(yy, xx).isdigit():
                    acc += gib(yy, xx)
                    clear(yy, xx)
                    xx += 1
                if acc:
                    nums.append(int(acc))
                xx += 1
        if len(nums) == 2:
            total += nums[0] * nums[1]
print(total)
