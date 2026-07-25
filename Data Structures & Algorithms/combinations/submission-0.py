class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, sol):
            if len(sol) == k:
                res.append(sol[:])
                return
            if i > n:  
                return

            sol.append(i)
            backtrack(i + 1, sol)
            sol.pop()
            backtrack(i + 1, sol)
        
        backtrack(1, [])
        return res

            
