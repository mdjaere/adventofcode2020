import fileinput

lines = [line.strip() for line in fileinput.input()]

seat_ids = []

for line in lines:
    r_str, s_str = line[0:7], line[7:]
    r_bin = r_str.replace("F", "0").replace("B", "1")
    row = int(r_bin, 2)
    s_bin = s_str.replace("L", "0").replace("R", "1")
    seat = int(s_bin, 2)
    # print(f"Row: {row}, Seat: {seat}")
    id = row * 8 + seat
    seat_ids.append(id)

highest = max(seat_ids)
print(highest)

missing_id = sum(range(min(seat_ids), max(seat_ids) + 1)) - sum(seat_ids)
print(missing_id)
