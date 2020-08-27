# 167. Two Sum II - Input array is sorted
# 1) 투 포인터 => 시간초과
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, i+1
        while i < len(numbers)-1:
            if numbers[i]+numbers[j] == target:
                return [i+1, j+1]
            elif j == len(numbers)-1:
                i += 1
                j = i+1
            else:
                j += 1
                