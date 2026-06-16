class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        ct = {}
        for T in t:
            ct[T] = 1 + ct.get(T,0)
        
        ans = [-1,-1]
        l = float("infinity")

        for i in range(len(s)):
            countwindow = {}
            for j in range(i,len(s)):
                countwindow[s[j]] = 1 + countwindow.get(s[j],0)

                flag = True
                for c in ct:
                    if ct[c] > countwindow.get(c,0):
                        flag = False
                        break
                
                if flag and (j-i+1) < l:
                    l = j-i+1
                    ans = [i,j]

        return s[ans[0] : ans[1] + 1] if len != float("infinity") else ""