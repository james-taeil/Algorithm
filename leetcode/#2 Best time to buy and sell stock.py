def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    buy = 0
    sell = 1
    
    while sell < len(prices):
        current_profit = prices[sell] - prices[buy]
        
        if prices[sell] > prices[buy]:
            profit = max(current_profit, profit)
        else:
            buy = sell
        sell += 1
    return profit