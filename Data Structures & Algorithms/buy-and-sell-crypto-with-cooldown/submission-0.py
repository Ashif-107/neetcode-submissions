from functools import cache

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, buying):
            if i >= n:
                return 0

            if buying:
                buy = dfs(i + 1, False) - prices[i]
                skip = dfs(i + 1, True)
                return max(buy, skip)
            else:
                sell = prices[i] + dfs(i + 2, True)  # cooldown
                hold = dfs(i + 1, False)
                return max(sell, hold)

        return dfs(0, True)