class Solution:
    def trap(self, h: List[int]) -> int:
        res = 0
        i = 0
        j = len(h) - 1

        maxl = h[i]
        maxr = h[j]
        while i < j:
            if maxl < maxr:
                i += 1
                maxl = max(maxl, h[i])
                res += maxl - h[i]
            else:
                j -=1 
                maxr = max(maxr,h[j])
                res += maxr - h[j]

        return res