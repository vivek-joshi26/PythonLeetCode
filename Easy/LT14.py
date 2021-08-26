# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        str_len = len(strs[0])
        str_first = strs[0]
        match_index  = 0
        while match_index < str_len :
            charac = str_first[match_index]
            index = 1
            while index < len(strs):
                if match_index == len(strs[index]) or charac != strs[index][match_index]:
                    return str_first[0:match_index]
                index += 1
            match_index += 1
        return str_first

s = Solution()
print(s.longestCommonPrefix( ["flower", "flow", "flowht"]))
print(s.longestCommonPrefix( ["dog","racecar","car"]))


