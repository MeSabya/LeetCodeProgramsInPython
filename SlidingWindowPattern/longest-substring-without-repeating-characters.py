class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        max_len = 0
        unique_str = {}        
        while end < len(s):
            if s[end] not in unique_str:
                unique_str[s[end]] = True
                max_len = max(len(unique_str), max_len)
                end = end+1
            else:
                del unique_str[s[start]]
                start = start+1
        return max_len