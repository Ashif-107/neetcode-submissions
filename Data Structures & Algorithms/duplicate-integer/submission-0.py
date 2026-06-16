class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        clone = []
        for num in nums:
            if num in clone:
                return True
            else:
                clone.append(num)
        return False
        