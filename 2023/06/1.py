from math import prod

data = open("input", "r").read().split("\n")
data = [[int(e) for e in row.split()[1:]] for row in data if row]

def solve(time, distance):
    return sum((time-s)*s > distance for s in range(time))

print(prod(solve(data[0][i], data[1][i]) for i in range(len(data[0]))))
