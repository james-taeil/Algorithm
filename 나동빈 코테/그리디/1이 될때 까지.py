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