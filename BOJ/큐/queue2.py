import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
de = deque()

for i in range(N):
    command = input().rstrip()

    if command[0] == "push":
        de.append(command[1])

    elif command[0] == 'pop':
        if len(de) < 1:
            print(-1)
        else:
            print(de.popleft())

    elif command[0] == "size":
        print(len(de))

    elif command[0] == 'empty':
        if len(de) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(de) < 1:
            print(-1)
        else:
            print(de[0])

    elif command == 'back':
        if len(de) < 1:
            print(-1)
        else:
            print(de[-1])


            