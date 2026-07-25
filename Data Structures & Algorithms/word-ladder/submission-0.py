class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = [len(wordList) + 1] * 1

        def backtrack(i, word):
            print(word, i)
            if word == endWord:
                res[0] = min(res[0], i)
                return
            if i == len(wordList):
                return 

            possibleWords = []
            for w in wordList:
                differences = 0
                for j in range(len(w)):
                    if word[j] != w[j]:
                        differences += 1
                if differences == 1:
                    possibleWords.append(w)
            for w in possibleWords:
                backtrack(i + 1, w)

        backtrack(1, beginWord)
        return 0 if res[0] == len(wordList) + 1 else res[0]

                