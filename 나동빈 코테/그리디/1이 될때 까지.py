n, m = map(int, input().split())
count = 0

while True:
    if n <= 1:
        break
    
    if n % m == 0:
        n = n // m
    else:
        n -= 1
           
    count += 1

print(count)


# 해설
result = 0
while True:
    target = (n // m) * m
    result += (n - target)
    n = target
    
    if n < k:
        break
    result += 1
    n //= m
    
result += (n - 1)
print(reuslt)