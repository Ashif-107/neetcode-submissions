class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        i = 0
        j = l
        while j < len(s2)+1:
            win = s2[i:j]
            print(win)
            if sorted(win) == sorted(s1):
                return True
            
            i+= 1
            j+= 1
        
        return False