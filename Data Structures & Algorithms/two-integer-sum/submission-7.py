class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            s = {}

            for i,b in enumerate(nums):
                a = target - b
                if a in s:
                    return([s[a],i])
                
                s[b] = i
            