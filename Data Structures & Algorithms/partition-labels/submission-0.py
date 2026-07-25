class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndices = {}
        for i in range(len(s)):
            lastIndices[s[i]] = i
        
        res = []
        i = 0
        while i < len(s):
            start, endIdx = i, i
            while i <= endIdx:
                endIdx = max(endIdx, lastIndices[s[i]])
                i += 1
            res.append(i - start)

        return res