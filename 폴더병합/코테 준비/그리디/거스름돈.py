'''
1. 가장 큰 수 500원 부터 제외 해 나간다.
2. 받은 돈이 코인 보다 작은 경우를 생각
'''

basket = [500, 100, 50, 10]
money = int(input())
count = 0

for coin in basket:
    count += (money//coin)
    money = money - ((money//coin)*coin)
    
    
print(count)
        