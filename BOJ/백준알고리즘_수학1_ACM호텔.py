# how = int(input())
# count = 0
# room = "0"
# for i in range(how):
#     H, W, num = map(int, input().split())
#     for k in range(1, W+1):
#         for j in range(1, H+1):
#             j, k = str(j), str(k)
#             room = j + room + k
#             count += 1
#             if num == count:
#                 print(room)
#                 break
#             room = "0"

count = int(input())
for i in range(count):
    H, W, num = map(int, input().split())
    dist = num // H + 1
    floor = num % H
    if floor == 0:
        floor = H
        dist = num//H

    print(floor * 100 + dist)
