class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPalindrome(start, end):
            l, r = start, end
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True


        def backtrack(start, sol):
            if start == len(s):
                res.append(sol[:])
                return
            
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    sol.append(s[start:end+1])
                    backtrack(end + 1, sol)
                    sol.pop()
        
        backtrack(0, [])
        return res
