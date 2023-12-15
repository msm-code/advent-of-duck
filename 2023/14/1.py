data = [list(l) for l in open("input", "r").read().split("\n") if l]

def tilt(data):
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "O":
                y1 = y - 1
                while y1 >= 0 and data[y1][x] == '.':
                    data[y1][x], data[y1+1][x] = "O", '.'
                    y1 -= 1

tilt(data)
print(sum((el == 'O') * (len(data) - y) for y, row in enumerate(data) for el in row))
