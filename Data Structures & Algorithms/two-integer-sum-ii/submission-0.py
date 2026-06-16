class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}

        for i, b in enumerate(numbers):
            a = target - b
            if a in d:
                return [d[a],i+1]
            
            d[b] = i+1