def solution(nums):    
    def reverse(x):
        res = 0
        while x:
            div = x % 10
            res = (res * 10) + div
            x //= 10
        return res

    def isPrime(x):
        if x == 1:
            return False
        
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                return False
        else:
            return True
        
    answer = 0
    
    for num in nums:
        if isPrime(reverse(num)):
            answer += 1
    
    return answer



nums = [32, 55, 62, 3700, 250]
print(solution(nums))