def solution(n):
    answer = -1
    n = n ** 0.5
    if n == int(n):
        return (n + 1) ** 2
    return answer

print(solution(121))