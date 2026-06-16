class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        countT = Counter(t)
        window = {}

        have = 0
        need = len(countT)

        res = [-1,-1]
        reslen = float("infinity")
        i = 0
        for j in range(len(s)):
            c = s[j]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (j-i + 1) < reslen:
                    reslen = j-i+1
                    res = [i,j]
                
                window[s[i]] -= 1
                if s[i] in countT and window[s[i]] < countT[s[i]]:
                    have -= 1
                i += 1
        
        return s[res[0]: res[1]+1]

