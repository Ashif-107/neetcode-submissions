class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        i = 0
        j = len(height) - 1

        maxl = height[i]
        maxr = height[j]

        while i < j:
            if maxl < maxr:
                i += 1
                h = height[i]
                maxl = max(maxl, h)
                ans += maxl-h
            else:
                j -= 1
                h = height[j]
                maxr = max(maxr, h)
                ans += maxr - h
        
        return ans