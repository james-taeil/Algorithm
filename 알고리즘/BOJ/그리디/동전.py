import sys
input = sys.stdin.readline

N, K = map(int, input().split())

basket = []

for i in range(N):
    coin = int(input())
    if coin > K:
        pass
    else:
        basket.append(coin)

basket.sort()

count = 0

while (K != 0):
    count += K // basket[-1]
    K = K % basket[-1]
    basket.pop()

print(count)