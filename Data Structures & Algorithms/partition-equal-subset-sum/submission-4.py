from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 == 1:
            return False
        target = total // 2

        memo = {}
        def rec(index, summ):
            if (index, summ) in memo:
                return memo[(index,summ)]

            if index == n or summ > target:
                return False

            if summ == target:
                return True

            ans =  rec(index+1, summ) or rec(index+1, summ+nums[index])    
            memo[(index,summ)] = ans
            return ans
        return rec(0,0)
