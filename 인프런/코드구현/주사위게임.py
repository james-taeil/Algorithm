def diceGame(dice):
    moneys = []
    # res = 0
    
    for i in dice:
        i.sort()
        a, b, c = i
        money = 0
        if a == b and b == c:
            money = 10000 + (a * 1000)
            moneys.append(money)
        elif a == b or a == c:
            money = 1000 + (a * 100)
            moneys.append(money)
        elif b == c:
            money = 1000 + (b * 100)
            moneys.append(money)
        else:
            money = c * 100
            moneys.append(money)
        
        # if money > res:
        #     res = money
    return max(moneys)

dice = [[3, 3, 6], [2, 2, 2], [6, 2, 5]]
print(diceGame(dice))