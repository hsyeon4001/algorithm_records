# 387. First Unique Character in a String
# 1) Counter => 56ms / 13.9MB
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        dict = Counter(s)
        min_idx = len(s) - 1
        
        if 1 not in dict.values():
            return -1
        
        for k, v in dict.items():
            if v == 1:
                min_idx = min(s.index(k), min_idx)
            
        return min_idx