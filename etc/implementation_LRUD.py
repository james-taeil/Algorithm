# n = int(input())
#
# m = n
#
# matrix = []
#
# for i in range(1,n+1):
#     numlist = []
#     for j in range(1,m+1):
#         numlist.append(j)
#     matrix.append(numlist)
#
#
#
#
# print(matrix)

#-----------------------------

# n = int(input())
#
# #현재 위치
# x, y = 1, 1
# plans = input().split()
#
# #남북서동 // 하기나름
# dx = [0,0,-1,1] #x방향성
# dy = [-1,1,0,0] #y방향성
#
#
#
# move_types = ['L','R','U','D']
# print(len(move_types))
# for plan in plans:
#     print(plan)
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             #다음위치
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if (nx < 1) or (ny < 1) or (nx > n) or (ny > n):
#         continue
#     x, y = nx, ny
# print(x, y)

#--------------------------------

#보통의 방향벡터
#동 북 서 남
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]
#
# x, y = 2, 2
#
# for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     print(nx, ny)


#--------------------------------

n = int(input())

dis = input().split()

udlr = ['L','R','U','D']

x, y = 1, 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for di in dis:
    for i in range(len(udlr)):
        if di == udlr[i]:
            nx = n + dx[i]
            ny = n + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)