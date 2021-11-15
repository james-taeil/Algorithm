# def solution(n):
#     answer = 0
#     arr = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             answer += i
#     return answer

def solution(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])
n = 12
print(solution(n))