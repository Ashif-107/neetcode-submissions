class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = 0
        n = len(nums)

        memo = {}
        def dp(i,s):
            if (i,s) in memo:
                return memo[(i,s)]

            if i == n:
                return 1 if s == target else 0
                
            curr = nums[i]
            ans = dp(i+1,s+curr) + dp(i+1,s-curr)
            memo[(i,s)] = ans
            return ans
            
        return dp(0,0)