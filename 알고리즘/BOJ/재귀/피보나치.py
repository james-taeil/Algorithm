#for문
# def solution(N):
#     if N == 0:
#         return 0
#     elif N == 1:
#         return 1
#     else:
#         pi = [0, 1]
#         for i in range(N-1):
#             pibo = pi[i] + pi[i+1]
#             pi.append(pibo)
        
#         return pi[-1]

# N = int(input())
# print(solution(N))


#재귀
def solution_PIBO_recursive(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return solution_PIBO_recursive(N-1) + solution_PIBO_recursive(N-2)

N = int(input())
print(solution_PIBO_recursive(N))