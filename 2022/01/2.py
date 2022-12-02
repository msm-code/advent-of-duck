import pathlib

data = pathlib.Path("input").read_text().split("\n\n")
print(sum(sorted(sum(int(c) for c in d.split("\n") if c) for d in data)[-3:]))
