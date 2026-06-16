class Solution:
    def maxProfit(self, p: List[int]) -> int:
        max_price = 0
        x = p[0]
        i = 0
        for j in range(1,len(p)):
            if p[j] < x:
                x = p[j]
                i = j
                continue
            
            max_price = max(max_price, (p[j] - x ))
        

        return max_price