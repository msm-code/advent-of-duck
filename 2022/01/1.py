import pathlib

data = pathlib.Path("input").read_text().split("\n\n")
print(max(sum(int(c) for c in d.split("\n") if c) for d in data))
