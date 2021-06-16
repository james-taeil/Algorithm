# 데이터 문자열로 받기
# 두번째 문자는 그냥 행
# 첫번째 아스키코드 값으로 바꾸기

# 움직일수 있는 경우의 수 8가지



data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1

# 행 열 순으로
moves = [ (-2, -1),  (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)  
        ]

result = 0
for move in moves:
    next_row = row + move[0]
    next_col = col + move[1]
    
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)