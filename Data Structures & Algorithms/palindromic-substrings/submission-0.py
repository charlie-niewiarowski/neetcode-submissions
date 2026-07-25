# Let's find the number of unique palindromic substrings in a string
# A palindrome can be identified by the index it starts with, ends with, or is the middle


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # for odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l, r = l - 1, r + 1
            # for even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l, r = l - 1, r + 1
        return res