
#
# def push(a):
#     arr.append(a)
#
# def pop():
#     if len(arr) < 1:
#         return -1
#     else:
#         return arr.pop()
#
# def size():
#     return len(arr)
#
# def empty():
#     if len(arr) < 1:
#         return 1
#     else:
#         return 0
#
# def top():
#     if len(arr) < 1:
#         return 0
#     else:
#         return arr[-1]
#
#
#
# for i in range(N):
#     input_list = sys.stdin.readline().rstrip().split()
#
#     a = input_list[0]
#
#     if a == 'push':
#         push(input_list[1])
#     elif a == 'pop':
#         print(pop())
#     elif a == 'size':
#         print(size())
#     elif a == 'empty':
#         print(empty())
#     elif a == 'top':
#         print(top())

import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    ipt = input().rstrip()
    if " " in ipt:
        a, b = ipt.split()
        arr.append(b)

    elif ipt == 'pop':
        if len(arr) < 1:
            print(-1)
        else:
            # print(arr[-1])
            # arr = arr[:-1]
            print(arr.pop())

    elif ipt == 'size':
        print(len(arr))

    elif ipt == 'empty':
        if len(arr) < 1:
            print(1)
        else:
            print(0)

    elif ipt == 'top':
        if len(arr) < 1:
            print(-1)
        else:
            print(arr[-1])

