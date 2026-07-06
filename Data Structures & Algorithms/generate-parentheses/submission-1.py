class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ""
        
        def dfs(oc, cc, path):    
            if len(path) == 2*n:
                res.append(path[:])
                return
            
            if oc < n:
              dfs(oc+1, cc, path + '(')  
            
            if cc < oc:
                dfs(oc, cc+1, path + ")")
        
        dfs(0,0,"")
        return res