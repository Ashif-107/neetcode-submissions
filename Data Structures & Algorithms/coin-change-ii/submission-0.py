class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        
        for i in range(len(coins)):
            c = coins[i]
            for j in range(c,amount+1):
                dp[j] += dp[j-c]
        
        return dp[amount]