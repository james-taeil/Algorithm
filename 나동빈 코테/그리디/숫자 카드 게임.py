n, m = map(int, input().split())

# answer = []

# for i in range(n):
#     numList = list(map(int, input().split()))
#     answer.append(min(numList))

# print(max(answer))


result = 0
for i in range(n):
    numList = list(map(int, input().split()))
    minValue = min(numList)
    result = max(result, minValue)
    
print(result)