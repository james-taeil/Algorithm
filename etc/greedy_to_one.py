n, k = map(int, input().split())

count = 0

while True:
    if n == 1:
        break

    else:
        if (n % k) == 0:
            n = n / k
            count += 1
        else:
            n -= 1
            count += 1

print(count)

#--------------------------------------

n, k = map(int, input().split())

count = 0

while n >= k:
    while n % k != 0:
        n -= 1
        count += 1
    n = n//k
    count += 1

while n > 1:
    n -= 1
    count += 1

#----------------------------------------



