# 561. Array Partition I
# 1) sort => 320ms / 16.2MB
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()
        
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        
        return sum

# 2) 인덱스 짝수 => 296ms / 16.1MB
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n        
        
        return sum

# 3) 슬라이싱 => 268ms / 16.1MB
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])