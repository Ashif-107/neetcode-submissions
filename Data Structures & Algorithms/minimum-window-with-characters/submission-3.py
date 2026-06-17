class Solution:
    def minWindow(self, s: str, t: str) -> str:
        valid = 0
        left = 0
        right = 0
        length = float("inf")
        start = 0

        need = {}
        win = {}
        for c in t:
            need[c] = need.get(c,0)+1
        
        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                win[c] = win.get(c,0)+1
                if win[c] == need[c]:
                    valid += 1
            
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                
                d = s[left]
                left += 1

                if d in need:
                    if win[d] == need[d]:
                        valid -= 1
                    win[d] -= 1

        
        return "" if length == float("inf") else s[start:start+length]