a = int(input())

num = 0

numlist = list(map(int, input().split(' ')))


for i in numlist:
    count = 0
    if i == 1:
        pass
    else:
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            num += 1
print(num)