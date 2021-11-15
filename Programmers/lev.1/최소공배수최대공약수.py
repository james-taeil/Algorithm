def solution(n, m):
    # 최대공약수
    def GCD(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    
    # 최소공배수
    def LCM(x, y):
        result = (x * y) // GCD(x, y)
        return result
    
    answer = [GCD(n, m), LCM(n, m)]
    return answer

n = 2
m = 5
print(solution(n, m))
