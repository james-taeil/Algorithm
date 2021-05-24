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
            popnum = arr[0]
            arr = arr[1:]
            print(popnum)
    elif ipt == 'size':
        print(len(arr))

    elif ipt == 'empty':
        if len(arr) < 1:
            print(1)
        else:
            print(0)

    elif ipt == 'front':
        if len(arr) < 1:
            print(-1)
        else:
            print(arr[0])
    elif ipt == 'back':
        if len(arr) < 1:
            print(-1)
        else:
            print(arr[-1])