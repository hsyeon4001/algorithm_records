# 347. Top K Frequent Elements
# 1) Counter => 84ms / 18.5MB
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
            
        topk = list()
        
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        
        return topk
        
# 2) zip, * => 100ms / 18.4MB
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]