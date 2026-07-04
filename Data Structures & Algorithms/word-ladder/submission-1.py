class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)

        if endWord not in wordset:
            return 0
        
        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps
            
            word = list(word)

            for i in range(len(word)):
                original = word[i]

                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original:
                        continue
                    
                    word[i] = c
                    newword = "".join(word)

                    if newword in wordset and newword not in visited:
                        visited.add(newword)
                        q.append((newword,steps+1))
                
                word[i] = original
            
        return 0