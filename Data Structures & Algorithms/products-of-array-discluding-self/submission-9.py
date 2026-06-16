class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = 1
        suffix[len(nums)-1] = 1

        for i in range(1,len(nums)):
            prefix[i] = nums[i-1]*prefix[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = nums[i+1]*suffix[i+1]
        
        for i,n in enumerate(nums):
            res.append(prefix[i]*suffix[i])

        return res