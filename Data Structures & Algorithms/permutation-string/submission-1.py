class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1c = Counter(s1)
        win = Counter(s2[:len(s1)])

        if s1c == win:
            return True
        
        for i in range(len(s1),len(s2)):
            win[s2[i]] += 1
            win[s2[i-len(s1)]] -= 1

            if s1c == win:
                return True

        return False