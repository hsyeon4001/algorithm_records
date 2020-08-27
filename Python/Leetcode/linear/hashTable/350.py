# 350. Intersection of Two Arrays II
# 1) for문 => 84ms / 14MB
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.remove(nums1[i])
        return res

# 2) 투 포인터 => 76ms / 14MB
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j = 0, 0
        n1 = len(nums1)
        n2 = len(nums2)
        nums1_s = sorted(nums1)
        nums2_s = sorted(nums2)
        res = []
        
        while i < n1 and j < n2:
            if nums1_s[i] < nums2_s[j]:
                i += 1
            elif nums1_s[i] > nums2_s[j]:
                j += 1
            else:
                res.append(nums1_s[i])
                i += 1
                j += 1
                
        return res

# 3) Counter => 48ms / 13.9MB
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        
        answer = []
        for x, count in c1.items():
            count2 = c2.get(x, 0)
            answer += [x] * min(count, count2)
                
                
        return answer