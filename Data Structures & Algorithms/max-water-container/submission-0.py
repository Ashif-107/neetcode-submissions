class Solution:
    def maxArea(self, h: List[int]) -> int:
        res = 0
        i = 0
        j = len(h) - 1

        while i < j:
            vol = (j-i) * min(h[i],h[j])
            res = max(res,vol)

            if h[i] <= h[j]:
                i+=1
            else:
                j-=1
            
            
        

        return res