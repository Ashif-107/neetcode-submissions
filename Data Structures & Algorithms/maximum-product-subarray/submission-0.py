class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        gmax = nums[0]
        cmax = nums[0]
        cmin = nums[0]

        for i in range(1,len(nums)):
            num = nums[i]

            if num < 0:
                cmax, cmin = cmin, cmax
            
            cmax = max(num, cmax*num)
            cmin = min(num, cmin*num)

            gmax = max(cmax, gmax)
        
        return gmax