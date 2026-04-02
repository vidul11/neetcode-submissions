class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        chars = {}
        
        for right in range(len(s)):
            if s[right] in chars and chars[s[right]] >= left:
                left = chars[s[right]] + 1
            
            chars[s[right]] = right
            
            max_length = max(max_length, right - left + 1)
        
        return max_length