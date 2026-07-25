class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            day, currTotal = 1, 0
            for w in weights:
                if currTotal + w > cap:
                    currTotal = 0
                    day += 1
                
                currTotal += w
            return day <= days

        """////////////////////////////////////////////"""

        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            m = (l + r) // 2

            if canShip(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

