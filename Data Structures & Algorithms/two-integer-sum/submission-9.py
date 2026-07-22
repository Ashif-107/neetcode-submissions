class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i,num in enumerate(nums):
            a = target - num
            if a in d:
                return [d[a],i]
            
            d[num] = i

        return -1