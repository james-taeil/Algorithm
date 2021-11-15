def solution(n):
    answer = 0
    prime = [0] * (n + 2)
    for i in range(2, n + 1):
        if prime[i] == 0:
            answer += 1
            for j in range(i, n + 1, i):
                prime[i] = 1
    return answer

