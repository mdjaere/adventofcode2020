with open("input.txt") as file:
    lines = file.read().split("\n")

data_list = [line.split(": ") for line in lines]

valid_count = 0
for data in data_list:
    [rule_raw, password] = data
    [range_raw, letter] = rule_raw.split(" ")
    [low, high] = map(int, range_raw.split("-"))
    letter_count = len(list(filter(lambda x: x == letter, password)))
    if low <= letter_count <= high:
        valid_count = valid_count + 1
print(f"There are {valid_count} valid passwords")
