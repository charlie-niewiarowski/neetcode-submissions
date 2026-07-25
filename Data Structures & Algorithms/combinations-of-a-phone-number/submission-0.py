class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, sol):
            if i == len(digits):
                res.append(''.join(sol[:]))
                return
            
            for c in digitToChar[digits[i]]:
                sol.append(c)
                backtrack(i + 1, sol)
                sol.pop()
        
        backtrack(0, [])
        return [] if res == [""] else res