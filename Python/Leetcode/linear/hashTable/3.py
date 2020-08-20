# 3. Longest Substring Without Repeating Characters
# 1) 투 포인터 => 48ms / 13.9MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_len = start = 0

        for idx, char in enumerate(s):
            if char in used and used[char] >= start:
                start = used[char] + 1
            else:
                max_len = max(max_len, idx - start + 1)
        
            used[char] = idx
        
        return max_len