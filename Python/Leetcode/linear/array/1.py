# 1. Two Sum
# 1) for문(brute force) => 6024ms / 14.6MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 2) in 탐색 => 1136ms / 14.7MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            print(i, n, complement)
            if complement in nums[i + 1:]:
                print('pass', n, complement)
                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

# 3) 해시테이블 => 48ms / 15.9MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]

# 4) 해시테이블2 => 48ms / 15.1MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
