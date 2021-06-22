n = int(input())

#메모리제이션
d = [0] * (n * 2)

d[0] = 1
d[1] = 2

for i in range(2, n + 1):
    d[i] = (d[i - 1] + d[i - 2])


print(d[n])