class Solution:
    def reverse(self, x: int) -> int:
        MIN = -(2**31)
        MAX = 2**31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            tmp = (res * 10) + digit
            print(tmp)
            if tmp > MAX or tmp < MIN:
                return 0
            res = tmp
        
        return res