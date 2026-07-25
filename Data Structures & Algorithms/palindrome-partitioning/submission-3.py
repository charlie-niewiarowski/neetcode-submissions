class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True


        def backtrack(i, sol):
            if i == len(s):
                for sub in sol:
                    if not isPalindrome(sub):
                        return
                res.append(sol[:])
                return
            
            sol.append(s[i])
            backtrack(i + 1, sol)
            sol.pop()

            if i > 0:
                sol[-1] += s[i]
                backtrack(i + 1, sol)
        
        backtrack(0, [])
        return res
