class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
        self.comps = n

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        self.comps -= 1
        if self.size[pu] < self.size[pv]:
            pu,pv = pv,pu
        
        self.size[pu] += self.size[pu]
        self.parent[pv] = pu

        return True

    def compss(self):
        return self.comps


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        dsu = DSU(n)
        for u,v in edges:
            if not dsu.union(u,v):
                return False
        
        return dsu.compss() == 1