class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length()
        peak = -1

        while l <= r:
            m = (l + r) // 2
            curr, prev, nxt = mountainArr.get(m), mountainArr.get(m - 1), mountainArr.get(m + 1)

            if curr > prev and curr > nxt:
                peak = m
                break
            elif curr > prev and curr < nxt:
                l = m + 1
            else:
                r = m - 1
        
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            curr = mountainArr.get(m)
            if curr == target:
                return m
            elif curr < target:
                l = m + 1
            else:
                r = m - 1
        
        l, r = peak, mountainArr.length()
        while l <= r:
            m = (l + r) // 2
            curr = mountainArr.get(m)
            if curr == target:
                return m
            elif curr > target:
                l = m + 1
            else: 
                r = m - 1
        
        return -1


