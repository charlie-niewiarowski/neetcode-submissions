class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n, res, seen = len(candidates), [], set()

        def backtrack(i, sol, total):
            if total == target:
                product = 1
                for num in sol:
                    product *= num
                
                if product not in seen:
                    seen.add(product)
                    res.append(sol[:])
                return
            if i == n:
                return
            
            backtrack(i + 1, sol, total)

            sol.append(candidates[i])
            backtrack(i + 1, sol, total + candidates[i])
            sol.pop()
        
        backtrack(0, [], 0)
        return res
            

                