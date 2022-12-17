import re

data = open("input1").read()
sensdata = re.findall(r"Sensor at x=(\d+), y=(\d+): closest beacon is at x=([-0-9]+), y=([-0-9]+)", data)

beacons = []
sensors = []
for line in sensdata:
    sx, sy, bx, by = map(int, line)
    sensors.append((sx, sy, abs(sx-bx) + abs(sy-by)))
    beacons.append((bx, by))

def get_row(row_y, minb, maxb):
    intervals = []
    for sx, sy, power in sensors:
        if abs(sy - row_y) > power:
            continue
        overlap = power - abs(sy - row_y)
        x0, x1 = sx - overlap, sx + overlap
        intervals.append([x0, x1])

    intervals = sorted(intervals)
    outintervals = [intervals[0]]
    for intv in intervals[1:]:
        last = outintervals[-1]
        if last[1] >= intv[0] - 1:
            if intv[1] > outintervals[-1][1]:
                outintervals[-1][1] = intv[1]
        else:
            outintervals.append(intv)

    if len(outintervals) > 1:
        return outintervals[0][1] + 1
    return None


for y in range(4000000):
    x = get_row(y, 0, 4000000)
    if x:
        print(x*4000000 + y)
        break
