with open("input.txt") as file:
    lines = file.read().split("\n")

data_list = [line.split(": ") for line in lines]

valid_count = 0
for data in data_list:
    [rule_raw, password] = data
    [range_raw, letter] = rule_raw.split(" ")
    [p1, p2] = [int(loc) - 1 for loc in range_raw.split("-")]
    if (password[p1] == letter) ^ (password[p2] == letter):
        valid_count += 1
print(f"There are {valid_count} valid passwords")
