class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            valid.append(t)
        
        now = [-1,-1,-1]

        for v in valid:
            now[0] = max(now[0],v[0])
            now[1] = max(now[1],v[1])
            now[2] = max(now[2],v[2])

            if now == target:
                return True
            
        return False
            
        
