# LeetCode - Best time to buy and sell stock

## Problems
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

## 해결
1. 반복문을 도는 문법을 만든다.
2. 반복문들 돌 때 미리 buy를 선언해서 사용한다.
  2-1. 여기서 중요한 점은 buy 값이 sell 값보다 클 경우 buy값을 재 선언해주고 넘어가는게 중요하다.


## My Solved

```py
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    buy = prices[0]
    size = len(prices)
    for i in range(1, size):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > profit:
                profit = prices[i] - buy
    return profit
```

Runtime : 994 ms
나름 빠르게 만든 코드 같다. size를 쓰는게 len(prices)를 쓰는 것과 공간활용에서 다른가 의문이 살짝 든다.

## 멋진 풀이

```py
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
```

코드가 직관적으로 잘보인다. 또한 current를 활용한 방법을 이용하여 max() 함수를 정확히 사용한 것 같다.