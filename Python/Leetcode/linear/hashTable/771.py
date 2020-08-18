# 771. Jewels and Stones
# 1) 해시테이블 => 28ms / 13.8MB
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stones = {}
        cnt = 0
        for s in S:
            if s not in stones:
                stones[s] = 1
            else:
                stones[s] +=1
        
        for j in J:
            if j in stones:
                cnt += stones[j]
        
        return cnt

# 2) defaultdict => 32ms / 13.7MB
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stones = collections.defaultdict(int)
        cnt = 0
        
        for s in S:
            stones[s] += 1
        
        for j in J:
            if j in stones:
                cnt += stones[j]
        
        return cnt

# 3) Counter => 28ms / 13.8MB
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stones = collections.Counter(S)
        cnt = 0
        
        for j in J:
            cnt += stones[j]
        
        return cnt

# 4) 파이썬st => 24ms / 13.7MB
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)
