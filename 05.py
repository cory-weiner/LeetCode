#  Longest Palindromic Substring    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = ''
        for i,c in enumerate(s):
            for x in range(i, len(s)+1):
                if is_palendrome(s[i:x]):
                    if len(s[i:x]) > len(longest): longest = s[i:x]
        return longest

def is_palendrome(s):
    return s == s[::-1]

print(Solution().longestPalindrome('aa'))