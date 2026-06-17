class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        x = prices[0]
        for j in range(1,len(prices)):
            if prices[j] < x:
                x = prices[j]
                
            profit = prices[j] - x
            pro = max(profit, pro)
        
        return pro