class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def merge(l1, l2):
            res = [0] * 3
            for i in range(3):
                res[i] = max(l1[i], l2[i])
            return res

        curr = [0, 0, 0]
        for tri in triplets:
            shouldMerge = True
            for i in range(3):
                if tri[i] > target[i]:
                    shouldMerge = False
                    break
            if shouldMerge:
                curr = merge(curr, tri)

            if curr == target:
                return True
        
        return False
            