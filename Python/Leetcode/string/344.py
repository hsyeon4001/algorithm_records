# 344. Reverse String
# 1) 포인터 => 216 ms / 18.1 MB
class Solution:
    def reverseString(self, s: List[str]) -> None:
        a, b = 0, len(s)-1
        while a < b:
            s[a], s[b] = s[b], s[a]
            a += 1
            b -= 1

# 2) reverse 함수
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

# ※ input이 문자열일 경우 : 슬라이싱
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s = s[::-1]