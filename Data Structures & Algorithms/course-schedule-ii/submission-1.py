class Solution:
    def findOrder(self, n: int, prereq: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u,v in prereq:
            graph[v].append(u)
        
        res = []
        state = [0]*n
        nums = 0

        def dfs(node):
            state [node] = 1

            for nei in graph[node]:
                if state[nei] == 1:
                    return False
                
                if state[nei] == 0:
                    if not dfs(nei):
                        return False
            
            state[node] = 2
            res.append(node)
            return True
        
        for node in range(n):
            if state[node] == 0:
                if not dfs(node):
                    return []
        
        res.reverse()
        return res