class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l, r = 0, 1
        longest = 1
        while r < len(s):
            if s[r] in s[l: r]:
                print("true")
                while s[r] in s[l: r]:
                    l += 1
            current = r - l + 1
            longest = max(current, longest)

            r += 1
        return longest
