class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = defaultdict(list)
        indeg = [0]*(n+1)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indeg[u] += 1
            indeg[v] += 1
        
        q = deque()
        for i in range(1,n+1):
            if indeg[i] == 1:
                q.append(i)
        
        while q:
            node = q.popleft()
            indeg[node] -= 1

            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 1:
                    q.append(nei)
        
        for u,v in reversed(edges):
            if indeg[u] == 2 and indeg[v]:
                return [u,v]
         
        return []