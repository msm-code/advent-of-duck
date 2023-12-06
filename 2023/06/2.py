data = open("input", "r").read().split("\n")
time, distance = [int(r.split(":")[1].replace(" ", "")) for r in data if r]
print(sum((time-s)*s > distance for s in range(time)))
