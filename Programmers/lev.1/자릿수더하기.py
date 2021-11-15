# def solution(n):
#     answer = 0
#     while n > 0:
#         answer += n % 10
#         n //= 10
#     return answer

# recursive solution
def solution(n):
    if n < 10:
        return n
    return (n % 10) + solution(n //10)

n = 123
print(solution(n))