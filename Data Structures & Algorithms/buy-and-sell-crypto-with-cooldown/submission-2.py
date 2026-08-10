class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        memo = {}
        def dp(i,buying):
            if (i,buying) in memo:
                return memo[(i,buying)]

            if i >= n:
                return 0
            
            ans = 0
            if buying:
                buy = dp(i+1, False) - prices[i]
                wait = dp(i+1, True)
                ans =  max(buy, wait)
            else:
                sell = prices[i] + dp(i+2,True)
                hold = dp(i+1, False)
                ans = max(sell,hold)

            memo[(i,buying)] = ans
            return ans
        return dp(0,True)