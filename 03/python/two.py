from functools import reduce

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

paths = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
results = []

for right_step, down_step in paths:
    pos = 0
    tree_count = 0

    for index, line in enumerate(lines[0::down_step]):
        item = line[pos % len(line)]
        if index != 0:
            tree_count += item == "#"
        pos += right_step
    results.append(tree_count)

product = reduce((lambda x, y: x * y), results)
print(f"The product of all path tree hits {results} is {product}")
