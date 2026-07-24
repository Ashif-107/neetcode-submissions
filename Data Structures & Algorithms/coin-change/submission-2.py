class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float("inf")] * (amount+1) 
        dp[0] = 0

        for i in range(len(coins)):
            c = coins[i]
            for j in range(c,amount+1): 
                dp[j] = min(dp[j-c]+1, dp[j])
        
        return dp[amount] if dp[amount] != float("inf") else -1