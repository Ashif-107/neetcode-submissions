class Solution:
    def rob(self, num: List[int]) -> int:
        if len(num) == 1:
            return num[0]            
        
        def robs(nums):
            if len(nums) == 1:
                return nums[0]
            
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
            return dp[-1]
        
        return max(robs(num[1:]), robs(num[:-1]))