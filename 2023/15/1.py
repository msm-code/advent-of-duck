def hash(str):
    h = 0
    for c in str:
        h = ((h + ord(c)) * 17) % 256
    return h
data = open("test_data").read().strip().split(",")
print(sum(hash(x) for x in data))
