coins = [500, 100, 50, 10]


money = int(input())
count = 0
countCoin = 0


for coin in coins:
    if money == 0:
        break
    count = int(money / coin)
    countCoin += count
    money = money - (coin * count)    
    
print(countCoin)