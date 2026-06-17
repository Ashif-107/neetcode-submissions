class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        maxfreq = 0
        ans = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxfreq = max(maxfreq, freq[s[right]])
            rep = (right-left+1) - maxfreq
            if rep > k:
                freq[s[left]] -= 1
                left += 1
            
            ans = max(ans, right-left+1)

        return ans