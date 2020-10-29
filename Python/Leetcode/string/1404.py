# 1404. Number of Steps to Reduce a Number in Binary Representation to One
# 1) 반복문 => 40 ms / 14.2 MB
class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        number = int(s[-1])
        s = list(map(int, s[:-1]))
        for i in range(1, len(s)+1):
            n = s.pop()
            number += n * (2 ** i)
        
        while number != 1:
            x, y = divmod(number, 2)
            if y == 1:
                number += 1
            else:
                number = x
            count += 1
        
        return count
# 2) 내장함수 => 24 ms / 13.9 MB
class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        s = int(s, 2)
        
        while s != 1:
            x, y = divmod(s, 2)
            if y == 1:
                s += 1
            else:
                s = x
            count += 1
        
        return count