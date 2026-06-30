class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        count = 0

        def dfs(node):
            if node in visit:
                return 
            
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
            

        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)

        return count