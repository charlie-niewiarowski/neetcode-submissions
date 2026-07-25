class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def backtrack(opened, closed):
            if opened + closed == n * 2:
                res.append(''.join(sol))
                return

            if opened < n:
                sol.append('(')
                backtrack(opened + 1, closed)
                sol.pop()

            if closed < opened:
                sol.append(')')
                backtrack(opened, closed + 1)
                sol.pop()

        backtrack(0, 0)
        return res
