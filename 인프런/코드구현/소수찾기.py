# 에라토스테네스의 체
def solution(n):
    arr = [0 for i in range(n + 1)]
    count = 0
    for i in range(2, n + 1):
        if arr[i] == 0:
            arr[i] = 1
            count += 1
            for j in range(i, n + 1, i):
                arr[j] = 1
    return [arr, count]
    
n = 20
print(solution(n))    