input_data = input()
row = int(input_data[1])

colums = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

count = 0

for step in steps:
    next_row = row + step[0]
    next_colums = colums + step[1]

    if next_row >= 1 and next_row <= 8 and next_colums >= 1 and next_colums <= 8:
        count += 1
print(count)