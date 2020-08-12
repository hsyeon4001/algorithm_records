# 26. Remove Duplicates from Sorted Array
# 1) 포인터 => 88ms / 15.4MB
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if num != nums[i]:
                i += 1
                nums[i] = num
        return i + 1
