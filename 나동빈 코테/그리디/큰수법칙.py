n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

firstNum = data[-1]
secondNum = data[-2]

count = (m // (k + 1)) * k
count += (m % (k + 1))

result = 0
result += count * firstNum
result += secondNum * (m - count)

print(result)