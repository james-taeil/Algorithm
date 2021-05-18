import sys

def solution(conlist):
    answer = 0
    last = 0
    for start, end in conlist:
        if start >= last:
            answer += 1
            last = end

    return answer


conlist = []

N = int(sys.stdin.readline())

for i in range(N):
    time = list(map(int, sys.stdin.readline().split()))
    conlist.append(time)


conlist.sort(key=lambda x: (x[1], x[0]))
print(solution(conlist))