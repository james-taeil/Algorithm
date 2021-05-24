#1 2  3  4  5  6    7    8    9   10  0f
#1 3  6 10 15  21  28   36   45   55  1f
#1 4 10 20 35  46  74  110  155  210  2f
#1 5 15 35 70 116 190  300  455  665

# first_floor = [0]
# floor = []
# dept = []소수
#
# for k in range(1, 15):
#     first_floor.append(k)
# dept.append(first_floor)
#
# for j in range(13):
#     for i in range(1, 16):
#         floor.append(sum(first_floor[:i]))
#     dept.append(floor)
#     first_floor = floor
#     floor = []
#
# count = int(input())
# for p in range(count):
#     a = int(input())
#     b = int(input())
#     print(dept[a][b])

#1 2  3  4  5  6    7    8    9   10  0f
#1 3  6 10 15  21  28   36   45   55  1f
#1 4 10 20 35  46  74  110  155  210  2f
#1 5 15 35 70 116 190  300  455  665

count = int(input())
for p in range(count):
    a = int(input())
    b = int(input())
    dept = [k for k in range(1, b+1)]
    for i in range(a):
        for j in range(1, b):
            dept[j] += dept[j-1]
    print(dept[-1])
