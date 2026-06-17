class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maxlength = 0
        win = set()
        while j < len(s):
            while s[j] in win:
                win.remove(s[i])
                i += 1
            
            win.add(s[j])
            maxlength = max(maxlength, j-i+1)
            j += 1
        
        return maxlength

