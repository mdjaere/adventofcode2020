import fileinput

code = [int(line.strip()) for line in fileinput.input()]


# Part 1
n_pre = 25
specials = []


def is_special(to_test, pre):
    for p in pre:
        new_pre = filter(lambda x: x != p, pre)
        if (to_test - p) in new_pre:
            return False
    return True


for i in range(n_pre, len(code)):
    if is_special(code[i], code[i - n_pre: i]):
        specials.append(code[i])

print(specials[0])

# Part 2
goal = specials[0]


def find_combo(code):
    for n in range(2, len(code)):
        for i in range(len(code)-n):
            to_test = code[i:i+n]
            if sum(to_test) == goal:
                return to_test


a = find_combo(code)
a.sort()
p2 = a[0] + a[-1]
print(p2)
