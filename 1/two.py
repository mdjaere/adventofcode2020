with open("input.txt") as file:
    raw = file.read().split("\n")
data = [int(item) for item in raw]

solved = False
indices = range(len(data))
for i in indices:
    a = data[i]
    for j in filter(lambda x: x is not i, indices):
        b = data[j]
        for k in filter(lambda x: x not in [i, j], indices):
            c = data[k]
            if a + b + c == 2020:
                print(f"{a} * {b} * {c} = {a * b * c}")
                solved = True
            if solved:
                break
        if solved:
            break
    if solved:
        break
