class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = {}
        win = {}
        wl = len(s1)
        
        for c in s1:
            need[c] = need.get(c,0) + 1
        
        for i in range(wl):
            win[s2[i]] = win.get(s2[i],0) + 1

        for right in range(wl, len(s2)):
            if(win == need):
                return True
            
            win[s2[right]] = win.get(s2[right], 0) + 1
            win[s2[right - wl]] -= 1
            if win[s2[right - wl]] == 0:
                del win[s2[right - wl]]
        
        return win == need