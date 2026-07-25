class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            if (r - l - 1) > resLen:
                resLen = r - l - 1
                resIdx = i

            # even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            if (r - l - 1) > resLen:
                resLen = r - l - 1
                resIdx = i
        
        start = resIdx - (resLen - 1) // 2
        return s[start:start + resLen]



