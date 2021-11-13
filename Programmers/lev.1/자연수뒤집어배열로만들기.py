def solution(n):
    answer = list(map(int, reversed(str(n))))
    return answer

n = 12345
print(solution(n))