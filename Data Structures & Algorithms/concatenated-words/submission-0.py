class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def canConcatenate(s):
            n = len(s)
            dp = [False] * (n + 1)
            dp[n] = True

            for i in range(n - 1, -1, -1):
                for w in words:
                    if s == w:
                        continue
                    if i + len(w) <= n and s[i : i + len(w)] == w:
                        dp[i] = dp[i + len(w)]
                    if dp[i]:
                        break
            return dp[0]
        
        res = []
        for w in words:
            if canConcatenate(w):
                res.append(w)
        
        return res