class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u,v in prereq:
            graph[v].append(u)
        
        state = [0]*numCourses

        def dfs(node):
            state[node] = 1

            for nei in graph[node]:
                if state[nei] == 1:
                    return False
                
                if state[nei] == 0:
                    if not dfs(nei):
                        return False
            
            state[node] = 2
            return True
        
        for node in range(numCourses):
            if state[node] == 0:
                if not dfs(node):
                    return False
        
        return True
