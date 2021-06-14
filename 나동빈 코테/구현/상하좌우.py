n  = int(input())
moves = list(map(str, input().split()))
x, y = 1, 1


command = ['L', 'R', 'U', 'D']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for move in moves:
    for i in range(len(command)):
        if move == command[i]:
            # 배열은 아래로 생기니까
            nx = x + dy[i]
            ny = y + dx[i]
            
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)



## 책의 답안지

# #L R U D 따른 이동
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# command = ['L', 'R', 'U', 'D']

# for move in moves:
#     # 이동 좌표에서 하나씩 확인
#     for i in range(len(command)):
#         if move == command[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]

#     # 범위 벗어날 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue    
#     # 이동 수행
#     x, y = nx, ny
    
# print(x, y)