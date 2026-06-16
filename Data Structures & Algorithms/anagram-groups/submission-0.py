from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for st in strs:
            key = ''.join(sorted(st))

            dic[key].append(st)

        return list(dic.values()) 
        