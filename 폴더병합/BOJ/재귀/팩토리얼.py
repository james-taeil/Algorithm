# N = int(input())
# pt = 1
# for i in range(1, N+1):
#     pt *= i

# print(pt)

#반복문
# def solution(N):
#     pt = 1
#     for i in range(1, N+1):
#         pt *= i
#     return pt


#재귀
def solution_FAC_recursive(N):
    if N == 0:
        return 1
    else:    
        return (N * solution_FAC_recursive(N-1))

N = int(input())
print(solution_FAC_recursive(N))