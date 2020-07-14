# 1493
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        arr = []
        for i, v in enumerate(nums):
            if v == 0:
                arr.append(i)
        answer = 0
        if len(arr) == 0 or len(arr) == 1:
            return len(nums) - 1
        for i, v in enumerate(arr):
            left = -1 if i == 0 else arr[i-1]
            right = len(nums) if i == len(arr)-1 else arr[i+1]
            answer = max(answer, right-left-2)

        return answer