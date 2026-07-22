class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        left = 0
        right = 0

        last = {}
        for i,c in enumerate(s):
            last[c] = i
        
        for i,ch in enumerate(s):
            right = max(right, last[ch])

            if i == right:
                l = right - left + 1
                ans.append(l)
                left = right + 1
        
        return ans