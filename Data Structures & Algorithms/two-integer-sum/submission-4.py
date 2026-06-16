class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            s = {}

            for i, a in enumerate(nums):
                b = target - a
                if b in s:
                    return [s[b],i]  
                
                s[a] = i

            return []