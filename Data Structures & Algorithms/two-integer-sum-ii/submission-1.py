class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        i = 0
        j = len(n) - 1

        while i < j:
            if n[i] + n[j] == target:
                return [i+1,j+1]
            if n[i] + n[j] > target:
                j -= 1
            if n[i] + n[j] < target:
                i += 1