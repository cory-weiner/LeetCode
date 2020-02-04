# Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_l = 1
        for i,c in enumerate(s):
            curr_string = [c]
            for char in s[i+1:]:            
                if char in curr_string:
                    break
                curr_string.append(char)
            max_l = max(len(curr_string),max_l)
        return max_l

            




print(Solution().lengthOfLongestSubstring('pwwkew'))
