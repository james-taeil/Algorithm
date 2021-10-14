def knapsack1(bag, item_weight, item_price):
    # 전체배낭무게, 각아이템무게, 각아이템가격
    
    # 
    n = len(item_weight) - 1
    K = [0] * (n + 1)
    
    weight = 0
    
    for i in range(1, n + 1):
        weight += w[i]
        K[i] = w[i]
        if (weight > bag):
            K[i] -= (weight - bag)
            break
        
    return K