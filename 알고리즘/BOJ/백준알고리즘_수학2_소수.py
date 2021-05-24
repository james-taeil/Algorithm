m = int(input())
n = int(input())
num = []

for i in range(m, n+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
            if count > 2:
                break
    if count == 2:
       num.append(i)

if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(min(num))