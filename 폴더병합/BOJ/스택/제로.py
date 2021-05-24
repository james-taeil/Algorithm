#시간초과
import sys

input = sys.stdin.readline

stacklist = []

N = int(input())

for i in range(N):
    numstack = int(input())

    if numstack > 0:
        stacklist.append(numstack)

    elif numstack == 0:
        # pop 함수를 안쓰고 이렇게 쓰면 시간초과가 난다.
        # stacklist = stacklist[:-1]
        stacklist.pop()

print(sum(stacklist))