from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 == 1:
            return False
        target = total // 2

        dp = [[False]*(target+1) for _ in range(n+1)]
        dp[0][0] = True

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            current = nums[i - 1]

            for s in range(target + 1):

                dp[i][s] = dp[i - 1][s]

                if current <= s:
                    dp[i][s] = dp[i][s] or dp[i - 1][s - current]
        
        return dp[n][target]