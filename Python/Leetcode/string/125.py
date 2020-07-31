# 125 valid palindrome
# 1) 배열 =>  256 ms / 19.4 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = []
        for char in s: # O(n)
            if char.isalnum(): 
                s2.append(char.lower())
        
        while len(s2) > 1:
            if s2.pop(0) != s2.pop(): # O(n**2)
                return False
        return True

# 2) 데크 =>  64 ms / 19.1 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        from collections import deque
        dq = deque()
        for char in s: # O(n)
            if char.isalnum():
                dq.append(char.lower())
        
        while len(dq) > 1:
            if dq.popleft() != dq.pop(): # O(n)
                return False
        return True

# 3) 데크+문자열 => 56 ms / 19.8 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        from collections import deque
        dq = deque()
        for char in s:
            if char.isalnum(): # O(n)
                dq.append(char.lower())
        
        s = "".join(dq)
        return s == s[::-1]

# 4) 정규식+문자열 => 56 ms / 14.6 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = "".join(re.findall("[a-zA-Z0-9]", s)).lower()
        return s == s[::-1]