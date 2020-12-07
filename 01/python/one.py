with open("input.txt") as file:
    raw = file.read().split("\n")
data = [int(item) for item in raw]

indices = range(len(data))
solved = False
for i in indices:
    a = data[i]
    for j in filter(lambda x: x is not i, indices):
        b = data[j]
        if a + b == 2020:
            print(f"{a} + {b} = {a + b}")
            solved = True
        if solved:
            break
    if solved:
        break
