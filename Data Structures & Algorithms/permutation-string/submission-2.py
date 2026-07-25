class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        original = {}
        count = {}
        for i in range(len(s1)):
            original[s1[i]] = 1 + original.get(s1[i], 0)
            count[s2[i]] = 1 + count.get(s2[i], 0)
        print(original)
        if original == count:
            return True

        l, r = 0, len(s1) - 1
        while r < len(s2) - 1:       
            l += 1
            r += 1

            if count[s2[l - 1]] > 1:
                count[s2[l - 1]] -= 1
            else:
                del count[s2[l - 1]]

            count[s2[r]] = 1 + count.get(s2[r], 0)
            
            print(count)
            if count == original:
                return True
        return False