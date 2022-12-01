import itertools
from functools import reduce

algorithm, image = open("input").read().split("\n\n")
algorithm = [int(c == '#') for c in algorithm]
image = [[int(c == '#') for c in row] for row in image.split("\n") if row]
background = 0

def get1(arr, y, x): return arr[y][x] if 0 <= y < len(arr) and 0 <= x < len(arr[0]) else background
def get9(arr, y, x): return [get1(arr, y1, x1) for y1 in [y-1, y, y+1] for x1 in [x-1, x, x+1]]
def getI(arr, y, x): return algorithm[int("".join(str(c) for c in get9(arr, y, x)), 2)]
def iterate(img): return [[getI(img, y, x) for x in range(-1, len(img[0])+1)] for y in range(-1, len(img)+1)]
def iterate2(img):
    global background
    newimg, background = iterate(img), algorithm[-background % len(algorithm)]
    return newimg

print(sum(map(sum, reduce(lambda x, _: iterate2(x), range(50), image))))