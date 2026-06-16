class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = j = 0
        char = defaultdict(int)
        max_freq = 0

        max_len = 0
        while j < len(s):
            char[s[j]] += 1
            max_freq = max(max_freq, char[s[j]])

            if (j - i + 1) - max_freq > k :
                char[s[i]] -= 1
                i += 1
            
            max_len = max(max_len, j-i+1)
            j+= 1

        return max_len