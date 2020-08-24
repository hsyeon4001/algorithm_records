# 389. Find the Difference
# 1) 문자열 치환 => 32ms / 13.8MB
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in s:
            if char in t:
                t = t.replace(char, '', 1)
        
        return t

# 2) Counter => 28ms / 14.1MB
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        
        s_dict = Counter(s)
        t_dict = Counter(t)
        
        for k in t_dict.keys():
            if s_dict[k] != t_dict[k]:
                return k

# 3) ASCII => 20ms / 13.6MB
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(97,97+26):
            if s.count(chr(i))!=t.count(chr(i)):
                return chr(i)